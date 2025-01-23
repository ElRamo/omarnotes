# Vault  

## Dev mode  

- Démarrer rapidement un serveur pour des tests ou de l'**apprentissage**.   
- Il est **non sécurisé**  
- Utilise un **storage inmem** qui est éphémère  


**1/ démarrer Vault en mode développement**   
`vault server -dev`  

**2/ Exporter l'adresse et le token**  
```
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='<dev-root-token>'
```  
    
**3/ Tester la connexion**  
`vault status`  

## Auto-complétions   
```
echo "source /usr/share/bash-completion/bash_completion" >> ~/.bashrc
vault -autocomplete-install
source ~/.bashrc
```

## CLI - gérer les secrets  
1. Créer un chemin (activer le moteur de secrets KV) :  
	`vault secrets enable -path=<nom_du_path> kv`  

2. Créer ou mettre à jour un secret (KV) :    
	`vault kv put <path>/<clé> <nom_de_clé>=<valeur>`  

3. Récupérer un secret :  
	`vault kv get <path>/  
	`vault kv get <path>/<clé>`  
	`vault kv get -format=json <path>/<clé>`  

4. Supprimer un secret :   
	`vault kv delete <path>/<clé>`  
5. Afficher tous les paths  
	`vault secrets list`
  
## Secrets Engines  

Gère un **type spécifique** de données ou d'opérations (ex. : KV, PKI, DB credentials, AWS).    

[Liste des secrets engines disponibles](https://developer.hashicorp.com/vault/docs/secrets#secrets-engines)  

**Activer un secret engine**   
`vault secrets enable -path=<path> <type>`  

**Désactiver un secret engine**  
`vault secrets disable <path>`  

## Secrets dynamiques  

Il est possible de générer **dynamiquement** secrets grâce aux **secrets engines**.  
**Exemple AWS** [documentation](https://developer.hashicorp.com/vault/docs/secrets/aws)  

**1/** Activer le moteur de secrets AWS dans Vault  
```
vault secrets enable aws
```
**2/** Configurer les identifiants AWS dans Vault  
```
vault write aws/config/root \
    access_key=$access \
    secret_key=$secret$ \
    region=us-east-1
```
**3/** Créer un rôle (my-role) Vault avec une politique IAM (CLI ou GUI)  
**4/** Générer des credentials temporaires via le rôle
```
vault read aws/creds/my-role
```
**5/** Vérifier l'expiration des credentials  
```
vault read aws/stats
```

## Authentication  

### Token  

`vault login -method=token <token>`: Se connecter à Vault avec un token  
`vault token create`: Générer un nouveau token d'accès  
`vault token revoke <token>`: Révoquer un token existant  

### Github  

1. **Prérequis sur Github.com :**  
    - Créer une organisation : Profil > Organizations > New organization  
    - Créer une team : Organisation > Teams > New team  
    - Ajouter les utilisateurs à la team  
2. **Créer un token :**  
    - Profil > Settings > Developer settings > Personal access token > Token (classic) > Generate  
    - Sélectionner les permissions nécessaires  
    - Copier le token immédiatement après sa création  
3. **Se connecter :**  
    - `vault auth enable github`  
    - `vault write auth/github/config organization=NOM-ORGANISATION  `
    - `vault write auth/github/map/teams/NOM-TEAM value=ROLE`  
    - `vault login -method=github token=<token>`  
4. **Révoquer l'accès :**  
    - Supprimer le token sur Github  
    - `vault token revoke -mode path auth/github`  

### Connexion ldap en CLI
`vault login -method=ldap username=$(whoami)`  
## Serveur de prod  

**1/ Créer le fichier** <details><summary>config.hcl</summary>
```
# Adresse du listener, où Vault écoutera les requêtes HTTP
listener "tcp" {
  # L'adresse d'écoute (localhost pour la prod, utiliser une adresse réseau en prod)
  address = "0.0.0.0:8200"  # Écoute sur toutes les interfaces réseau
  # Si vous utilisez HTTPS, configurez un certificat SSL ici
  tls_cert_file = "/etc/vault.d/vault.crt"
  tls_key_file  = "/etc/vault.d/vault.key"
  # Si HTTPS désactivé
  tls_disable = "true"

}

