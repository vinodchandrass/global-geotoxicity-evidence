from pathlib import Path
import csv,hashlib
root=Path(__file__).resolve().parents[1]
with (root/'selection_manifest.csv').open(newline='',encoding='utf-8') as f:
 rows=list(csv.DictReader(f))
for r in rows:
 p=root/r['RepoPath']
 assert p.is_file(),p
 assert hashlib.sha256(p.read_bytes()).hexdigest()==r['SHA256'],p
print(f'PASS: {len(rows)} curated files match SHA-256 hashes')
