import re


def validate_empty(message: str):
    isValid = bool(message.strip())
    return {
        "isValid": isValid,
        "description": "OK" if isValid else "Commit message empty",
    }


def validate_longueur(message: str):
    list_message = message.splitlines()
    subject = list_message[0] if len(list_message) > 0 else ""
    description = list_message[1] if len(list_message) > 1 else ""
    footer = list_message[2] if len(list_message) > 2 else ""

    if len(subject) > 50:
        return {
            "isValid": False,
            "description": "Subject too long (max 50 characters)",
        }
    if len(description) > 72:
        return {
            "isValid": False,
            "description": "Description too long (max 72 characters)",
        }
    if len(footer) > 72:
        return {
            "isValid": False,
            "description": "Footer too long (max 72 characters)",
        }
    return {"isValid": True, "description": "OK"}


def validate_subject(message: str):
    pattern = re.compile(
        r"^(build|ci|docs|feat|fix|perf|refactor|style|test)(\([a-zA-Z0-9_-]+\))?: [a-z][^A-Z.]*$"
    )
    isValid = bool(
        pattern.match(
            message.splitlines()[0].strip(),
        )
    )
    return {
        "isValid": isValid,
        "description": (
            "OK" if isValid else "Subject does not follow the conventional format"
        ),
    }
