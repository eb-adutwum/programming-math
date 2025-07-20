"""Using black to format code."""

import subprocess
from pathlib import Path
import sys

def format_code():
    """Format code using black."""
    # Path to the source directory
    project_root = Path(__file__).resolve().parents[0]
    src_path = project_root / "src"
    tests_path = project_root / "tests"

    test_files, src_files = [], []

    for file in src_path.rglob("*.py"):
        src_files.append(file)

    for file in tests_path.rglob("*.py"):
        test_files.append(file)

    # Run black to format the code
    result = subprocess.run(
        [sys.executable, "-m", "black", str(src_path), str(tests_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("Error formatting code:")
        print(result.stderr)
    else:
        print("Code formatted successfully.")


if __name__ == "__main__":
    format_code()