#!/usr/bin/env python3
'''
Build Hugo offline HTML docs and zip selected content for distribution.

Run from any directory; paths are resolved relative to the repository root.

Use --noRN to skip utils/build_rns.py (same as declining regeneration when prompted).
'''

from __future__ import annotations

import argparse
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

STEP_TOTAL = 8


def progress(step: int, message: str) -> None:
    print("\n[Step {}/{}] {}".format(step, STEP_TOTAL, message), flush=True)


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
        print(
            "         Already on branch {!r}.".format(REQUIRED_BRANCH),
            flush=True,
        )
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

    print(
        "         Checking for uncommitted or staged changes…",
        flush=True,
    )
    if not working_tree_clean(root):
        print(
            "Your working tree has uncommitted or staged changes. "
            "Commit, stash, or discard them before switching branches, then run again."
        )
        sys.exit(1)

    print(
        "         Checking out {!r}…".format(REQUIRED_BRANCH),
        flush=True,
    )
    checkout = run_git(["checkout", REQUIRED_BRANCH], cwd=root)
    if checkout.returncode != 0:
        sys.exit(checkout.returncode)
    print("         Checkout complete.", flush=True)


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

    print(
        "\n         Release notes markdown summary (from {}): {}".format(
            BUILD_RNS_SCRIPT,
            len(pairs),
        ),
        flush=True,
    )
    if not pairs:
        print(
            "         (no “Building markdown for …” lines found in script output)",
            flush=True,
        )
        return
    for product, version in pairs:
        print("         - {} {}".format(product, version), flush=True)


def run_build_rns(root: Path) -> None:
    script = root / BUILD_RNS_SCRIPT.replace("/", os.sep)
    if not script.is_file():
        print("Missing script: {}".format(script), file=sys.stderr)
        sys.exit(1)

    print(
        "         (Output suppressed; summary follows when finished.)",
        flush=True,
    )
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
        print("         Removing {!s}…".format(public), flush=True)
        shutil.rmtree(public)
        print("         Removed.", flush=True)
    else:
        print("         No existing {!s} to remove.".format(public), flush=True)


def run_hugo_minify(root: Path) -> None:
    print(
        "         Hugo output will appear below (this may take a while)…",
        flush=True,
    )
    proc = subprocess.run(["hugo", "--minify"], cwd=str(root))
    if proc.returncode != 0:
        sys.exit(proc.returncode)


def product_image_prune_path(content_dir: str) -> str:
    '''Return images/ path to remove for the selected product bundle.'''
    if content_dir.startswith("cumulus-netq"):
        return "images/cumulus-linux"
    return "images/netq"


def prune_public(public: Path, content_dir: str) -> None:
    product_images = product_image_prune_path(content_dir)
    print(
        "         Stripping {!s}, {}, and other unused paths…".format(
            product_images,
            "{}/api".format(content_dir),
        ),
        flush=True,
    )
    cmds = [
        ["rm", "-rf", product_images],
        ["rm", "-rf", "images/old_doc_images"],
        ["rm", "-rf", "images/sonic"],
        ["rm", "-rf", "images/knowledge-base/"],
        ["rm", "-rf", "images/cumulus-vx/"],
        ["rm", "-rf", "{}/api".format(content_dir)],
        ["rm", "-rf", "images/guides"],
    ]
    for cmd in cmds:
        subprocess.run(cmd, cwd=str(public), check=False)
    print("         Prune finished.", flush=True)


def copy_icons_into_subdirs(public: Path) -> None:
    print(
        "         Running find + cp -r (warnings suppressed; may take a minute)…",
        flush=True,
    )
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
    print("         Icon copy finished.", flush=True)


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
    print(
        "         Adding {!s} items to {!s} (quiet zip; may take a minute)…".format(
            len(members),
            zip_filename,
        ),
        flush=True,
    )
    cmd = ["zip", "-q", "-r", zip_filename, *members]
    proc = subprocess.run(cmd, cwd=str(public))
    if proc.returncode != 0:
        sys.exit(proc.returncode)
    return archive


def print_ls_line_and_warnings(archive: Path, content_dir: str) -> None:
    print("\n         Archive:", flush=True)
    ls = subprocess.run(
        ["ls", "-lh", archive.name],
        cwd=str(archive.parent),
        capture_output=True,
        text=True,
    )
    if ls.returncode == 0 and ls.stdout:
        print(ls.stdout.rstrip(), flush=True)
    else:
        size = archive.stat().st_size
        print("{}  ({:,} bytes)".format(archive.name, size), flush=True)

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build offline HTML docs with Hugo and zip selected content.",
    )
    parser.add_argument(
        "--noRN",
        action="store_true",
        help="Skip {} (do not regenerate release notes).".format(BUILD_RNS_SCRIPT),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = repo_root()
    print(
        "\nOffline docs HTML zip — repository root: {!s}".format(root),
        flush=True,
    )
    if args.noRN:
        print(
            "Option --noRN: release notes script will be skipped.",
            flush=True,
        )
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

    print(
        "\nUsing content directory {!r} ({!s}).".format(content_dir, content_src),
        flush=True,
    )

    if args.noRN:
        skip_rn = True
    else:
        rn_choice = input(
            "\nRegenerate release notes with {!s}?\n"
            "  (Downloads JSON from CloudFront and rewrites RN markdown in content/.)\n"
            "[Y/n]: ".format(BUILD_RNS_SCRIPT)
        ).strip().lower()
        skip_rn = rn_choice in ("n", "no")

    progress(1, "Checking git branch (expect {!r})…".format(REQUIRED_BRANCH))
    ensure_generate_offlinedocs_branch(root)

    if skip_rn:
        progress(
            2,
            "Skipping release notes ({!s}); using existing RN markdown.".format(BUILD_RNS_SCRIPT),
        )
        print(
            "         {}".format(
                "Skipping because of --noRN."
                if args.noRN
                else "Skipping because you chose not to regenerate."
            ),
            flush=True,
        )
    else:
        progress(
            2,
            "Running release notes script {!s} before Hugo build…".format(BUILD_RNS_SCRIPT),
        )
        run_build_rns(root)

    progress(3, "Removing previous Hugo output directory public/…")
    remove_public(root)

    progress(4, "Building site with hugo --minify…")
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

    if content_dir.startswith("cumulus-netq"):
        prune_detail = "keeping images/netq; removing images/cumulus-linux"
    elif content_dir.startswith("cumulus-linux"):
        prune_detail = "keeping images/cumulus-linux; removing images/netq"
    else:
        prune_detail = "removing images/netq (default for non-NetQ bundles)"
    progress(
        5,
        "Pruning unused paths from public/ ({}, {}/api, …)…".format(
            prune_detail,
            content_dir,
        ),
    )
    prune_public(public, content_dir)

    progress(6, "Fixing up icons (copy into each subdirectory)…")
    copy_icons_into_subdirs(public)

    progress(7, "ZIP filename — archive will be created under public/")
    zip_prompt = input(
        "\nZIP filename (created under public/):\n"
        "  e.g. CL5.16.1-docs-html.zip, NetQ5.1.0-docs-html.zip, DSX-Air-docs-html.zip\n"
        "> "
    ).strip()
    zip_name = normalize_zip_filename(zip_prompt)

    progress(8, "Creating zip archive {!s}…".format(zip_name))
    archive = zip_docs(public, zip_name, content_dir)
    print_ls_line_and_warnings(archive, content_dir)
    print("\n[Done] All steps finished.", flush=True)


if __name__ == "__main__":
    main()
