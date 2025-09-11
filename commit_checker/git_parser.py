from git import Repo


def get_commits(path=".", branch="HEAD", limit=None):
    repo = Repo(path)
    return list(repo.iter_commits("HEAD", max_count=limit))
