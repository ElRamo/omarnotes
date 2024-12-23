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
- **`docker pull [image]`** : Télécharge une image depuis Docker Hub.  
- **`docker push [image]`** : Envoie une image vers un registre Docker.    

### Réseau/Volume  
- **`docker volume ls`** : Liste les volumes Docker.  
- **`docker network ls`** : Liste les réseaux Docker.  
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
docker build -t my/repo:tag .  
```  
B - Se connecter au repo (créer un token dans paramètres)
```
docker login
```  
C - Pousser l'image
```
docker push omar/flask-app tag
```  
## Références  
[Coursera - Docker Basics for DevOps](https://www.coursera.org/learn/docker-basics-for-devops)  