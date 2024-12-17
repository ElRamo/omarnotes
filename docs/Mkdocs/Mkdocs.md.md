#### **1. Installation des outils nécessaires**

Assure-toi d'avoir **Python** et **MkDocs** installés :
```
# Installer MkDocs
pip install mkdocs

# (Optionnel) Installer le thème Material pour MkDocs
pip install mkdocs-material
```

#### **2. Créer un projet MkDocs**

Dans le terminal, exécute :
```
mkdocs new mon-site
```
Cela crée la structure suivante :
```
mon-site/
│── mkdocs.yml       # Fichier de configuration
│── docs/            # Contient les fichiers Markdown
    └── index.md     # Page d'accueil

```
#### **3. Ajouter tes notes Obsidian**

- Copie tous tes fichiers **`.md`** dans le dossier `docs`.
- Structure ton contenu dans des sous-dossiers si nécessaire.  
```
docs/
│── index.md
│── Docker/
│   └── Docker.md
│── Jenkins/
    └── Jenkins.md
 
```
#### **4. Configurer `mkdocs.yml`**

Ouvre **`mkdocs.yml`** et configure la navigation et le thème :
```
site_name: Mes Notes
nav:
  - Accueil: index.md
  - Docker: Docker/Docker.md
  - Jenkins: Jenkins/Jenkins.md
theme:
  name: material
  palette:
    - scheme: default
      primary: blue
      accent: blue
      toggle:
        icon: material/weather-sunny
        name: Basculer en mode sombre
    - scheme: slate
      primary: blue
      accent: blue
      toggle:
        icon: material/weather-night
        name: Basculer en mode clair
```
#### **5. Tester localement le site**

Lance la commande suivante pour voir ton site en local :
```
mkdocs serve
```
Accède à `http://127.0.0.1:8000` dans ton navigateur.
#### **6. Initialiser le dépôt GitHub**

Si ton projet n'est pas encore lié à un dépôt GitHub, initialise-le :
```
git init
git add .
git commit -m "Initialisation du projet MkDocs"
git remote add origin https://github.com/ton-utilisateur/ton-depot.git
git push -u origin master
```
#### 7.**Publier sur GitHub Pages**
Utilise la commande suivante pour déployer ton site :
`mkdocs gh-deploy`
Cela :

1. Génère le site statique.
2. Publie le site sur la branche **`gh-pages`** de ton dépôt GitHub.
#### **8. Activer GitHub Pages**

1. Va dans ton dépôt GitHub → **Settings** → **Pages**.
2. Choisis la branche **`gh-pages`** comme source.
3. Ton site sera accessible à :
```
https://ton-utilisateur.github.io/ton-depot/
```
