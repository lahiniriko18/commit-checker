import sys

from colorama import Fore, Style
from git import Repo

repo = Repo(".")


def check_commit_message(message: str):
    list_message = message.splitlines()
    # if len(list_message)
    rules = {
        "non_vide": bool(message.strip()),
        "longueur_ok": len(message.splitlines()[0]) <= 72,
    }
    score = sum(rules.values())
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
        print(f"Score: {result['score']}/2")

        for rule, isOk in result["rules"].items():
            color = Fore.GREEN if isOk else Fore.RED
            print(f"{rule}: {color} {"OK" if isOk else "NOT OK"}{Style.RESET_ALL}")

        total_score += result["score"]

    print(
        f"{Fore.YELLOW} \nScore global: {total_score}/{len(commits)*2} {Style.RESET_ALL}"
    )


if __name__ == "__main__":
    main()
