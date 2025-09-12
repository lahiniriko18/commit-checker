##### OUTIL DE VALIDATION DES COMMITS #####

# Installation

1. Cloner le dépôt
git clone https://github.com/lahiniriko18/commit-checker.git
cd commit-checker

2. Créer l'environnement virtuel
python -m venv venv

3. Activer l'environnement
>>> venv\Scripts\activate //windows
>>> source venv/bin/activate //linux

4. Installer les dépendances:
pip install -r requirements.txt


# Utilisation

1. Verifier tous le commits
python main.py

2. Inverser la lisate
python main.py --reverse || python main.py -r

3. Verifier les commits avec une limite
python main.py --limit 5

4. Liste des normes du commit
python main.py -l || python main.py --list

5. Vérifier le dernier commit seulement
python main.py --last

6. Vérifier le premier commit seulement
python main.py --first

7. Consulter l'aide
python main.py -h