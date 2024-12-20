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
2. java -jar jenkins-cli.jar -s http://@IP:8080/ help  
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
On peut utiliser un **WebHook** (voir plus bas), ou lancer la pipeline **manuellement**.  
Pour lancer **manuellement** :  
1. Créer un nouveau item pipeline  
2. Dans **pipeline definition** sélectionner **Pipeline script from SCM**  
3. Choisir le projet Git et la branche  

### Exemple de declarative script Pipeline  
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

### Github/Jenkins Webhook  

#### Polling vs Webhook  
**Polling** configure une cron pour vérifier les changements au niveau du projet Github. Aucune configuration n'est nécessaire au niveau de Github.  
**Webhook** : Permet de déclencher le pipeline en réponse à un changement du code Github (commit etc)  
> Il est obligatoire de renseigner le [script from SCM](#jenkinsfile-sur-github) pour utiliser webhook et/ou Polling
#### Polling configuration  
1. Créer un nouvel item **pipeline**  
2. Dans général sélectionner **GitHub project** et renseigner le lien du projet  
3. Dans **Build triggers** sélectionner **Poll SCM**  
4. Choisir la fréquence *(ex: * * * * )*  
#### Webhook configuration  
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

### Affichage Pipelines  
1. Aller dans `Dashboard` et cliquer sur `+ new view`  
2. Choisir `Build pipeline view`  
3. Dans `Pipeline Flow` choisr `Based on upstream/downstream relationship`  
4. Sélectionner le job initial de la pipeline dans `Select initial job` et sauvegarder   

### Pipeline scriptée vs Pipeline déclarative  
<details>
<summary>Pipeline scriptée</summary>
```
node {
	stage ("checkout"){
		git branch : "main" , url: "https://github.com/ElRamo/SpringPetClinic"	
	}
	stage ("built"){
		withMaven(maven: "M3"){
			sh "mvn compile"
		}
	 }
}
``` 
</details>
<details>
<summary>Pipeline déclarative</summary>
```
pipeline{  

  agent any  
  tools {maven "M3"}  
  stages{  
    
    stage("checkout"){  
      steps{     
        git branch: "main" , url: "https://github.com/ElRamo/SpringPetClinic"  
      }  
    }  
  
    stage("test"){  
        steps{  
          sh "mvn test"  
        }     
    }    
  }  
}  
```
</details>  
> Les deux types de pipelines, **scriptée** et **déclarative**, peuvent être utilisés dans un **Jenkinsfile** dans GitHub (voir la rubrique **Github hook**).  
## Architectures  
- **Standalone (Monolithique)** : Une seule instance Jenkins gère tout, idéal pour des projets simples.  
- **Distributed (Controller/Agent)** : Un controller orchestre des agents pour exécuter les tâches, adapté à la montée en charge.  
- **High Availability (HA)** : Plusieurs controllers configurés pour garantir une résilience en cas de panne.  
- **Containerized Jenkins** : Jenkins et les builds sont isolés dans des conteneurs pour une meilleure reproductibilité.  
- **Cloud-Native Jenkins** : Déployé sur le cloud avec des agents éphémères pour une scalabilité automatique.  
- **Pipeline-as-a-Service (Jenkinsfile-Driven)** : Les pipelines sont définis dans des fichiers versionnés, offrant flexibilité et contrôle.  
- **Event-Driven Jenkins** : Jenkins réagit à des événements externes comme des commits ou des notifications cloud.  
## Types d'items  
### Freestyle projet  (exemple : Maven)
1. Aller dans `Manager Jenkins > Global tool configuration > Maven`  
2. Configurer l'installation Maven (nom et version)  
3. Créer un nouvel item de type `freestyle project`  
4. Définir le lien du projet github dans `source code management`  
5. Dans `Build Steps` choisir `Invoke top-level Maven Targets > Maven version créée plutôt` Goals `compile` ou `Test`   
6. Pour le Goal `Test` définir `Build Triggers > Build after other projects are built` et définir le projet de compile  
### Pipeline  
Définir le `script` du pipeline directement ou spécifier un `GitHub Project` contenant un fichier `Jenkinsfile` (voir la rubrique pipeline plus haut)

## Ajouter un nœud  
Aller dans `Manage Jenkins > Nodes > New Node`

## A venir
- **Gestion des utilisateurs** :  
    - Créer et gérer des utilisateurs avec des rôles spécifiques.  
    - Configurer des stratégies d'autorisation (par exemple, **Matrix Authorization Strategy** ou **Role-based Authorization Strategy**).  
- **Permissions de base** :  
    - **Lire** : Accès en lecture aux jobs.  
    - **Exécuter** : Permet de lancer un job.  
    - **Configurer** : Accès pour modifier un job.  
    - **Administrer** : Accès complet pour gérer Jenkins (configuration globale, gestion des utilisateurs).  
- **RBAC (Role-Based Access Control)** :  
    - Définir des rôles (Admin, Developer, Read-Only) pour limiter les actions des utilisateurs.  
    - Restreindre l'accès à certains jobs ou environnements.  
- **Sécurisation de Jenkins** :  
    - Utiliser **SSL** pour sécuriser les connexions.  
    - Intégrer avec des outils externes (LDAP, Active Directory) pour l'authentification. 
    - Utiliser des plugins comme **Build Authorization Plugin** pour contrôler l'accès aux builds.  
- **Gestion des permissions par job** :   
    - Configurer les droits d'accès spécifiques sur chaque job (lecture, exécution, configuration).  
    - Utiliser des plugins pour restreindre l'accès à des jobs sensibles ou critiques.  
- **Audits et logs** :  
    - Activer la journalisation des actions des utilisateurs pour un audit complet.  
    - Surveiller les accès et l'activité des utilisateurs pour prévenir les abus.   

## Référence cours
[Coursera : Jenkins for Beginners](https://www.coursera.org/learn/jenkins-for-beginners)  
[Coursera : CICD Using Jenkins](https://www.coursera.org/learn/cicd-using-jenkins)


