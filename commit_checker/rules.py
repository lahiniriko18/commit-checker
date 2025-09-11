from .validation import validate_empty, validate_longueur, validate_subject
from git.objects.commit import Commit


def check_commit(commit: Commit):

    rules = {
        "non_vide": validate_empty(commit.message),
        "longueur_ok": validate_longueur(commit.message),
        "sujet_ok": validate_subject(commit.message),
    }

    score = sum(rule["isValid"] for rule in rules.values())
    return {
        "commit": commit.hexsha[:7],
        "message": commit.message,
        "rules": rules,
        "score": score,
    }
