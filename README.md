# 📝 Commit Checker

Un outil en ligne de commande (CLI) développé en **Python** permettant de vérifier la qualité des messages de commit Git en fonction de règles définies (longueur, non-vide, etc.) et des normes de convention de commit.

---

## 🚀 Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/lahiniriko18/commit-checker.git
cd commit-checker
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate   # sous Linux / MacOS
venv\Scripts\activate      # sous Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## ▶️ Utilisation

### 1. Verifier tous le commits :
```bash
python main.py --all
```

### 2. Verifier les 5 derniers commits :
```bash
python main.py
```

### 3. Inverser la vérification :
```bash
python main.py --reverse
```
#### Options :
-r, --reverse    Inverser la vérification (du dernier au plus récent ou vice versa)

### 4. Vérifier les commits avec une limite

```bash
python main.py --limit <limite>
```
#### Options :
-lm, --limit    Limiter les commits à vérifier (ex: --limit 5)
Par défaut : 5 (si non spécifié)


### 5. Liste des normes du commit :
```bash
python main.py --list
```
#### Options:
-ls, --list       Lister les types des commits valides

### 6. Exporter une rapport JSON ou TXT :
```bash
python main.py --output <nom_fichier> [--format json|txt]
```
### Exemple
```bash
python main.py --output report --format json
```
#### Options:
--output, -o     Specifier le nom du fichier (ex: report.json ou report.txt)
--format         Choisir le format du fichier à exporter: "json" ou "txt"
Par défaut:      json (si non specifié)

### 7. Vérifier le premier commit seulement :
```bash
python main.py --first
```

### 8. Vérifier le dernier commit seulement :
```bash
python main.py --last
```

### 9. Vérifier le commit aujourd'hui:
```bash
python main.py --now
```
Ajouter --all pour vérifier tous les commits aujourd'hui sinon il vérifie les 5 derniers commits aujourd'hui

### 10. Vérfier les commits dans une répot spécifique :
```bash
python main.py --path <chemin\vers\repos>
```
### Exemple:
```bash
python main.py --path D:\LNJ\projet
```
#### Options:
-p, --path     Vérifier les commits dans une autre répos  

### 11. Vérifier les commits dans une branche :
```bash
python main.py --branch
```
#### Options:
-b, --branch     Specifier le branche cible (ex: auth)
Par défaut:      HEAD (si non specifié)

### 12. Consulter l'aide:
```bash
python main.py --help
```
#### Options:
-b, --help     Consulter des aides pour les différentes commandes

### Exemple de sortie :
```
commit: e796736
message: feat: add type format repport
report format txt or json by using --format
not_empty:  OK
length:  OK
content:  OK
note: 3/3 (Excellent)
```

---

## 📂 Structure du projet

```
└── 📁commit_checker
    └── 📁constants
        ├── constants.py
    └── 📁filters
        ├── commit_filter.py
    └── 📁parsers
        ├── git_parser.py
        ├── parser_argument.py
    └── 📁reports
        ├── commit_list.py
        ├── reports.py
        ├── utils.py
    └── 📁rules
        ├── rules.py
    └── 📁validations
        ├── validation_reports.py
        ├── validation_rules.py
    ├── cli.py
└── 📁venv 
│── requirements.txt
│── README.md
```

---

## 📏 Norme de Commit (Git Standard)

Tous les commits doivent respecter le format suivant :

```
<type>(<portée>): <sujet>
<description>
<footer>
```

### 🔹 Types autorisés :
- **build**: Système de build (ex: gulp, webpack, npm)
- **ci**: Intégration continue (ex: Travis, Circle, BrowserStack, SauceLabs)
- **docs**: Documentation
- **feat**: Ajout d’une fonctionnalité
- **fix**: Correction de bogue
- **perf**: Amélioration des performances
- **refactor**: Changement du code sans modification du comportement
- **style**: Changement de style de code (sans changer la logique)
- **test**: Modification ou ajout de tests

### 🔹 Portée *(optionnelle)* :
Divise le projet en module/partie. Exemple :  
```
feat(auth): add login
```

### 🔹 Sujet :
- Verbe à l’impératif  
- Pas de majuscule  
- Pas de point final  

Exemple :  
```
fix(api): correct error handling
```

### 🔹 Description :
- Explique **pourquoi** le changement, pas son contenu.

### 🔹 Footer :
Utilisé pour lier des issues ou PR.  
Exemple :  
```
closes #42
```