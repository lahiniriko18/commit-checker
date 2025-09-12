import sys

from colorama import Fore, Style
from git import Repo
from ..filters.commit_filter import filter_commit


def get_commits(
    path=".",
    branch="HEAD",
    limit=None,
    reverse=False,
    first=False,
    last=False,
    author=None,
    all=False,
    now=False,
):
    try:
        repo = Repo(path)
        filters = {
            "branch": branch,
            "limit": limit,
            "reverse": reverse,
            "first": first,
            "last": last,
            "author": author,
            "all": all,
            "now": now,
        }
        commits = filter_commit(repo, filters)
        return commits
    except Exception as e:
        print(f"{Fore.RED}Erreur: {e}{Style.RESET_ALL}")
        sys.exit(1)
