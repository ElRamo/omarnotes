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
## Commandes de bases  

- **`docker run [image]`** : Lance un conteneur à partir d'une image.  
- **`docker run -d [image]`** : Lance un conteneur à partir d'une image et mode détaché
- **`docker attach [container]`** : Se connecte au terminal d'un conteneur en cours d'exécution.
- **`docker ps`** : Affiche les conteneurs en cours d'exécution.  
- **`docker ps -a`** : Affiche tous les conteneurs, y compris ceux qui sont arrêtés.  
- **`docker stop [container]`** : Arrête un conteneur en cours d'exécution.  
- **`docker start [container]`** : Démarre un conteneur arrêté.  
- **`docker restart [container]`** : Redémarre un conteneur.  
- **`docker rm [container]`** : Supprime un conteneur arrêté.  
- **`docker rmi [image]`** : Supprime une image Docker.  
- **`docker build -t [image_name] [path]`** : Crée une image Docker à partir d'un Dockerfile.  
- **`docker images`** : Liste les images disponibles localement.  
- **`docker pull [image]`** : Télécharge une image depuis Docker Hub.  
- **`docker push [image]`** : Envoie une image vers un registre Docker.  
- **`docker exec -it [container] [command]`** : Exécute une commande dans un conteneur en cours d'exécution.  
- **`docker logs [container]`** : Affiche les logs d'un conteneur.  
- **`docker volume ls`** : Liste les volumes Docker.  
- **`docker network ls`** : Liste les réseaux Docker.  
- **`docker prune`** : Supprime les ressources inutilisées (conteneurs, images, volumes, réseaux)  
## Docker Hub  
[Listes des images](https://hub.docker.com/)  

## Références  
[Coursera - Docker Basics for DevOps](https://www.coursera.org/learn/docker-basics-for-devops)  