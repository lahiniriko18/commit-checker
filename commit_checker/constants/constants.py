from colorama import Fore

DEFAULT_COMMIT_LIMIT = 5

DICT_COMMIT = {
    "build": "Build system changes",
    "ci": "Continuous integration changes",
    "docs": "Documentation changes",
    "feat": "Adding a new feature",
    "fix": "Bug fixes",
    "perf": "Performance improvements",
    "refactor": "Code changes that do not affect functionality",
    "style": "Code style changes (no logic changes)",
    "test": "Test code modifications"
}


COLOR_LEVEL = {
    "excellent": Fore.GREEN,
    "very good": Fore.LIGHTGREEN_EX,
    "good": Fore.CYAN,
    "average": Fore.LIGHTYELLOW_EX,
    "below average": Fore.YELLOW,
    "poor": Fore.LIGHTRED_EX,
    "very poor": Fore.RED,
}
