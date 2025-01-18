#!/usr/bin/env python3
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
    "Nugine/simdutf-rs",
    "Nugine/epkv",
    "Nugine/setup-flatc",
    "Nugine/nublog",
    "Nugine/pastebin",
]


def main():
    print("|Repo|Status|")
    print("|-|-|")
    for repo in REPO_LIST:
        link = f"[{repo}](https://github.com/{repo})"
        ci = f"[![CI](https://github.com/{repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/{repo}/actions)"
        print(f"|{link}|{ci}|")


if __name__ == "__main__":
    main()
