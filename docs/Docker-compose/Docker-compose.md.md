# Docker-compose  
## Définition  
**Docker Compose** est un outil pour définir et gérer des applications multi-conteneurs Docker à l’aide d’un fichier YAML.  

## Commandes de base  
- **`docker-compose up`** : Démarre les conteneurs définis.  
- **`docker-compose down`** : Arrête et supprime les conteneurs, réseaux et volumes.  
- **`docker-compose ps`** : Liste les conteneurs en cours d’exécution.  
- **`docker-compose logs`** : Affiche les journaux des conteneurs.  
- **`docker-compose build`** : Construit ou reconstruit les images.  
- **`docker-compose exec`** : Exécute une commande dans un conteneur en cours d’exécution.  

## Version du compose  

## Exemple docker-compose.yml  

<details><summary>docker-compose.yml</summary>

```
version: '3.9' # Version du format Compose

services:
  app:
    image: my-app:latest
    build:
      context: ./app
    ports:
      - "8080:80" # Mappe le port 80 du conteneur au port 8080 de l’hôte
    environment:
      - APP_ENV=production
    volumes:
      - ./data:/app/data
    networks:
      - my-network
    restart: always

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - my-network

networks:
  my-network:
    driver: bridge

volumes:
  db_data:
    driver: local
```
</details>

## Scaling  
**Important**  
	
- Le scaling fonctionne uniquement si le service est **stateless** (pas de conflit sur les ports ou volumes)
- Pour les services **stateful** (ex. bases de données), un orchestrateur comme **Docker Swarm** ou **Kubernetes** est recommandé.  


**Commande**  
`docker-compose up --scale service1=3 --scale service2=2`