# GIT
## Git stash

**Description**
Permet de sauvegarder temporairement vos modifications en cours (non indexées ou indexées) sans les committer.

**Commandes**

```
git stash
```

Sauvegarde les modifications actuelles dans une pile sans les committer.

```
git stash pop
```

Applique et supprime la dernière sauvegarde de la pile.

```
git stash drop
```

Supprime la dernière sauvegarde de la pile sans l'appliquer.

```
git stash apply
```

Applique une sauvegarde sans la supprimer de la pile.

```
git stash clear
```

Supprime toutes les sauvegardes de la pile.

## Git log

**Description**
`git log` permet de visualiser l'historique des commits dans un dépôt.

**Commandes**

```
git log --oneline
```

Affiche un résumé des commits sous forme de liste concise avec un identifiant abrégé et un message.

```
git log -p
```

Affiche l'historique des commits avec les différences (`diffs`) des fichiers modifiés.

```
git log --stat
```

Affiche l'historique des commits avec des statistiques sur les fichiers modifiés (ajouts, suppressions).

```
git shortlog
```

Affiche l'historique des commits par auteur, avec un résumé des contributions.

```
git log --graph
```

Affiche l'historique des commits sous forme de graphique pour visualiser les branches.

```
git log --oneline --graph
```

Affiche l'historique des commits sous forme de graphique simplifié avec une ligne par commit.

```
git log --graph --pretty="%C(yellow) Hash: %h %C(blue)Date: %ad %C(red) Message: %s " --date=human
```

Affiche un graphique des commits avec des informations formatées sur le hash, la date et le message.

```
git log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit
```

Affiche un graphique avec un format personnalisé, y compris le nom de l'auteur et l'heure du commit.

```
git config --global alias.lg 'log --color --graph --pretty="%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit'
```

Crée un alias `lg` pour afficher les commits dans un format graphique personnalisé.

```
git log -- testfile-02 branchfile-01
```

Affiche l'historique des commits pour des fichiers spécifiques dans une branche donnée.

```
git log master..second-branch
```

Affiche l'historique des commits pour comparer deux branches (ici `master` et `second-branch`).

```
git log --merges (ou --no-merges)
```

Affiche uniquement les commits de type merge ou les exclut selon l'option choisie.

```
git log --before 2021-4-30 --after=2021-4-1
```

Affiche les commits dans une plage de dates spécifique.

```
git log -3
```

Affiche les 3 derniers commits.

```
git log -1 --grep="JIRA"
```

Recherche les commits contenant un mot-clé dans leur message, ici "JIRA".

## Git branch 

Afficher les branches distantes

```
git branch -r
```

## Erreur SSL à cause du CA ROOT

### Etapes pour Linux

**Description**
Si une erreur SSL se produit, il peut être nécessaire de mettre à jour le certificat racine (CA Root) pour résoudre le problème.

Télécharger le CA ROOT.

Copier le fichier ici :  
`/usr/local/share/ca-certificates/ca.crt`

Lancer la commande :

```
sudo update-ca-certificates
```

### Étapes pour Windows

1. Ouvrir le gestionnaire des certificats
2. Appuyez sur Win + R et tapez :
   ```
   certmgr.msc
   ```
3. Importer le certificat root
4. Naviguez vers Autorités de certification racines de confiance > Certificats.
5. Faites un clic droit et sélectionnez Toutes les tâches > Importer.
6. Suivez l’assistant et sélectionnez votre certificat root (par exemple, root-ca.crt).
7. Redémarrer les applications concernées

Une fois le certificat ajouté, redémarrez les applications ou services (GitLab Runner, Ansible, etc.).

## Git config

### Option git config

- `--system` - Table applicable à l'ensemble de la machine.
- `--global` - Configuration pour l'utilisateur actuel.
- `--local` (par défaut) - Configuration pour le dépôt courant.

### Configuration de base

```
git config --global user.email johndoe@myemail.com
```

```
git config --global user.name "John Doe"
```

```
git config --global color.status auto
```

```
git config --global color.branch auto
```

```
git config --global color.interactive auto
```

```
git config --global color.diff auto
```

```
git config --global alias.adog "log --all --decorate --oneline --graph"
```

```
git config --global core.editor vim
```

Le fichier de configuration est `~/.gitconfig`.

### Afficher les configs

```
git config --list
```

```
git config --list --global
```

```
git config user.name
```

## Contenu du dossier .git

- **hooks** : Contient tous les hooks personnalisés. Ce sont des scripts exécutés avant ou après certaines actions (commit, push, etc.).
- **branches** : Ce dossier est obsolète.
- **HEAD** : Pointeur vers la branche actuelle et son dernier commit.
- **config** : Fichier de configuration du dépôt.
- **info** : Contient les fichiers en attente d'ajout avec `git add`.
- **refs** : Contient l'état actuel des branches et des tags.
- **objects** : Contient les objets Git tels que les commits, arbres et blobs.
- **logs** : Contient les logs des actions effectuées sur le dépôt.
- **description** : Description du dépôt.

## Git checkout

**Annuler changement sur un fichier non indexé (not yet added)**

```
git checkout testfile-01
```

## Git rm

**Annuler modification indexée (added**)

Supprime un fichier de la staging area sans le supprimer du disque.

```
git rm --cached myfile
```

Supprime un fichier à la fois de Git et du disque, même s'il est modifié.

```
git rm -f myfile
```

## Git reset et revert

### Reset

#### Soft

Revenir 1 commit en arrière sans supprimer les modifications au niveau du fichier.

```
git reset --soft HEAD~1
```

#### Hard

Revenir 1 commit en arrière et supprimer les modifications au niveau du fichier.

```
git reset --hard HEAD~1
```

### Revert

Crée un nouveau commit qui annule un ancien commit. Cela permet de rester linéaire et de ne pas avoir un HEAD en retard par rapport au HEAD distant.

**Important :** revert annule les modifications apportées par le commit ciblé par le revert.

```
git revert --no-edit HEAD~1
```

## Git diff

```
git diff
```

```
git diff HEAD~1
```

```
git diff HEAD~1 testfile-01
```

```
git diff --staged
```

## Git show

Affiche le résultat de `git log` + `git diff` d'un commit. Utiliser `git log -p` pour tous les commits.

```
git show
```

```
git show HEAD~1
```

## Git tag

### Supprimer un tag

```
git tag -d v1.0
```

### Basculer sur un tag

```
git checkout v1.0
```

### Créer un tag sur le commit courant

```
git tag -a v2.0 -m "version 2.0. A lot of new features"
```

### Afficher contenu d'un commit par son tag

```
git show v1.0
```

## Git fetch

Télécharge les derniers commits distants sans les intégrer à la branche locale. Ces merges sont dans une branche différente (ex: `origin/main`, local c'est `main`).

## Git rebase

Réécrit les commits d'une branche dans un historique linéaire sur la branche master. Cela permet d'avoir un historique linéaire et des identifiants de commit différents.

Pratique : faire un rebase et ensuite merger pour changer la pointe du master sur le dernier commit.

## Git remote

### Ajouter un remote repo

```
git remote add origin $URI
```

### Afficher les repos distants

```
git remote -v
```

## Git fork

Créer une copie d'un projet, modifier et créer ensuite une PR (pull request) pour demander au projet forké d'accepter et de merger les modifications. Utilisé surtout sur les projets sur lesquels on n'a pas les droits de pull.

## Git merge

### Fast-forward merge

Le master n'a aucun nouveau commit comparé à la branche à merger.

### No fast-forward merge

Le master a de nouveaux commits comparé à la branche à merger. Un commit de merge est créé.
