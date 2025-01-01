# Terraform  

## Fichier `terraform.tfstate`  
Le fichier `terraform.tfstate` stocke **l'état actuel de l'infrastructure** telle que Terraform la connaît.  
le fichier **`terraform.tfstate`** est **mis à jour automatiquement** par Terraform chaque fois que **vous exécutez une commande** qui modifie l'état de l'infrastructure comme **terraform apply**  

**`terraform plan --refresh=false`** : Se baser uniquement sur le fichier `terraform.tfstate` et ne pas fetcher l'état de l'infra depuis le cloud (par ex)  

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
- **`terraform validate`** : Valide le fichier de configuration Terraform.  
- **`terraform fmt`** : Formate le fichier de configuration selon les standards.  
- **`terraform plan`** : Affiche un plan des modifications qui seront apportées à l'infrastructure.  
- **`terraform plan --refresh=false`** : Se baser uniquement sur le fichier .tfstate et ne pas fetch l'état de l'infra depuis le cloud (par ex)  
- **`terraform apply`** : Applique les changements planifiés pour créer ou modifier l'infrastructure.  
- **`terraform apply -refresh-only`** : Met à jour le state sans modifier l'infrastructure  
- **`terraform show`** : Affiche les détails de l’état ou du plan.  
- **`terraform output`** : Montre les valeurs des sorties définies dans le fichier Terraform.  
- **`terraform output`** : Affiche les valeurs des outputs définis dans le fichier de configuration après l'exécution de `terraform apply`  
- **`terraform providers`** : Liste les providers utilisés dans la configuration.  
- **`terraform providers mirror`** : Télécharge les providers dans un répertoire local.  
- **`terraform graph`** : Génère un graphe des ressources Terraform en format DOT.  
- **`terraform destroy`** : Supprime l'infrastructure gérée par Terraform.  
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

## Variables  

### Définir la valeur d'une variable
#### -var  
`terraform apply -var="instance_type=t2.micro"`  
#### terraform.tfvars  (-var-file)
```
# terraform.tfvars  
instance_type = "t2.micro"  
region         = "us-west-2"  
```

`terraform apply -var-file="custom.tfvars"`  
#### export  
`export TF_VAR_instance_type="t2.micro"`  
`terraform apply`  
#### Valeur par défaut dans variables.tf 
voir ci-dessous  
#### \*.auto.tfvars  
```
# Something.auto.tfvars
instance_type = "t2.micro"
region         = "us-west-2"
```  
Le fichier est reconnu **automatiquement**  
`terraform apply`

#### Précédence  
1. **Variables d'environnement** (par exemple `TF_VAR_instance_type`).
2. **`-var` en ligne de commande**.
3. **Fichiers `-var-file`** (ex : `-var-file="custom.tfvars"`).
4. **Fichiers `*.auto.tfvars`** (chargés automatiquement par Terraform).
5. **Fichier `terraform.tfvars`** (chargé automatiquement par Terraform si présent).
6. **Valeurs par défaut dans le fichier `variables.tf`**.