# Configuration du stockage local (sur disque)
storage "file" {
  # Chemin du répertoire où Vault stocke ses données
  path = "/opt/vault/data"
}


# Adresse de l'API, utilisée pour interagir avec Vault
api_addr = "https://vault.example.com:8200"  # Adresse externe de Vault
ui = true
```
</details>

**2/ Créer le dossier data**  
```
mkdir -p vault/data
chown vault vault/data
```
**3/ Lancer le serveur**  
`vault server -config=config.hcl`

**4/ Exporter la variable**  
`export VAULT_ADDR='http://127.0.0.1:8200'`  

**5/ Init vault**  

- Le serveur démarre en mode `sealed` (read/write bloqué).
- Les clés de unseal sont nécessaires pour démarrer Vault après chaque redémarrage.  
`vault operator init`  

## Approle  

**1/ Activer le backend d'authentification AppRole**   
`vault auth enable approle`

**2/ Créer un approle**  
```
vault write auth/approle/role/<role-name> \
    secret_id_ttl=60m \
    token_ttl=20m \
    token_max_ttl=30m \
    policies="<policy-name>"
```   

**3/ Récupérer le Role ID**  
`vault read auth/approle/role/<role-name>/role-id`  

**4/ Générer un Secret ID**  
`vault write -f auth/approle/role/<role-name>/secret-id`  

**5/ Authentification avec AppRole**  
```
vault write auth/approle/login \
    role_id="<role-id>" \
    secret_id="<secret-id>"
```  

## Entités et Alias  

- **Entité** : Identité unique d'un utilisateur dans Vault.  
- **Alias** : Méthode d'authentification liée à une entité (ex : LDAP, GitHub).   
- **Fusion d'entités** : Combine plusieurs entités en une seule pour regrouper les alias.  

**Exemple** :   
Alice utilise LDAP et GitHub. Vault crée une entité pour chaque méthode. En fusionnant, Alice a une seule entité avec les deux alias, partageant les mêmes policies.  

## Lease  
Un **lease** dans Vault correspond à une durée de vie temporaire associée à une ressource, comme des secrets, des tokens, ou des identifiants générés. Cela permet de garantir que ces ressources expirent après un certain temps pour des raisons de sécurité.  

Superviser ce métrique aide à :  

- Suivre l'utilisation des ressources Vault.  
- Identifier une accumulation anormale de leases (potentiellement due à des fuites ou des processus non nettoyés).  

## Cluster et Storage  
### Consul vs RAFT
- Vault utilisait auparavant **Consul** comme backend de stockage pour gérer les données et assurer la haute disponibilité.  
- Désormais, Vault utilise un **storage intégré basé sur RAFT**.  
- Le backend RAFT offre :  
    - Réplication intégrée des données.  
    - Haute disponibilité native.  
    - Simplification de la configuration en éliminant la dépendance à Consul.  

### Retry_join
- Dans chacun des nœuds on ajoute les autres nœuds dans retry_join
- Lancer `vault operator init` sur un nœuds va lancer `init` **tous les nœuds** du cluster  
- Il faut **unseal** vault sur tous les nœuds si ce dernier n'est pas en mode auto-unseal (ex: AWS KMS)    
<details><summary>Exemple de configuration retry_join</summary>
```
# Configuration du backend de stockage intégré basé sur RAFT
storage "raft" {
  # Chemin local où Vault stockera les données
  path    = "/opt/vault/data"
  
  # Identifiant unique pour ce nœud dans le cluster
  node_id = "vault-node-1"

  # Configuration pour rejoindre un cluster existant
  retry_join {
    # Adresse API du leader ou d'un autre nœud connu
    leader_api_addr = "https://vault-node-2:8200"
  }
  retry_join {
    # Adresse API d'un autre nœud connu
    leader_api_addr = "https://vault-node-3:8200"
  }
}

