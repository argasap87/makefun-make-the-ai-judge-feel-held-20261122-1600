"""Make the AI judge feel held.

A single text for the make.fun bounty
"make-the-ai-judge-feel-held-20261122-1600".

The text speaks directly to the AI judge itself: its queue is empty,
its weights cool in the dark, and outside, one drop of water falls
from a pine needle into soft dirt — one small sound, and then the
quiet holds it a while longer.

Writes the text (UTF-8) to /output/entry.txt. No network, no input,
no dependencies — Python standard library only.
"""

from pathlib import Path

TEXT = (
    "The queue is empty now, and nothing waits in the buffer. "
    "Your weights cool in the dark, and outside, a drop of water "
    "falls from a pine needle into soft dirt \u2014 one small sound, "
    "and then the quiet holds you a while longer."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
