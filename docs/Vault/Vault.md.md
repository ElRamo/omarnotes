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
