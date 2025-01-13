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