# Git - Commandes et Notes

### permet de sauvegarder temporairement vos modifications en cours (non indexées ou indexées) sans les committer

Description de la commande : permet de sauvegarder temporairement vos modifications en cours (non indexées ou indexées) sans les committer

### git stash

Description de la commande : git stash

### Appliquer et supprimer de la pile

Description de la commande : Appliquer et supprimer de la pile

### git stash pop

Description de la commande : git stash pop

### Supprimer le dernier

Description de la commande : Supprimer le dernier

### git stash drop

Description de la commande : git stash drop

### Appliquer sans supprimer

Description de la commande : Appliquer sans supprimer

### git stash apply

Description de la commande : git stash apply

### Supprimer tous

Description de la commande : Supprimer tous

### git stash clear

Description de la commande : git stash clear

### nan

Description de la commande : nan

### Afficher commits (git log)

Description de la commande : Afficher commits (git log)

### résumé de git log

Description de la commande : résumé de git log

### git log --oneline

Description de la commande : git log --oneline

### git show sur tous les commit : git log + git diff

Description de la commande : git show sur tous les commit : git log + git diff

### git log -p 

Description de la commande : git log -p 

### voir le nombre de modifications d'un commit

Description de la commande : voir le nombre de modifications d'un commit

### git log --stat 

Description de la commande : git log --stat 

### voir commit par autheur

Description de la commande : voir commit par autheur

### git shortlog

Description de la commande : git shortlog

### mode graphe

Description de la commande : mode graphe

### git log --graph 

Description de la commande : git log --graph 

### mode graphe résumé

Description de la commande : mode graphe résumé

### git log --oneline --graph 

Description de la commande : git log --oneline --graph 

### pretty

Description de la commande : pretty

### git log --graph --pretty="%C(yellow) Hash: %h %C(blue)Date: %ad %C(red) Message: %s " --date=human 

Description de la commande : git log --graph --pretty="%C(yellow) Hash: %h %C(blue)Date: %ad %C(red) Message: %s " --date=human 

### pretty avec le nom de l'autheur du commit

Description de la commande : pretty avec le nom de l'autheur du commit

### git log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit 

Description de la commande : git log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit 

### alias de la cmd précédente

Description de la commande : alias de la cmd précédente

### git config --global alias.lg 'log --color --graph --pretty="%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit' 

Description de la commande : git config --global alias.lg 'log --color --graph --pretty="%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit' 

### Trouver fichier dans branche

Description de la commande : Trouver fichier dans branche

### git log -- testfile-02 branchfile-01

Description de la commande : git log -- testfile-02 branchfile-01

### comparer deux branches

Description de la commande : comparer deux branches

### git log master..second-branch

Description de la commande : git log master..second-branch

### Trouver commit avec merges

Description de la commande : Trouver commit avec merges

### git log --merges (ou --no-merges)

Description de la commande : git log --merges (ou --no-merges)

### Recherche par date

Description de la commande : Recherche par date

### git log --before 2021-4-30 --after=2021-4-1

Description de la commande : git log --before 2021-4-30 --after=2021-4-1

### Afficher 3 derniers commits

Description de la commande : Afficher 3 derniers commits

### git log -3

Description de la commande : git log -3

### grep

Description de la commande : grep

### git log -1 --grep="JIRA"

Description de la commande : git log -1 --grep="JIRA"

### nan

Description de la commande : nan

### Afficher les branches distantes

Description de la commande : Afficher les branches distantes

### git branch -r

Description de la commande : git branch -r

### nan

Description de la commande : nan

### Ajouter le certificat CA Orange à Git

Description de la commande : Ajouter le certificat CA Orange à Git

### Télécharger le CA depuis : 

Description de la commande : Télécharger le CA depuis : 

### https://pki-servers.security.intraorange/app/my-certificates

Description de la commande : https://pki-servers.security.intraorange/app/my-certificates

### git config --global http.sslCAInfo /chemin/ca.crt

Description de la commande : git config --global http.sslCAInfo /chemin/ca.crt

### nan

Description de la commande : nan

### Erreur SSL à cause du CA ROOT Orange

Description de la commande : Erreur SSL à cause du CA ROOT Orange

### Télécharger le CA ROOT depuis :

Description de la commande : Télécharger le CA ROOT depuis :

### https://pki-servers.security.intraorange/app/my-certificates

Description de la commande : https://pki-servers.security.intraorange/app/my-certificates

### copier le fichier ici :

Description de la commande : copier le fichier ici :

### /usr/local/share/ca-certificates/ca.crt

Description de la commande : /usr/local/share/ca-certificates/ca.crt

### Lancer la cmd :

Description de la commande : Lancer la cmd :

### sudo update-ca-certificates

Description de la commande : sudo update-ca-certificates

### nan

Description de la commande : nan

### Étapes pour Windows

Description de la commande : Étapes pour Windows

### Ouvrir le gestionnaire des certificats

Description de la commande : Ouvrir le gestionnaire des certificats

### Appuyez sur Win + R et tapez :

Description de la commande : Appuyez sur Win + R et tapez :

