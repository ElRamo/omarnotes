# Terraform  

## Fichier `.tfstate`  
Le fichier `.tfstate` stocke **l'état actuel de l'infrastructure** telle que Terraform la connaît.  
le fichier **`.tfstate`** est **mis à jour automatiquement** par Terraform chaque fois que **vous exécutez une commande** qui modifie l'état de l'infrastructure comme **terraform apply**  

## Declaratif vs Imperatif  
### En général
- **Déclaratif** : Vous décrivez l'état final souhaité de l'infrastructure, et Terraform détermine les actions nécessaires pour y parvenir.  
- **Inverse** : La méthode **impérative**, où vous spécifiez étape par étape les actions à exécuter. 
### Terraform  
**Terraform** fonctionne en mode **Déclaratif**  

## Providers  
**Définition**  
Les providers offrent des ressources que l'on peut utiliser pour déployer.   

Le **provider** `AWS`, par exemple, propose la **ressource** `aws_ec2_instance_state`, qui permet de modifier l'état d'une instance EC2  

**Repository**  
[Browse Providers | Terraform Registry](https://registry.terraform.io/browse/providers)  

**Répertoire de télécharge**  
`monDossier/.terraform/providers/`
## Commandes de base  
- **`terraform init`** : Initialise le répertoire de travail avec les plugins nécessaires pour utiliser Terraform.  
- **`terraform plan`** : Affiche un plan des modifications qui seront apportées à l'infrastructure.  
- **`terraform apply`** : Applique les changements planifiés pour créer ou modifier l'infrastructure.  
- **`terraform destroy`** : Supprime l'infrastructure gérée par Terraform.  
- **`terraform validate`** : Valide le fichier de configuration Terraform.  
- **`terraform fmt`** : Formate le fichier de configuration selon les standards.  
- **`terraform show`** : Affiche les détails de l’état ou du plan.  
- **`terraform output`** : Montre les valeurs des sorties définies dans le fichier Terraform.  
## Etapes de déploiement 

1. **`terraform init`** :  
    - Télécharge les plugins nécessaires et prépare l’environnement de travail.  
2. **`terraform plan`** :   
    - Vérifie la configuration et affiche les changements qui seront réalisés sans les appliquer.  
3. **`terraform apply`** :  
    - Exécute les modifications prévues dans l’étape précédente pour déployer l’infrastructure.  
## Fichier `.tf`  
**Exemple** :  
```
provider "aws" {  
  region = "us-west-2"  
}  
  
resource "aws_instance" "example" {  
  ami           = "ami-12345678"  
  instance_type = "t2.micro"  
  
  tags = {  
    Name = "ExampleInstance"  
  }  
}  
``` 
**Explications** :

- **`provider`** : Définit le fournisseur cloud (ici AWS) et la région.
- **`resource`** : Crée une instance EC2 avec l’AMI spécifiée et le type d’instance choisi.
- **`tags`** : Ajoute un tag "Name" pour identifier la ressource.