from colorama import Fore

DEFAULT_COMMIT_LIMIT = 5

DICT_COMMIT = {
    "build": "Système de build",
    "ci": "Intégration continue",
    "docs": "Documentation",
    "feat": "Ajout d’une fonctionnalité",
    "fix": "Correction de bogue",
    "perf": "Amélioration des performances",
    "refactor": "Changement du code qui ne change rien au fonctionnement",
    "style": "Changement du style de code (Sans changer la logique)",
    "test": "Modification des tests",
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
