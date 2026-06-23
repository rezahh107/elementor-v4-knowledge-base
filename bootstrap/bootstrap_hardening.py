#!/usr/bin/env python3
"""One-time, self-verifying bootstrap for hardening/evidence-platform-v1."""
from __future__ import annotations
import base64, hashlib, io, tarfile
from pathlib import Path

EXPECTED_SHA256 = "57e82f8a4271d3727b8f151cb3cdb211657a005f5414b29dea3d2ae5924edc31"

def main() -> None:
    root = Path(__file__).resolve().parent.parent
    encoded = "".join(
        path.read_text(encoding="ascii").strip()
        for path in sorted((root / "bootstrap").glob("payload-*.b64"))
    )
    raw = base64.b64decode(encoded, validate=True)
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_SHA256:
        raise SystemExit(f"payload SHA-256 mismatch: {actual}")
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as archive:
        members = archive.getmembers()
        for member in members:
            target = Path(member.name)
            if target.is_absolute() or ".." in target.parts or member.issym() or member.islnk():
                raise SystemExit(f"unsafe archive member: {member.name}")
        archive.extractall(root, members=members, filter="data")
    print(f"extracted {len(members)} hardening files; payload_sha256={actual}")

if __name__ == "__main__":
    main()
