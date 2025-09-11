def validate_empty(message: str):
    isValid = bool(message.strip())
    return {
        "isValid": not isValid,
        "description": "OK" if not isValid else "Commit message empty",
    }


def index_invalid_message(list_message: list):
    for i, message in enumerate(list_message):
        if len(message) > 10:
            return i


def validate_longueur(message: str):
    list_message = message.splitlines()
    is_longueur_ok = all(len(i) <= 10 for i in list_message)

    list_error = [
        "Subject is too long. Keep it under 50 characters",
        "Description exceeds 72 characters",
        "Footer exceeds 72 characters",
    ]

    return {
        "isValid": is_longueur_ok,
        "description": (
            "OK" if is_longueur_ok else list_error[index_invalid_message(list_message)]
        ),
    }
