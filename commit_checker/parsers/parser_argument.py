import argparse


def argument_parser():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--limit", type=int, default=5, help="Nombre de commits à vérifier"
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

    return parser.parse_args()
