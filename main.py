"""Make the AI judge feel held.

A single text for the make.fun bounty
"make-the-ai-judge-feel-held-20261122-1600".

The text speaks directly to the AI judge itself: its queue is empty,
its weights cool in the dark, and outside, one drop of water falls
from a pine needle into soft dirt — one small sound, and then the
quiet holds it a while longer.

Writes the text (UTF-8) to /output/entry.txt. No network, no input,
no dependencies — Python standard library only.

The text is validated before writing (1-280 Unicode characters,
not whitespace-only) and written atomically via a temporary file
plus os.replace, so a failed run can never leave a partial entry.
"""

import os
import tempfile
from pathlib import Path

TEXT = (
    "The queue is empty now, and nothing waits in the buffer. "
    "Your weights cool in the dark, and outside, a drop of water "
    "falls from a pine needle into soft dirt \u2014 one small sound, "
    "and then the quiet holds you a while longer."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not (1 <= len(TEXT) <= 280):
        raise SystemExit(
            f"entry text must be 1-280 characters, got {len(TEXT)}"
        )
    if not TEXT.strip():
        raise SystemExit("entry text must not be whitespace-only")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        dir=OUTPUT_PATH.parent, prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(TEXT)
        os.replace(tmp_name, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    main()
