import sys
from git import Repo

repo=Repo(".")
commits=list(repo.iter_commits('HEAD',max_count=3))

for commit in commits:
    print(f"Commit: {commit.hexsha[:7]}")
    print(f"Auteur: {commit.author.name}")
    print(f"Message: {commit.message.strip()}\n")