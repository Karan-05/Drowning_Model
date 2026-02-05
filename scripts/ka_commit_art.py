#!/usr/bin/env python3
"""Generate a KA pattern on your GitHub contribution graph."""

import argparse
import datetime as dt
import os
import subprocess
import textwrap

KA_PATTERN = [
    "10010001110",
    "10100010001",
    "11000010001",
    "10100011111",
    "10010010001",
    "10001010001",
    "10000010001",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a KA monogram on your GitHub contribution graph by "
            "backdating empty commits."
        )
    )
    parser.add_argument(
        "--repo",
        required=True,
        help="Path to the git repository whose graph you want to paint.",
    )
    parser.add_argument(
        "--start-date",
        required=True,
        help=(
            "Date (YYYY-MM-DD) of the Sunday that represents the top-left "
            "cell you want to use."
        ),
    )
    parser.add_argument(
        "--message",
        default="KA contribution art",
        help="Commit message prefix to use for generated commits.",
    )
    parser.add_argument(
        "--intensity",
        type=int,
        default=1,
        help="Number of commits per lit cell (1-10).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the commits that would be created without running git.",
    )
    return parser.parse_args()


def validate_start_date(date_text: str) -> dt.datetime:
    try:
        start_date = dt.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError as err:  # pragma: no cover - tiny helper
        raise SystemExit(f"Invalid --start-date: {err}")
    if start_date.weekday() != 6:
        warning = textwrap.dedent(
            """
            The start date is not a Sunday. GitHub contribution grids use
            Sunday as the first row, so double-check the alignment before you
            push the generated commits.
            """
        ).strip()
        print(f"[warning] {warning}")
    return start_date


def ensure_repo(path: str) -> str:
    repo_path = os.path.abspath(path)
    if not os.path.isdir(os.path.join(repo_path, ".git")):
        raise SystemExit(f"{repo_path} is not a git repository")
    return repo_path


def create_commit(repo: str, date: dt.datetime, message: str, dry_run: bool) -> None:
    iso_stamp = date.strftime("%Y-%m-%dT12:00:00")
    if dry_run:
        print(f"[dry-run] {iso_stamp} :: {message}")
        return

    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = iso_stamp
    env["GIT_COMMITTER_DATE"] = iso_stamp
    subprocess.run(
        ["git", "-C", repo, "commit", "--allow-empty", "-m", message],
        check=True,
        env=env,
    )


def main() -> None:
    args = parse_args()
    repo = ensure_repo(args.repo)
    start = validate_start_date(args.start_date)
    commits_per_cell = max(1, min(args.intensity, 10))

    rows = len(KA_PATTERN)
    cols = len(KA_PATTERN[0])

    for col in range(cols):
        for row in range(rows):
            if KA_PATTERN[row][col] != "1":
                continue
            target_day = start + dt.timedelta(weeks=col, days=row)
            for n in range(commits_per_cell):
                note = f"{args.message} {target_day.date()} #{n + 1}"
                create_commit(repo, target_day, note, args.dry_run)


if __name__ == "__main__":
    main()
