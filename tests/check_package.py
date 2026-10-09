from pathlib import Path
import csv
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "release_manifest_v1.0.0.csv"

def main():
    if not MANIFEST.is_file():
        print(f"FAIL: Manifest missing: {MANIFEST}")
        return 1

    with MANIFEST.open(
        "r", newline="", encoding="utf-8-sig"
    ) as f:
        reader = csv.DictReader(f)
        required = {"RepoPath", "Bytes", "SHA256", "Origin"}

        if not required.issubset(reader.fieldnames or []):
            print("FAIL: Invalid release manifest columns")
            return 1

        rows = list(reader)

    failures = []
    seen = set()

    for row in rows:
        relative = row["RepoPath"]
        path = (ROOT / relative).resolve()

        if relative in seen:
            failures.append(f"Duplicate manifest entry: {relative}")
            continue

        seen.add(relative)

        if not path.is_relative_to(ROOT.resolve()):
            failures.append(f"Path outside repository: {relative}")
            continue

        if not path.is_file():
            failures.append(f"Missing file: {relative}")
            continue

        data = path.read_bytes()
        actual_size = len(data)
        actual_hash = hashlib.sha256(data).hexdigest()

        try:
            expected_size = int(row["Bytes"])
        except (ValueError, TypeError):
            failures.append(f"Invalid byte count: {relative}")
            continue

        if actual_size != expected_size:
            failures.append(
                f"Size mismatch: {relative} "
                f"(expected {expected_size}, actual {actual_size})"
            )

        if actual_hash.lower() != row["SHA256"].strip().lower():
            failures.append(f"SHA-256 mismatch: {relative}")

    print(f"Manifest: {MANIFEST.name}")
    print(f"Files checked: {len(rows)}")
    print(f"Failures: {len(failures)}")

    if failures:
        for failure in failures:
            print("FAIL:", failure)
        return 1

    print("PASS: All release manifest checksums verified")
    return 0

if __name__ == "__main__":
    sys.exit(main())
