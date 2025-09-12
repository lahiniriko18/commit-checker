import argparse
from ..constants.constants import DEFAULT_COMMIT_LIMIT


def argument_parser():
    parser = argparse.ArgumentParser(description="Commit Validation Tool")
    parser.add_argument(
        "-lm","--limit",
        type=int,
        default=DEFAULT_COMMIT_LIMIT,
        help="Number of commits to check",
    )
    parser.add_argument(
        "-p", "--path", type=str, default=".", help="Path to the Git repository"
    )
    parser.add_argument("-o", "--output", type=str, help="Export a report (JSON)")
    parser.add_argument("-auth", "--author", type=str, help="User commits")
    parser.add_argument(
        "-b", "--branch", type=str, default="HEAD", help="Commit branch"
    )
    parser.add_argument(
        "-f", "--format", type=str, default="json", help="Commit branch"
    )
    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        default=False,
        help="Reverse the order of commits",
    )
    parser.add_argument(
        "-ls",
        "--list",
        action="store_true",
        help="Show the list of commit types",
    )
    parser.add_argument(
        "--last",
        action="store_true",
        help="Check the last commit",
    )
    parser.add_argument(
        "--first",
        action="store_true",
        help="Check the first commit",
    )
    parser.add_argument(
        "--now",
        action="store_true",
        help="Check only commits made today",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Check all commits",
    )

    return parser.parse_args()
