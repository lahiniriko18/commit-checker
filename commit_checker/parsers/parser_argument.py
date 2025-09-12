import argparse


def argument_parser():
    parser = argparse.ArgumentParser(description="Outil de validation des commits")
    parser.add_argument(
        "--limit", type=int, help="Nombre de commits à vérifier"
    )
    parser.add_argument("--path", default=".", help="Chemin du dépôt Git")
    parser.add_argument("--output", help="Exporter un rapport (JSON)")

    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        default=False,
        help="Inverse l'ordre des commits",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="Afficher la liste des types de commits",
    )
    parser.add_argument(
        "--last",
        action="store_true",
        help="Afficher le dernier commit",
    )
    parser.add_argument(
        "--first",
        action="store_true",
        help="Afficher le premier commit",
    )

    return parser.parse_args()
