import sys

from colorama import Fore, Style
from git import Repo


def get_commits(path=".", branch="HEAD", limit=None, reverse=False):
    try:
        repo = Repo(path)
        allRepos = list(repo.iter_commits(branch))
        allRepos = allRepos[::-1] if reverse else allRepos
        if limit:
            return allRepos[:limit]
        return allRepos
    except Exception as e:
        print(f"{Fore.RED}Erreur: {e}{Style.RESET_ALL}")
        sys.exit(1)