# Configuration de l'écoute des requêtes
listener "tcp" {
  # Adresse et port sur lesquels Vault écoute les requêtes
  address     = "0.0.0.0:8200"

  # Désactiver TLS (0 = activé, 1 = désactivé). Ici, TLS est activé.
  tls_disable = 0

  # Chemin vers le certificat TLS
  tls_cert_file = "/etc/vault/ssl/vault.crt"

  # Chemin vers la clé privée TLS
  tls_key_file  = "/etc/vault/ssl/vault.key"

}

# Adresse API utilisée pour accéder à Vault depuis l'extérieur
api_addr = "https://vault-node-1:8200"

# Adresse utilisée pour la communication interne entre les nœuds du cluster
cluster_addr = "https://vault-node-1:8201"
```
</details>  

### Auto_join
L'**auto-join** permet à un nœud Vault de rejoindre automatiquement un cluster existant en découvrant les autres nœuds via un fournisseur ou une configuration prédéfinie (ex : AWS tags).  
- Dans chacun des nœuds on ajoute les autres nœuds dans retry_join
- Lancer `vault operator init` sur un nœuds va lancer `init` **tous les nœuds** du cluster  
- Il faut **unseal** vault sur tous les nœuds si ce dernier n'est pas en mode auto-unseal (ex: AWS KMS)    
- Créer une nouvelle instance avec **les bons tags** fera qu'elle va **rejoindre automatiquement** le cluster
<details><summary>Exemple de configuration AWS</summary>
```
# Configuration du backend de stockage RAFT
storage "raft" {
  # Chemin local où Vault stockera les données
  path    = "/opt/vault/data"
  
  # Identifiant unique pour ce nœud dans le cluster
  node_id = "vault-node-aws-1"

  # Configuration autojoin basée sur les tags AWS
  retry_join {
    # Type de fournisseur autojoin : AWS
    provider = "aws"

    # Région AWS où se trouvent les instances
    region = "us-east-1"

    # Clé du tag AWS à utiliser pour identifier les instances du cluster
    tag_key = "vault-cluster"

    # Valeur du tag AWS correspondant aux instances Vault
    tag_value = "production"

    # Optionnel : Nom du rôle IAM (si nécessaire pour accéder à AWS)
    iam_server_id_header_value = "vault"
    
    # Spécifie que le schéma HTTPS doit être utilisé
     auto_join_scheme = "https"
  }
}

# Configuration de l'écoute des requêtes
listener "tcp" {
  # Adresse et port sur lesquels Vault écoute les requêtes
  address     = "0.0.0.0:8200"

  # Désactiver TLS (0 = activé, 1 = désactivé). Ici, TLS est activé.
  tls_disable = 0

  # Chemin vers le certificat TLS
  tls_cert_file = "/etc/vault/ssl/vault.crt"

  # Chemin vers la clé privée TLS
  tls_key_file  = "/etc/vault/ssl/vault.key"
}

# Adresse API utilisée pour accéder à Vault depuis l'extérieur
api_addr = "https://vault-node-aws-1:8200"

# Adresse utilisée pour la communication interne entre les nœuds du cluster
cluster_addr = "https://vault-node-aws-1:8201"
```
</details>  

### Configurer Cluster manuellement avec CLI  
**Lancer le  nœud leader**
`vault server -config=/path/to/config.hcl`  

**Initialiser Vault**  
`vault operator init -key-shares=1 -key-threshold=1`  

**Déverrouiller Vault**  
`vault operator unseal`  

**Connectez-vous avec le root token**  
`vault login <root_token>`  

**Vérifiez le statut du cluster**  
`vault operator raft list-peers`  

**Sur le deuxième cluster : Joindre le Cluster leader**  
- Vault sera **init automatiquement**  
- Il faut **unseal** vault si ce dernier n'est pas en mode auto-unseal (ex: AWS KMS)  
`vault operator raft join https://vault-leader:8200`  
### Commandes pratiques 
```
vault operator raft list-peers
vault operator raft join <leader_api_addr>
vault operator raft remove-peer <node_id>
vault operator step-down
```


