import sys

from colorama import Fore, Style
from git import Repo
from commit_checker.validation import (
    validate_empty,
    validate_longueur,
    validate_subject,
)


def check_commit_message(message: str):

    rules = {
        "non_vide": validate_empty(message),
        "longueur_ok": validate_longueur(message),
        "sujet_ok": validate_subject(message),
    }

    score = sum(rule["isValid"] for rule in rules.values())
    return {"message": message, "rules": rules, "score": score}


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."
    try:
        repo = Repo(path)
        commits = list(repo.iter_commits("HEAD", max_count=3))
    except Exception as e:
        print(f"{Fore.RED}Erreur: {e}{Style.RESET_ALL}")
        sys.exit(1)

    total_score = 0
    for commit in commits:
        result = check_commit_message(commit.message)
        print(f"{Fore.CYAN}Commit: {commit.hexsha[:7]}{Style.RESET_ALL}")
        print(f"Message: {result.get('message', commit.message).strip()}")
        print(f"Score: {result['score']}/3")

        for item, rule in result["rules"].items():
            color = Fore.GREEN if rule["isValid"] else Fore.RED
            print(f"{item}: {color} {rule["description"]}{Style.RESET_ALL}")

        total_score += result["score"]

    print(
        f"{Fore.YELLOW} \nScore global: {total_score}/{len(commits)*3} {Style.RESET_ALL}"
    )
