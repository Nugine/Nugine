#!/usr/bin/env python3
import os

REPO_LIST = [
    "Nugine/s3s",
    "Nugine/simd",
    "Nugine/rlimit",
    "Nugine/const-str",
    "Nugine/zuc",
    "Nugine/numeric_cast",
    "Nugine/asc",
    "Nugine/outref",
    "Nugine/std-next",
    "Nugine/transform-stream",
    "Nugine/wgp",
    "Nugine/ordered-vecmap",
    "Nugine/rust-utils",
    "Nugine/bfjit",
    "Nugine/simdutf-rs",
    "Nugine/epkv",
    "Nugine/setup-flatc",
    "Nugine/nublog",
    "Nugine/pastebin",
]


def main():
    s = "|Repo|Status|\n"
    s += "|-|-|\n"
    for repo in REPO_LIST:
        link = f"[{repo}](https://github.com/{repo})"
        ci = f"[![CI](https://github.com/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{repo}/actions)"
        s += f"|{link}|{ci}|\n"

    tempfile = ".vscode/a.txt"
    with open(tempfile, "w") as f:
        f.write(s)

    os.system(f"gh issue edit 1 --body-file {tempfile}")
    os.remove(tempfile)


if __name__ == "__main__":
    main()
