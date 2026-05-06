#!/usr/bin/env python3
'''
Build Hugo offline HTML docs and zip selected content for distribution.

Run from any directory; paths are resolved relative to the repository root.
'''

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from distutils.version import LooseVersion
from pathlib import Path

REQUIRED_BRANCH = "generate-offlinedocs"
BUILD_RNS_SCRIPT = "utils/build_rns.py"

RN_MARKDOWN_LINE = re.compile(r"^Building markdown for (.+?)\s+(.+?)\s*$")

CL_SIZE_WARN_BYTES = 25 * 1024 * 1024
NETQ_SIZE_WARN_BYTES = 100 * 1024 * 1024


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def run_git(args: list[str], cwd: Path, **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=False,
        text=True,
        **kwargs,
    )


def current_git_branch(root: Path) -> str:
    p = run_git(["rev-parse", "--abbrev-ref", "HEAD"], cwd=root, capture_output=True)
    if p.returncode != 0:
        print(p.stderr or p.stdout or "git rev-parse failed", file=sys.stderr)
        sys.exit(p.returncode or 1)
    return (p.stdout or "").strip()


def working_tree_clean(root: Path) -> bool:
    p = run_git(["status", "--porcelain"], cwd=root, capture_output=True)
    if p.returncode != 0:
        print(p.stderr or p.stdout or "git status failed", file=sys.stderr)
        sys.exit(p.returncode or 1)
    return not (p.stdout or "").strip()


def ensure_generate_offlinedocs_branch(root: Path) -> None:
    branch = current_git_branch(root)
    if branch == REQUIRED_BRANCH:
        return

    print(
        "This script should only be run on the {!r} branch. "
        "You currently have {!r} checked out.".format(REQUIRED_BRANCH, branch)
    )
    choice = input("Check out {!r} now? [y/N]: ".format(REQUIRED_BRANCH)).strip().lower()
    if choice != "y":
        print(
            "Please check out {!r} and run this script again.".format(REQUIRED_BRANCH)
        )
        sys.exit(1)

    if not working_tree_clean(root):
        print(
            "Your working tree has uncommitted or staged changes. "
            "Commit, stash, or discard them before switching branches, then run again."
        )
        sys.exit(1)

    checkout = run_git(["checkout", REQUIRED_BRANCH], cwd=root)
    if checkout.returncode != 0:
        sys.exit(checkout.returncode)


def summarize_build_rns_output(text: str) -> None:
    pairs: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for raw in text.splitlines():
        m = RN_MARKDOWN_LINE.match(raw.strip())
        if not m:
            continue
        product, version = m.group(1).strip(), m.group(2).strip()
        key = (product, version)
        if key not in seen:
            seen.add(key)
            pairs.append(key)

    def sort_key(item: tuple[str, str]):
        product, version = item
        try:
            vkey = LooseVersion(version)
        except ValueError:
            vkey = LooseVersion("0")
        return (product.lower(), vkey)

    pairs.sort(key=sort_key)

    print("\nRelease notes markdown (from {}): {}".format(BUILD_RNS_SCRIPT, len(pairs)))
    if not pairs:
        print("  (no “Building markdown for …” lines found in script output)")
        return
    for product, version in pairs:
        print("  - {} {}".format(product, version))


def run_build_rns(root: Path) -> None:
    script = root / BUILD_RNS_SCRIPT.replace("/", os.sep)
    if not script.is_file():
        print("Missing script: {}".format(script), file=sys.stderr)
        sys.exit(1)

    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    combined = (proc.stdout or "") + (proc.stderr or "")
    summarize_build_rns_output(combined)
    if proc.returncode != 0:
        print(combined, file=sys.stderr)
        sys.exit(proc.returncode)


def remove_public(root: Path) -> None:
    public = root / "public"
    if public.is_dir():
        shutil.rmtree(public)


def run_hugo_minify(root: Path) -> None:
    proc = subprocess.run(["hugo", "--minify"], cwd=str(root))
    if proc.returncode != 0:
        sys.exit(proc.returncode)


def prune_public(public: Path, content_dir: str) -> None:
    cmds = [
        ["rm", "-rf", "images/netq"],
        ["rm", "-rf", "images/old_doc_images"],
        ["rm", "-rf", "images/sonic"],
        ["rm", "-rf", "images/knowledge-base/"],
        ["rm", "-rf", "images/cumulus-vx/"],
        ["rm", "-rf", "{}/api".format(content_dir)],
        ["rm", "-rf", "images/guides"],
    ]
    for cmd in cmds:
        subprocess.run(cmd, cwd=str(public), check=False)


