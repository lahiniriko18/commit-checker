import argparse


def argument_parser():
    parser = argparse.ArgumentParser(description="Commit Validation Tool")
    parser.add_argument("--limit", type=int, help="Number of commits to check")
    parser.add_argument("--path", default=".", help="Path to the Git repository")
    parser.add_argument(
        "--output", type=str, help="Export a report (JSON)"
    )

    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        default=False,
        help="Reverse the order of commits",
    )
    parser.add_argument(
        "-l",
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

    return parser.parse_args()
