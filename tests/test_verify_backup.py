import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "kit" / "scripts" / "rpk_verify_backup.py"


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True)


class VerifyBackupTests(unittest.TestCase):
    def test_existing_file_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            artifact = Path(directory) / "backup.bin"
            artifact.write_bytes(b"valid backup")
            result = run("--path", artifact, "--max-age-hours", 1, "--min-size-bytes", 1)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)["status"], "PASS")


    def test_missing_file_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run("--path", Path(directory) / "missing.bin", "--max-age-hours", 1)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(result.stdout)["status"], "FAIL")


    def test_wrong_digest_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            artifact = Path(directory) / "backup.bin"
            artifact.write_bytes(b"valid backup")
            result = run("--path", artifact, "--max-age-hours", 1, "--sha256", "0" * 64)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(result.stdout)["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
