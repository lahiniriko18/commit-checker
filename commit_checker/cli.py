import argparse
import sys

from .git_parser import get_commits
from .report import generate_report
from .rules import check_commit


def commit_cli():
    parser = argparse.ArgumentParser(description="Outil de validation des commits")
    parser.add_argument("--last", type=int, default=5, help="Nombre de commits à vérifier")
    parser.add_argument("--path", default=".", help="Chemin du dépôt Git")
    parser.add_argument("--output", help="Exporter un rapport (JSON)")
    
    args = parser.parse_args()
    
    commits=get_commits(args.path,limit=args.last)
    results = [check_commit(commit) for commit in commits]
    generate_report(results)
