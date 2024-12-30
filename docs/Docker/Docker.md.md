# Docker  

## Compatibilité Kernel  

- Les conteneurs Docker partagent le **kernel du système hôte** (gère les ressources matérielles).  
- Par conséquent, Docker Linux ne peut tourner que sur un système hôte avec un **kernel Linux** compatible.  
## Installation  
### Convenience script
Il est préférable d'utiliser le [convenience script](https://get.docker.com/?_gl=1*1wpfmkm*_ga*MTgzODY3NDQ4My4xNzM0NjE4ODQx*_ga_XJWPQMJYHQ*MTczNDYxODg0MC4xLjEuMTczNDYxODg0NS41NS4wLjA.) pour une utilisation de docker **hors production**.  
### Windows
[Télécharger](https://www.docker.com/products/docker-desktop/)
### Documentation
https://docs.docker.com/engine/install/  

## Docker Exit  
Si le service qui tourne dans le container s'arrête le container est arrêté (exit)
## Commandes de base  

### RUN  
- **`docker run [image]`** : Lance un conteneur à partir d'une image.  
- **`docker run [image] [cmd]`** : Lance un conteneur à partir d'une image et taper la cmd.  
- **`docker run -d [image]`** : Lance un conteneur à partir d'une image et mode détaché  
- **`docker run -it [image]`** : Interactive terminal, permet d'afficher les promet et taper un argument si l'application le demande. 
- **`docker run -e mavariable=ABC [image]`** : définir variable
- **`docker run -p HostPort:ContainerPort [image]`** : port mapping
- **`docker run -v HostVolume:ContainerVolume [image]`** : port mapping  
- **`docker run --mount type=bind,source=/path/local,target=/path/container <image> :`** montage avec --mount
- **`docker run --memory="512m" --cpus="1.0" <image> :`** Définir les ressources
- **`docker run --name <container_name> --network <network_name> <image_name>`** : Attacher un réseau


### Gestion container  
- **`docker inspect [container]`** : Détail d'un container
- **`docker attach [container]`** : Se connecte au terminal d'un conteneur en cours d'exécution.
- **`docker ps`** : Affiche les conteneurs en cours d'exécution.  
- **`docker ps -a`** : Affiche tous les conteneurs, y compris ceux qui sont arrêtés.  
- **`docker stop [container]`** : Arrête un conteneur en cours d'exécution.  
- **`docker start [container]`** : Démarre un conteneur arrêté.  
- **`docker restart [container]`** : Redémarre un conteneur.  
- **`docker rm [container]`** : Supprime un conteneur arrêté.  
- **`docker exec -it [container] [command]`** : Exécute une commande dans un conteneur en cours d'exécution.  
- **`docker exec -it [container] env`** : Afficher les variables d'environnement du container
- **`docker logs [container]`** : Affiche les logs d'un conteneur.  

### Gestion images  
- **`docker rmi [image]`** : Supprime une image Docker.  
- **`docker build -t [image_name] [path]`** : Crée une image Docker à partir d'un Dockerfile.  
- **`docker images`** : Liste les images disponibles localement.  
- **`docker pull|push [image]`** : Télécharge/Upload une image depuis Docker Hub.
- **`docker push|pull [server]/[image]`** : Télécharge/Upload  une image depuis un registre privé.
- **`docker login [myrepo]`** : se connecter au repo privé myrepo

### Réseau/Volume  
- **`docker volume ls`** : Liste les volumes Docker.  
- **`docker network ls`** : Liste les réseaux Docker.  
- **`docker network create --driver bridge --subnet 192.168.100.0/24 --gateway 192.168.100.1 my_bridge_network  :`** Créer un nouveau subnet
- **`docker network connect <network_name> <container_name>`**: Attacher un réseau à un container
## Docker prune  
`docker <resource> prune`  

- **Images** :  
    - Une image est considérée comme "dangling" si elle n'a pas de tag (représentée par `<none>:<none>`) et n'est pas utilisée par un conteneur.  

- **Conteneurs** :  
    - Seuls les conteneurs **arrêtés** sont supprimés avec `docker container prune`.  
    - Un conteneur en cours d'exécution ne sera pas affecté.  

- **Volumes** :  
    - Seuls les volumes **non utilisés** par un conteneur actif ou arrêté sont supprimés avec `docker volume prune`.  

- **Réseaux** :  
    - Seuls les réseaux **non connectés** à un conteneur sont supprimés avec `docker network prune`.  
    - Les réseaux par défaut (`bridge`, `host`, `none`) ne sont jamais supprimés.    

- **Système** :  
    - `docker system prune` applique les règles ci-dessus pour toutes les ressources inutilisées.  
## Docker Hub  
[Listes des images](https://hub.docker.com/)  

## Accès application conteneurisée  
**1/ Depuis le host**  
Utiliser l'adresse IP du container `docker inspect [container]` 

**2/ Depuis l'extérieur**  
Faire du [port mapping](#commandes-de-bases) `docker run -p`  

## Créer image
**1/ Créer un dockerfile**  
<details>  
<summary>Dockerfile example</summary>  
```
# Utiliser une image Python comme base  
FROM python:3.9-slim  
  
# Définir le répertoire de travail  
WORKDIR /app  
  
# Copier les fichiers de l'application dans le conteneur  
COPY requirements.txt ./  
COPY app.py ./  
  
# Installer les dépendances  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Exposer le port utilisé par Flask  
EXPOSE 5000  
  
# Définir la commande pour lancer l'application Flask  
CMD ["python", "app.py"]  
```
</details>
**2/ builder l'image**  
```
docker build -t flask-app .  
```  
> Le deuxième build est plus rapide car les étapes de build (exemple : télécharge image ubuntu) ne sont pas rejouées.  

**3/ Upload image**  
A - Créer l'image avec le tag du repo et pousser  
```
docker tag flask-app:latest omael/flask-app:latest
```  
B - Se connecter au repo (créer un token dans paramètres)
```
docker login
```  
C - Pousser l'image
```
docker push omael/flask-app:latest
```  
## CMD   
- **Syntaxe :**  
    - Format JSON : `CMD ["executable", "param1", "param2"]`  
    - Format shell : `CMD command param1 param2`  
- **Peut être remplacé dans `docker run` :**  
    - Les arguments passés à `docker run` remplacent ceux de CMD.  
    - Exemple : `docker run my-image echo "Hello"`   
- **Est un argument de ENTRYPOINT si celui-ci existe :**  
	- CMD devient les arguments par défaut de l'ENTRYPOINT.  
	- Exemple :   
			`ENTRYPOINT ["echo"]`  
			`CMD ["Hello"] `

## ENTRYPOINT  

- **Syntaxe :**  
    - Format JSON : `ENTRYPOINT ["executable", "param1", "param2"]`  
    - Format shell : `ENTRYPOINT command param1 param2  `
- **Prend un argument dans `docker run` :**    
    - Les arguments passés à `docker run` s’ajoutent à ceux d’ENTRYPOINT.  
    - Exemple Entrypoint echo : `docker run my-image "Hello"`  
- **Prend comme argument CMD :**  
- CMD est utilisé comme arguments par défaut si `docker run` n’en fournit pas.  
- Exemple :  
	`ENTRYPOINT ["echo"]`    
	`CMD ["Hello"] `  
 - **Peut être remplacé dans `docker run` avec `--entrypoint` :**  
	- Exemple : `docker run --entrypoint "/bin/bash" my-image`  
## Variables d'environnement  
### Dockerfile  
**Une seule variable:**   
`ENV VARIABLE_NAME value`  

**Plusieurs variables:**   
`ENV VAR1=value1 VAR2=value2`  

**Utiliser une variable dans d'autres instructions**  
```
ENV APP_HOME /usr/src/app   
WORKDIR $APP_HOME  
```
### Command line  
` docker run -e APP_ENV=development my-image`  
## Docker Engine  
### Composants  
- **CLI** : Interface en ligne de commande pour interagir avec Docker.  
- **API REST** : Permet des intégrations et des automatisations.  
- **Daemon** : Gère les conteneurs et les images en arrière-plan.  
### Namespaces et Cgroups  

**Namespaces**  
Garantit **sécurité** et **confidentialité** entre conteneurs et hôte.  
- **PID** : Isole les processus du conteneur de ceux de l’hôte.  
- **Net** : Crée des réseaux isolés pour chaque conteneur.  
- **Mount** : Gère l’isolation des systèmes de fichiers.  
- **User** : Isole les ID utilisateurs entre conteneurs et hôte.  
- **IPC** : Sépare la communication inter-processus.  

**Cgroups**  
- Les **cgroups** permettent de limiter les ressources allouées à un conteneur, comme la mémoire et le CPU.  
**Exemple de commande :** 
`docker run --memory="512m" --cpus="1.0" <image>`  

## Docker Layers   (storage drivers)
- Géré par les **storage drivers** comme overlay2
- Les images Docker sont composées de **couches immuables** (layers).  
- Chaque instruction d’un Dockerfile crée une nouvelle couche.  
- Les conteneurs ajoutent une **couche de lecture/écriture** au-dessus des couches de l’image.  
- Les layers immuables sont réutilisables, ce qui optimise le stockage.  
## Storage  

[Commandes](#reseauvolume)  
### Chemin sur host  
`/var/lib/docker/volumes`
### Bind Mounting  
Lie un répertoire ou fichier de l’hôte directement au conteneur.  
`docker run -v /path/local:/path/container <image>`  
`docker run --mount type=bind,source=/path/local,target=/path/container <image>`  
### Volume Mounting  
- Utilise des volumes Docker gérés par Docker Engine.  
`docker run -v myvolume:/path/container <image>`  
`docker run --mount type=volume,source=myvolume,target=/path/container <image>  

## Réseaux Docker  
[Commandes](#reseauvolume)    
- **Bridge** :   
	- Utilisé par défaut si aucun réseau n'est spécifié  
	- Chaque conteneur obtient une adresse IP privée dans la plage 172.17.0.0/24
	- Les containers communiquent entre eux avec les IP privées
	- Pour un accès externe aux containers il faut faire du port mapping 
	- Créer un [nouveau subnet](#reseauvolume)
- **Host** :   
	- Le conteneur utilise le réseau de l’hôte, partageant l’IP de l’hôte pour les connexions réseau.  
	- Le service/port lancé dans le container est accessible directement depuis l'IP/port du host 
- **None** :   
	- Aucun réseau n’est connecté au conteneur, utilisé pour l'isolement total.  
- **DNS :**
	- Serveur DNS 127.0.0.11
	- Les conteneurs peuvent être résolus par leurs noms depuis un autre container  
## Registry privé  
**1/ Lancer le conteneur Registry**  
`docker run -d -p 5000:5000 --name registry registry:2`  
**2/ Pousser une image dans le registre privé**  
a) Registre local  
```
docker tag <image_name> localhost:5000/<image_name>
docker push localhost:5000/<image_name>  
```
	
b) Registre distant  
```
docker tag <image_name> <registry_url>/<repository>/<image_name>
docker push <registry_url>/<repository>/<image_name>
```
## Références  
[Coursera - Docker Basics for DevOps](https://www.coursera.org/learn/docker-basics-for-devops)  