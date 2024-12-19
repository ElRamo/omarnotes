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

## Github/Jenkins Webhook  

### Polling vs Webhook  
**Polling** configure une cron pour vérifier les changements au niveau du projet Github. Aucune configuration n'est nécessaire au niveau de Github.  
**Webhook** Permet de déclencher la pipeline avec un trigger qui est un changement au niveau de Github

### Webhook configuration  
**1/ Configurer GitHub (Webhook)** :  
- Allez dans votre dépôt GitHub.  
- Accédez à **Settings > Webhooks**.  
- Cliquez sur **Add webhook**.  
- Entrez l'URL de votre Jenkins suivi de `/github-webhook/` (ex. `http://your-jenkins-url/github-webhook/`).  
    - Si Jenkins est local, utilisez un service comme **ngrok** pour exposer votre Jenkins à Internet. 
- Cochez **Just the push event** pour que le webhook se déclenche sur chaque `push`.  
- Cliquez sur **Add webhook**.  

**2/ Configurer Jenkins (GitHub Plugin)** :  

- **Installer les plugins nécessaires** : Allez dans **"Gérer Jenkins" > "Gérer les plugins"** et installez les plugins **GitHub Plugin** et **GitHub Branch Source Plugin**.  
- Dans votre job Jenkins, sous **Source Code Management**, configurez votre dépôt GitHub (URL et authentification si nécessaire).  
- Sous **Build Triggers**, activez **"GitHub hook trigger for GITScm polling"** pour que Jenkins réagisse aux événements du webhook GitHub.  

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
### Plugin
**Télécharger le plugin ThinBackup**  
`Dashboard > Manage Jenkins > Pugins > Available Jenkins`  
**Configurer le plugin**  
`Dashboard > Manage Jenkins > System`  
### Snapshot   
A venir… peut être   

## Pipelines  
### Chemin sur le serveur  
`/var/lib/jenkins/workspace/pipeline_name`  
### Jenkinsfile sur Github  
Dans la configuration de la pipeline, cocher la case `GitHub project` et ajouter le lien du projet Github, exemple `https://github.com/ElRamo/myflaskapp/blob/main/Jenkinsfile`  

### Exemple de script Pipeline  
<details> 
<summary>Cliquer pour dérouler</summary> 
```
pipeline {  
  agent { docker { image 'python:3.8' } }  
  stages {  
    stage('build') {  
      steps {  
			sh 'python -m venv .venv'  
			sh '''  
				. .venv/bin/activate  
				pip install -r requirements.txt  
			 
			'''  
        
      }  
    }  
    stage('test') {  
      steps {  
			sh '''  
				. .venv/bin/activate  
				pytest --junit-xml test-reports/results.xml application_test.py  
				  
			'''  
         
      }  
      post {  
        always {  
          junit 'test-reports/*.xml'  
        }  
      }      
    }  
  }  
}   
```
</details>  
## Référence cours
[Coursera : Jenkins for Beginners](https://www.coursera.org/learn/jenkins-for-beginners)


