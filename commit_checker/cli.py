import sys

from .parsers.git_parser import get_commits
from .parsers.parser_argument import argument_parser
from .reports.commit_list import list_commit
from .reports.reports import generate_report
from .rules.rules import check_commit


def commit_cli():
    args = argument_parser()
    if args.list:
        list_commit()
        sys.exit(0)

    commits = get_commits(
        args.path,
        limit=args.limit,
        reverse=args.reverse,
        first=args.first,
        last=args.last,
    )
    results = [check_commit(commit) for commit in commits]
    generate_report(results, args.output)
