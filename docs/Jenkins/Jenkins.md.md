# Jenkins
## CICD Définition

**CI Continuous Integration**   
- Tests du code   
- Packaging de l'application  

**CD Continuous Delivery/Deployment**  
- Authentification à l'infrastructure qui héberge l'application   
- Déploiement de l'application  
- Test de l'application  

**Delivery vs Deployment**  
- Delivery : Le déploiement est lancé manuellement depuis Jenkins  
- Deployment : Mise en production automatisée    

## Installation
Sé référer à la [documentation](https://www.jenkins.io/doc/book/installing)   
**Pré-requis linux**   
`sudo apt install openjdk-17-jdk`  
La version JDK dépend de la version de jenkins  

## Port d'écoute  
**8022** SSH  
**8085** Interface graphique

## Authentification SSH clé publique  
**Générer une paire de clés SSH** (si ce n'est pas déjà fait) :  
`ssh-keygen -t rsa -b 4096 -C "votre_email@example.com"`  

**Ajouter la clé publique à Jenkins** :   
- Connectez-vous à Jenkins.  
- Allez dans **Gérer Jenkins > Gérer les identifiants**.  
- Choisissez le périmètre approprié (par ex. Global).  
- Cliquez sur **Ajouter des identifiants**.  
- Sélectionnez **Type** : "Nom d'utilisateur SSH avec clé privée".  
- Saisissez un **Nom d'utilisateur** et collez votre clé privée (`~/.ssh/id_rsa`) dans le champ **Clé   privée**.  
## CLI  
### Installation  
Aller dans la rubrique `Jenkins > Manage Jenkins > Jenkins CLI` et suivre les étapes d'installation.  
1. Télécharger le zip jenkins-cli.jar  
### Commandes
**TOKEN**  
1. Créer le token depuis `Account > Security > API Token`   
2. Lancer la commande avec token:  
`java -jar jenkins-cli.jar -s http://$IP:8080/ -auth USER:TOKEN`  

**SSH**  
1. Créer et déployer la clé SSH (voir rubrique `Authentification SSH clé publique`)  
2. Lancer la commande avec SSH  
   `ssh -i /chemin/clé_privée -l USER -p 8022 jenkins-server help`  
   **jenkins-server :** IP ou FQDN du serveur  
   
**Liste des commandes**  
 UI : `Jenkins > Manage Jenkins > Jenkins CLI`  

## Backup  
### Script
[GitHub - sue445/jenkins-backup-script: archive jenkins setting and plugins](https://github.com/sue445/jenkins-backup-script)


## Référence cours
[Coursera : Jenkins for Beginners](https://www.coursera.org/learn/jenkins-for-beginners)