### Déclarer/Appeler variable
#### variables.tf
Contenues dans le fichier **variables.tf**   
<details><summary>variables.tf</summary>  
```
# String
variable "instance_type" {
  description = "Type of EC2 instance"
  type        = string
  default     = "t2.micro"
}

# Number
variable "instance_count" {
  description = "Number of EC2 instances"
  type        = number
  default     = 1
}

# Map
variable "tags" {
  description = "Tags for the resources"
  type        = map(string)
  default = {
    Environment = "dev"
    Project     = "example"
  }
}

# List(string)
variable "allowed_ips" {
  description = "List of allowed IPs for security groups"
  type        = list(string)
  default     = ["192.168.1.1", "192.168.1.2"]
}

# Liste(number)
variable "allowed_numbers" {
  description = "List of allowed numbers"
  type        = list(number)
  default     = [ 1,2,3 ]
}

# Tuple
#Chaque élément doit correspondre au type défini + Ordre garanti
variable "example_tuple" {
  type = tuple([string, number, bool])
  default = ["example", 42, true]
}

# Object
variable "example_object" {
  type = object({
    name    = string
    age     = number
    active  = bool
  })
  default = {
    name   = "Alice"
    age    = 30
    active = true
  }
}

# Set = une liste avec ordre garanti et chaque élément est unique
variable "example_set" {
  type    = set(string)
  default = ["apple", "banana", "cherry"]
}


```
</details>  
#### main.tf  
Les variables sont ensuite appelées dans **main.tf**  
<details><summary>main.tf</summary>
```
provider "aws" {
  region = "us-west-2"
}

# String
resource "aws_instance" "example" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"

  tags = {
    Name = var.instance_name # Appel de la variable string
  }
}

# Number + count
resource "aws_instance" "example_multiple" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  count         = var.instance_count # Appel de la variable number

  tags = {
    Name = "Instance-${count.index}" # Exemple d'utilisation de count.index
  }
}

# Map
resource "aws_s3_bucket" "example" {
  bucket = "${var.tags["Environment"]}-bucket" # Appel d'une clé spécifique dans le map
  project = var.tags["myproject"]
  acl    = "private"

  tags = var.tags # Appel complet de la map pour les tags
}

# List
resource "aws_security_group" "example" {
  name_prefix = "example-"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.allowed_ips # Appel de la liste complète
  }

  # Appel d'un membre spécifique de la liste
  tags = {
    FirstAllowedIP = var.allowed_ips[0] # Premier élément de la liste
  }
}

# Tuple
output "first_element" {
  value = var.example_tuple[0]  # "hello"
}

output "second_element" {
  value = var.example_tuple[1]  # 123
}

# Object
output "name" {
  value = var.example_object.name  # "Alice"
}

output "age" {
  value = var.example_object.age   # 30
}

output "active_status" {
  value = var.example_object.active  # true
}

# Set
output "first_item" {
  value = element(var.example_set, 0)  # "apple"
}

output "all_items" {
  value = join(", ", var.example_set)  # "apple, banana, cherry"
}


```
</details>   
## Resource attributs  
```
# Ressource 1 : EC2 Instance
resource "aws_instance" "example" {
  ami           = "ami-12345678"         # Attribut : ID de l'AMI
  instance_type = "t2.micro"             # Attribut : Type d'instance
  key_name      = "my-key-pair"          # Attribut : Nom de la clé SSH

  tags = {
    Name = "ExampleInstance"             # Attribut : Tag personnalisé
  }
}

# Ressource 2 : Elastic IP (EIP) qui dépend de l'instance EC2
resource "aws_eip" "example_ip" {
  instance = aws_instance.example.id    # Utilisation de l'attribut 'id' de l'instance EC2
  Name = "EIP for instance ${aws_instance.example.id}" # Ex de ID au milieu d'une chaine de caractères  
}

```   
## Dependencies  
#### implicites   
Terraform gère automatiquement les dépendances entre ressources
#### explicites  
```
resource "aws_instance" "example" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}

resource "aws_security_group" "example" {
  name        = "example-sg"
  description = "Example security group"

  # Dépend explicitement de la création de l'instance
  depends_on = [aws_instance.example]
}
```     
## Output  
dans **fichier.tf**  
```
output "example_output" {
  value = aws_instance.example.id
}  
```  
La valeur est alors affichée lors du `terraform apply`
Il est possible aussi d'afficher les outputs avec `terraform output`  

## Terraform graph  
**1/ Installer graphviz**  
`apt install graphviz -y`  
**2/ Générer le graphe**  
`terraform graph | dot -Tsvc > graph.svg`  

## Immutable (Inimutable)  
**Immutable**: Si une modification est nécessaire, la ressource doit être détruite et recréée
```
resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  lifecycle {
    prevent_destroy = true
    create_before_destroy= true
  }
}
```  
**prevent_destroy**: Permet d'empêcher la suppression de la resource lors de `terraform apply`. Cependant, la resource sera tout de même supprimée si `terraform destroy`