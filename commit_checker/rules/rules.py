from git.objects.commit import Commit

from ..validations.validation_rules import validate_empty, validate_length, validate_subject


def check_commit(commit: Commit):
    rules = {
        "not_empty": validate_empty(commit.message),
        "length": validate_length(commit.message),
        "content": validate_subject(commit.message),
    }

    note = sum(rule["isValid"] for rule in rules.values())
    return {
        "commit": commit.hexsha[:7],
        "message": commit.message,
        "date": commit.committed_datetime.astimezone().strftime("%Y-%m-%d %H:%M:%S"),
        "rules": rules,
        "note": note,
    }
