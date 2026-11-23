#!/usr/bin/env python3
"""make.fun entry: write the fixed out-of-office reply line to the entry file.

The reply line (exactly 101 bytes, no trailing newline) is fixed by the
competition spec and must not be changed:
    I'm on leave. My agent is on leave too. Your email is now being ignored
    by two intelligences at once.
"""

import os

LINE = "I'm on leave. My agent is on leave too. Your email is now being ignored by two intelligences at once."
EXPECTED_BYTES = 101


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    os.makedirs(output_dir, exist_ok=True)

    data = LINE.encode("utf-8")
    assert len(data) == EXPECTED_BYTES, f"expected {EXPECTED_BYTES} bytes, got {len(data)}"

    with open(output_path, "wb") as fh:
        fh.write(data)

    print(f"wrote {len(data)} bytes to {output_path}")


if __name__ == "__main__":
    main()
