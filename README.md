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

### Lancer l’outil en CLI :
```bash
python -m commit_checker.cli
```

### Vérifier un message de commit spécifique :
```bash
python -m commit_checker.cli "feat(auth): add login feature"
```

### Exemple de sortie :
```
✔ Message non vide
✔ Longueur correcte
✅ Commit valide !
```

---

## 📂 Structure du projet

```
commit-checker/
│── commit_checker/
│   │── __init__.py
│   │── cli.py           # Point d’entrée CLI
│   │── git_parser.py    # Gestion des commits Git
│   │── validation.py    # Règles de validation
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

---

## 🤝 Contribution

1. Forker le projet  
2. Créer une branche (`git checkout -b feature/ma-feature`)  
3. Committer avec un message respectant la norme  
4. Pousser la branche (`git push origin feature/ma-feature`)  
5. Créer une Pull Request  

---

## 📄 Licence

Ce projet est sous licence **MIT**.
