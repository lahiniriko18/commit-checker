##### OUTIL DE VALIDATION DES COMMITS

# Installation

1. Cloner le dépôt
   git clone https://github.com/lahiniriko18/commit-checker.git
   cd commit-checker

2. Créer l'environnement virtuel
   python -m venv venv

3. Activer l'environnement

   > > > venv\Scripts\activate //windows
   > > > source venv/bin/activate //linux

4. Installer les dépendances:
   pip install -r requirements.txt

# Utilisation

1. Verifier les 5 derniers commits
   python main.py

2. Vérifier tous les commits
   python main.py --all

3. Inverser la liste des commits
   python main.py -r
   python main.py --reverse

4. Verifier les commits avec une limite
   python main.py --limit <limite>
   Options:
   -lm, --limit       Limiter les commits à vérifier (ex: --limit 5)
   Par défaut: 5 (si non specifié)


5. Liste des normes du commit
   python main.py --list
   python main.py -ls
   Options:
   -ls, --list       Lister les types des commits valides

6. Exporter une rapport JSON ou TXT
   python main.py --output <nom_fichier> [--format json|txt]
   Options:
   --output, -o     Specifier le nom du fichier (ex: report.json ou report.txt)
   --format Choisir le format du fichier à exporter: "json" ou "txt"
   Par défaut:      json (si non specifié)

7. Vérifier le premier commit seulement
   python main.py --first

8. Vérifier le dernier commit seulement
   python main.py --last

9. Vérifier le commit aujourd'hui
   python main.py --now
   Options:
   Ajouter --all pour récuperer tous les commits aujourd'hui

10. Vérifier les commits dans une branche
   python main.py --branch
   python main.py -b
   Options:
   -b, --branch     Specifier le branche cible (ex: auth)
   Par défaut:      HEAD (si non specifié)

11. Consulter l'aide
   python main.py -h
