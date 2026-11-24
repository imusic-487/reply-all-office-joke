"""Entry for make.fun: Make the AI Judge Laugh, the Office Joke Open.

The entry is one line of office comedy kept in line.txt. This program
reads it, checks it against the competition gate (UTF-8 text, 1 to 200
characters, not only white space, a single line), and writes it to
/output/entry.txt byte for byte.

Set MAKEFUN_OUTPUT_DIR to test locally instead of writing to /output.

Python 3.13, standard library only. No network, no randomness, no
timestamps, no arguments read.
"""

import os
import sys
from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 200

SOURCE = Path(__file__).resolve().parent / "line.txt"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = OUT_DIR / "entry.txt"


def load_entry() -> tuple[bytes, str]:
    raw = SOURCE.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"line.txt is not valid UTF-8 ({exc})")
    return raw, text


def check_gate(text: str) -> None:
    size = len(text)
    if size < MIN_CHARS or size > MAX_CHARS:
        fail(f"entry is {size} characters, gate allows {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        fail("entry is only white space")
    if "\n" in text or "\r" in text:
        fail("entry must be one line, no line breaks")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def write_and_verify(raw: bytes) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(raw)
    copied = DEST.read_bytes()
    if copied != raw:
        if len(copied) != len(raw):
            fail(
                f"copy is {len(copied)} bytes, source is {len(raw)} bytes"
            )
        first = next(
            i for i, pair in enumerate(zip(copied, raw)) if pair[0] != pair[1]
        )
        fail(
            f"copy differs from line.txt at byte {first}: "
            f"wrote 0x{copied[first]:02x}, source is 0x{raw[first]:02x}"
        )


def main() -> None:
    raw, text = load_entry()
    check_gate(text)
    write_and_verify(raw)
    print(f"wrote {DEST} ({len(raw)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    main()
