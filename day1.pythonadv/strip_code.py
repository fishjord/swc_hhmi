#!/usr/bin/env python
import os, sys, argparse, json, sha, base64, re

# Directory to save image files
IMAGE_DIR = "img"

# Prefix for Markdown image URLs
IMAGE_URL_PREFIX = "img"

def cleanup(s):
    return re.sub(r"[^0-9a-zA-Z]+", "", s)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", type=str, help="Path to IPython notebook file (.ipynb)")
    parser.add_argument("--output", type=str, default=None, help="Path to output file (default: stdout)")
    args = parser.parse_args()

    out = sys.stdout
    if args.output is not None:
        out = open(args.output, "w")

    # Import notebook JSON
    notebook = json.load(open(args.notebook, "r"))

    # Only one worksheet is supported
    cells = notebook["worksheets"][0]["cells"]
    in_code = False

    # Output each cell
    for cell in cells:
        if cell["cell_type"] == "code":
            # Wrap code in Github fenced code block
            cell["input"] = []
            cell["outputs"] = []

    print >>out, json.dumps(notebook)
