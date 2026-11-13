"""ai-happy-01 entry: "The robot's first laugh".

The image beside this file is the entry: a small friendly robot
laughing joyfully with a little girl and a golden puppy at sunset.
This program copies it byte-for-byte to /output/entry.png.

The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by
1024 pixels; the judge sees exactly the bytes copied. The program
runs twice and both runs must write the same bytes, so it only
copies: no network, no randomness, no timestamps in the output.

Local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"
# The gate refuses any image over 1 MiB, so fail loudly here rather
# than submit an entry the scorer would reject.
MAX_BYTES = 1048576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(src, dst)
    # Verify the copy is byte-identical to the source, and that the
    # image stays within the gate's size limit.
    with open(src, "rb") as f:
        expected = f.read()
    if len(expected) > MAX_BYTES:
        print("entry.png exceeds the 1 MiB gate limit", file=sys.stderr)
        return 1
    with open(dst, "rb") as f:
        actual = f.read()
    if actual != expected:
        print("copy mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
