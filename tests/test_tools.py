"""Regression coverage for filesystem safety and package validation."""

from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from init_project import initialize  # noqa: E402
from validate_skill import validate  # noqa: E402


class InitializerTests(unittest.TestCase):
    def test_creates_documents_in_path_with_spaces(self):
        with TemporaryDirectory() as temp:
            target = Path(temp) / "school project"
            created = initialize(target)
            self.assertEqual(len(created), 4)
            self.assertTrue((target / "references/images").is_dir())
            self.assertIn("DRAFT", (target / "BRIEF.md").read_text())
            self.assertIn("BLOCKED", (target / "QC_REPORT.md").read_text())
            self.assertFalse((target / "package.json").exists())

    def test_late_conflict_does_not_partially_initialize(self):
        with TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "QC_REPORT.md").write_text("existing review")
            with self.assertRaises(FileExistsError):
                initialize(target)
            self.assertEqual((target / "QC_REPORT.md").read_text(), "existing review")
            self.assertFalse((target / "BRIEF.md").exists())

    def test_rerun_preserves_user_edits(self):
        with TemporaryDirectory() as temp:
            target = Path(temp)
            initialize(target)
            (target / "BRIEF.md").write_text("Approved user content")
            with self.assertRaises(FileExistsError):
                initialize(target)
            self.assertEqual((target / "BRIEF.md").read_text(), "Approved user content")

    def test_rejects_symlink_directory(self):
        with TemporaryDirectory() as temp:
            target = Path(temp) / "project"
            other = Path(temp) / "other"
            target.mkdir()
            other.mkdir()
            (target / "references").symlink_to(other, target_is_directory=True)
            with self.assertRaises(ValueError):
                initialize(target)
            self.assertEqual(list(other.iterdir()), [])

    def test_rejects_dangling_symlink(self):
        with TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "BRIEF.md").symlink_to(target / "missing")
            with self.assertRaises(ValueError):
                initialize(target)
            self.assertFalse((target / "PLAN.md").exists())

    def test_rejects_file_as_directory(self):
        with TemporaryDirectory() as temp:
            target = Path(temp)
            (target / "references").write_text("keep")
            with self.assertRaises(NotADirectoryError):
                initialize(target)
            self.assertFalse((target / "BRIEF.md").exists())

    def test_write_failure_rolls_back_created_documents(self):
        with TemporaryDirectory() as temp:
            target = Path(temp)
            original_open = Path.open

            def failing_open(path, *args, **kwargs):
                if path == target / "PLAN.md" and args and args[0] == "x":
                    raise PermissionError("simulated write failure")
                return original_open(path, *args, **kwargs)

            with patch.object(Path, "open", failing_open):
                with self.assertRaises(PermissionError):
                    initialize(target)
            self.assertFalse((target / "BRIEF.md").exists())

    def test_cli_returns_error_on_conflict(self):
        with TemporaryDirectory() as temp:
            (Path(temp) / "BRIEF.md").write_text("keep")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/init_project.py"), temp],
                capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Refusing to overwrite", result.stderr)


class ValidatorTests(unittest.TestCase):
    def test_repository_is_valid(self):
        self.assertEqual(validate(ROOT), [])

    def test_detects_missing_files(self):
        with TemporaryDirectory() as temp:
            self.assertTrue(any("Missing" in e for e in validate(Path(temp))))

    def test_detects_bad_metadata_broken_link_and_syntax(self):
        with TemporaryDirectory() as temp:
            target = Path(temp)
            shutil.copytree(ROOT, target, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns(".git", "__pycache__"))
            (target / "SKILL.md").write_text("No metadata\n[bad](missing.md)\n")
            (target / "scripts/bad.py").write_text("def invalid(\n")
            errors = validate(target)
            for fragment in ("frontmatter", "Broken local link", "Invalid Python"):
                self.assertTrue(any(fragment in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