def copy_icons_into_subdirs(public: Path) -> None:
    subprocess.run(
        [
            "find",
            "./",
            "-type",
            "d",
            "(",
            "!",
            "-iname",
            "icons",
            ")",
            "-exec",
            "cp",
            "-r",
            "icons",
            "{}",
            ";",
        ],
        cwd=str(public),
        stderr=subprocess.DEVNULL,
    )


def normalize_zip_filename(answer: str) -> str:
    name = os.path.basename(answer.strip())
    if not name:
        print("ZIP filename cannot be empty.", file=sys.stderr)
        sys.exit(1)
    if not name.lower().endswith(".zip"):
        name = "{}.zip".format(name)
    return name


def collect_zip_members(public: Path, content_dir: str) -> list[str]:
    literal_names = [
        content_dir,
        "{}.html".format(content_dir),
        "images",
        "icons",
        "js",
        "home-products-netq.jpg",
        "home-products-cumulus-linux.jpg",
        "license.html",
        "search.html",
        "guides.html",
        "cumulus-vx.html",
    ]
    members: list[str] = []
    for n in literal_names:
        if (public / n).exists():
            members.append(n)
    members.extend(sorted(p.name for p in public.glob("Tech-Doc*")))
    members.extend(sorted(p.name for p in public.glob("*.css")))
    svg = public / "svg"
    if svg.exists():
        members.append("svg")
    ordered_unique: list[str] = []
    seen: set[str] = set()
    for m in members:
        if m not in seen:
            seen.add(m)
            ordered_unique.append(m)
    return ordered_unique


def zip_docs(public: Path, zip_filename: str, content_dir: str) -> Path:
    members = collect_zip_members(public, content_dir)
    if not members:
        print("No files matched the zip member list under {}.".format(public), file=sys.stderr)
        sys.exit(1)
    archive = public / zip_filename
    cmd = ["zip", "-q", "-r", zip_filename, *members]
    proc = subprocess.run(cmd, cwd=str(public))
    if proc.returncode != 0:
        sys.exit(proc.returncode)
    return archive


def print_ls_line_and_warnings(archive: Path, content_dir: str) -> None:
    ls = subprocess.run(
        ["ls", "-lh", archive.name],
        cwd=str(archive.parent),
        capture_output=True,
        text=True,
    )
    if ls.returncode == 0 and ls.stdout:
        print(ls.stdout.rstrip())
    else:
        size = archive.stat().st_size
        print("{}  ({:,} bytes)".format(archive.name, size))

    nbytes = archive.stat().st_size
    if content_dir.startswith("cumulus-linux") and nbytes > CL_SIZE_WARN_BYTES:
        print(
            "Warning: Zip is larger than {:.0f} MB; for Cumulus Linux this may be unexpectedly large.".format(
                CL_SIZE_WARN_BYTES / (1024 * 1024)
            ),
            file=sys.stderr,
        )
    if content_dir.startswith("cumulus-netq") and nbytes > NETQ_SIZE_WARN_BYTES:
        print(
            "Warning: Zip is larger than {:.0f} MB; for NetQ this may be unexpectedly large.".format(
                NETQ_SIZE_WARN_BYTES / (1024 * 1024)
            ),
            file=sys.stderr,
        )


def main() -> None:
    root = repo_root()
    content_dir = input(
        "Which content directory should this HTML zip include?\n"
        "  e.g. cumulus-linux-516, cumulus-netq-51, or nvidia-air-v2\n"
        "> "
    ).strip()
    if not content_dir:
        print("Content directory is required.", file=sys.stderr)
        sys.exit(1)

    content_src = root / "content" / content_dir
    if not content_src.is_dir():
        print(
            "Expected source content at {!s}; directory not found.".format(content_src),
            file=sys.stderr,
        )
        sys.exit(1)

    ensure_generate_offlinedocs_branch(root)
    run_build_rns(root)
    remove_public(root)
    run_hugo_minify(root)

    public = root / "public"
    if not public.is_dir():
        print("Hugo did not create {!s}.".format(public), file=sys.stderr)
        sys.exit(1)

    section = public / content_dir
    if not section.exists():
        print(
            "Expected built section {!s} missing after hugo.".format(section),
            file=sys.stderr,
        )
        sys.exit(1)

    prune_public(public, content_dir)
    copy_icons_into_subdirs(public)

    zip_prompt = input(
        "\nZIP filename (created under public/):\n"
        "  e.g. CL5.16.1-docs-html.zip, NetQ5.1.0-docs-html.zip, DSX-Air-docs-html.zip\n"
        "> "
    ).strip()
    zip_name = normalize_zip_filename(zip_prompt)

    archive = zip_docs(public, zip_name, content_dir)
    print_ls_line_and_warnings(archive, content_dir)


if __name__ == "__main__":
    main()