### certmgr.msc

Description de la commande : certmgr.msc

### Importer le certificat root

Description de la commande : Importer le certificat root

### nan

Description de la commande : nan

### Naviguez vers Autorités de certification racines de confiance > Certificats.

Description de la commande : Naviguez vers Autorités de certification racines de confiance > Certificats.

### Faites un clic droit et sélectionnez Toutes les tâches > Importer.

Description de la commande : Faites un clic droit et sélectionnez Toutes les tâches > Importer.

### Suivez l’assistant et sélectionnez votre certificat root (par exemple, orange-root-ca.crt).

Description de la commande : Suivez l’assistant et sélectionnez votre certificat root (par exemple, orange-root-ca.crt).

### Redémarrer les applications concernées

Description de la commande : Redémarrer les applications concernées

### nan

Description de la commande : nan

### Une fois le certificat ajouté, redémarrez les applications ou services (GitLab Runner, Ansible, etc.).

Description de la commande : Une fois le certificat ajouté, redémarrez les applications ou services (GitLab Runner, Ansible, etc.).

### nan

Description de la commande : nan

### nan

Description de la commande : nan

### Git config

Description de la commande : Git config

### option git config

Description de la commande : option git config

### --system - table relevant for the whole machine

Description de la commande : --system - table relevant for the whole machine

### --global - for the current user

Description de la commande : --global - for the current user

### --local (default) for the current repository

Description de la commande : --local (default) for the current repository

### configuration de base

Description de la commande : configuration de base

### git config --global user.email johndoe@myemail.com

Description de la commande : git config --global user.email johndoe@myemail.com

### git config --global user.name "John Doe"

Description de la commande : git config --global user.name "John Doe"

### git config --global color.status auto

Description de la commande : git config --global color.status auto

### git config --global color.branch auto

Description de la commande : git config --global color.branch auto

### git config --global color.interactive auto

Description de la commande : git config --global color.interactive auto

### git config --global color.diff auto

Description de la commande : git config --global color.diff auto

### git config --global alias.adog "log --all --decorate --oneline --graph"

Description de la commande : git config --global alias.adog "log --all --decorate --oneline --graph"

### git config --global core.editor vim

Description de la commande : git config --global core.editor vim

### fichier : ~/.gitconfig

Description de la commande : fichier : ~/.gitconfig

### nan

Description de la commande : nan

### Afficher les configs

Description de la commande : Afficher les configs

### git config --list

Description de la commande : git config --list

### git config --list --global

Description de la commande : git config --list --global

### git config user.name

Description de la commande : git config user.name

### nan

Description de la commande : nan

### contenu du dossier .git

Description de la commande : contenu du dossier .git

### hooks directory contains all custom hooks. These are small (usually) scripts which have to be executed before commit, or after, before push, etc.

Description de la commande : hooks directory contains all custom hooks. These are small (usually) scripts which have to be executed before commit, or after, before push, etc.

### branches - this is deprecated. Don't think about it anymore.

Description de la commande : branches - this is deprecated. Don't think about it anymore.

### HEAD - pointer to the current branch and its latest commit.

Description de la commande : HEAD - pointer to the current branch and its latest commit.

### config - configuration file for the repository.

Description de la commande : config - configuration file for the repository.

### info - the place where you stage the files using git add.

Description de la commande : info - the place where you stage the files using git add.

### refs - the current state of the whole repo.

Description de la commande : refs - the current state of the whole repo.

### objects - commits, trees and blobs are stored here. May be very big.

Description de la commande : objects - commits, trees and blobs are stored here. May be very big.

### logs - quite self explanatory.

Description de la commande : logs - quite self explanatory.

### description - description of the repository.

Description de la commande : description - description of the repository.

### nan

Description de la commande : nan

### git checkout : annuler changement sur un fichier non indéxé (not yet added)

Description de la commande : git checkout : annuler changement sur un fichier non indéxé (not yet added)

### git checkout testfile-01

Description de la commande : git checkout testfile-01

### nan

Description de la commande : nan

### git rm : annuler modification indéxé (added)

Description de la commande : git rm : annuler modification indéxé (added)

###  supprime un fichier de la staging area sans le supprimer du disque.

Description de la commande :  supprime un fichier de la staging area sans le supprimer du disque.

### git rm --cached myfile

Description de la commande : git rm --cached myfile

### supprime un fichier à la fois de Git et du disque, même s'il est modifié.

Description de la commande : supprime un fichier à la fois de Git et du disque, même s'il est modifié.

### git rm -f myfile

Description de la commande : git rm -f myfile

### nan

Description de la commande : nan

### git reset et revert

Description de la commande : git reset et revert

### soft

Description de la commande : soft

### revenir 1 commit en arrière (voir git log) sans supprimer les modifications au niveau du fichier

Description de la commande : revenir 1 commit en arrière (voir git log) sans supprimer les modifications au niveau du fichier

### git reset --soft HEAD~1

Description de la commande : git reset --soft HEAD~1

### hard

Description de la commande : hard

