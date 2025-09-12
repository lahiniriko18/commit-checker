import sys
from datetime import datetime

from colorama import Fore, Style
from git import Repo


def filter_commit(repo: Repo, filters: dict):
    kwargs = {}
    if filters["author"]:
        kwargs["author"] = filters["author"]
    if filters["limit"]:
        kwargs["max_count"] = (
            None
            if filters["reverse"]
            or filters["first"]
            or filters["last"]
            or filters["all"]
            else filters["limit"]
        )
    if filters["now"]:
        today = datetime.now().date()
        kwargs["since"] = today.strftime("%Y-%m-%d 00:00:00")
        kwargs["until"] = today.strftime("%Y-%m-%d 23:59:59")
        
    if filters["branch"] not in repo.branches and filters["branch"] != "HEAD":
        print(
            f"{Fore.RED}Error: The branch {filters["branch"]} does not exist.{Style.RESET_ALL}"
        )
        sys.exit(1)
    else:
        kwargs["rev"] = filters["branch"]

    commits = list(repo.iter_commits(**kwargs))
    if filters["reverse"]:
        commits = commits[::-1]
    if filters["all"]:
        return commits
    if filters["first"]:
        return [commits[-1]] if commits else []
    if filters["last"]:
        return [commits[0]] if commits else []
    if filters["limit"]:
        return commits[: filters["limit"]]
    return commits