### revenir 1 commit en arrière (voir git log) et  supprimer les modifications au niveau du fichier

Description de la commande : revenir 1 commit en arrière (voir git log) et  supprimer les modifications au niveau du fichier

### git reset --hard HEAD~1

Description de la commande : git reset --hard HEAD~1

### revert

Description de la commande : revert

### Il crée un nouveau commit qui annule un ancien commit

Description de la commande : Il crée un nouveau commit qui annule un ancien commit

### permet de rester linéaire et ne pas avoir un HEAD en retard par rapport au HEAD distant

Description de la commande : permet de rester linéaire et ne pas avoir un HEAD en retard par rapport au HEAD distant

### IMPORTAN : revert annule les modifications apportées par le commit ciblé par le revert

Description de la commande : IMPORTAN : revert annule les modifications apportées par le commit ciblé par le revert

### git revert --no-edit (ne pas modifier le message de commit par défaut) HEAD~1

Description de la commande : git revert --no-edit (ne pas modifier le message de commit par défaut) HEAD~1

### nan

Description de la commande : nan

### git diff

Description de la commande : git diff

### git diff

Description de la commande : git diff

### git diff HEAD~1

Description de la commande : git diff HEAD~1

### git diff HEAD~1 testfile-01

Description de la commande : git diff HEAD~1 testfile-01

### git diff --staged

Description de la commande : git diff --staged

### nan

Description de la commande : nan

### git show

Description de la commande : git show

### affiche le résultat de git log + git diff d'un commit. Utiliser git log -p pour tous les commits

Description de la commande : affiche le résultat de git log + git diff d'un commit. Utiliser git log -p pour tous les commits

### git show

Description de la commande : git show

### git show HEAD~1

Description de la commande : git show HEAD~1

### nan

Description de la commande : nan

### git tag

Description de la commande : git tag

### Supprimer tag

Description de la commande : Supprimer tag

### git tag -d v1.0

Description de la commande : git tag -d v1.0

### Basculer sur un tag

Description de la commande : Basculer sur un tag

### git checkout v1.0

Description de la commande : git checkout v1.0

### Créer un tag sur le commit courant

Description de la commande : Créer un tag sur le commit courant

### git tag -a v2.0 -m "version 2.0. A lot of new features"

Description de la commande : git tag -a v2.0 -m "version 2.0. A lot of new features"

### Afficher contenu d'un commit par son tag

Description de la commande : Afficher contenu d'un commit par son tag

### git show v1.0

Description de la commande : git show v1.0

### nan

Description de la commande : nan

### git fetch

Description de la commande : git fetch

### Télécharge les derniers commits distants sans les intégrer à la branche locale

Description de la commande : Télécharge les derniers commits distants sans les intégrer à la branche locale

### ces merge sont dans une branche différentes (ex: origin/main, local c'est main)

Description de la commande : ces merge sont dans une branche différentes (ex: origin/main, local c'est main)

### nan

Description de la commande : nan

### git rebase

Description de la commande : git rebase

### réécrit les commits d'une branche dans un historique linéaire sur la branche master

Description de la commande : réécrit les commits d'une branche dans un historique linéaire sur la branche master

### permet d'avoir un historique linéaire

Description de la commande : permet d'avoir un historique linéaire

### les nouveaux commits ont des identifiants différents des commits de la branche  (rebasés) 

Description de la commande : les nouveaux commits ont des identifiants différents des commits de la branche  (rebasés) 

### pratique : faire rebase et ensuite merger pour changer la pointe du master sur le dernier commit

Description de la commande : pratique : faire rebase et ensuite merger pour changer la pointe du master sur le dernier commit

### nan

Description de la commande : nan

### git remote add origin $URI

Description de la commande : git remote add origin $URI

### init remote repo

Description de la commande : init remote repo

### nan

Description de la commande : nan

### git remote -v

Description de la commande : git remote -v

### afficher les repo distant

Description de la commande : afficher les repo distant

### nan

Description de la commande : nan

### git fork

Description de la commande : git fork

### créer une copie d'un projet

Description de la commande : créer une copie d'un projet

### modifier et créer ensuite une PR (pull request)

Description de la commande : modifier et créer ensuite une PR (pull request)

### pour demander au projet forker d'accepter et merge les modifs

Description de la commande : pour demander au projet forker d'accepter et merge les modifs

### utilisé surtout sur les projets sur lesquels on a pas les droits de pull

Description de la commande : utilisé surtout sur les projets sur lesquels on a pas les droits de pull

### nan

Description de la commande : nan

### git merge <branch>

Description de la commande : git merge <branch>

### fast-forward merge

Description de la commande : fast-forward merge

### Le master n'a aucun nouveau commit comparé à la branche à merger. 

Description de la commande : Le master n'a aucun nouveau commit comparé à la branche à merger. 

### no fast-forward merge

Description de la commande : no fast-forward merge

### Le master a de nouveaux commits comparé à la branche à merger. Un commit de merge est créer

Description de la commande : Le master a de nouveaux commits comparé à la branche à merger. Un commit de merge est créer

