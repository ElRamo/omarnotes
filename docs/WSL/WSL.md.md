# WSL
## Initialisation  
```
wsl --install  
wsl --set-default-version 2  
reboot pc  
Microsoft store > installer ubuntu  
wsl  
sudo apt update 
```
 
## Arrêter/lancer session  
```
wsl --terminate <NomDeLaDistribution>  
wsl --list  
wsl -d Ubuntu-22.04  
```  

## backup d'une session  
`wsl --export Ubuntu-22.04 mybackup.tar`  

## Restaurer la session  
`wsl --import <DistributionNewName> <InstallLocation> <PathToBackupTar>`  


## Erreur SSL 
1. Télécharger le CA ROOT  
2. copier le fichier ici dans `/usr/local/share/ca-certificates/ca.crt`  
3. Lancer la cmd : `sudo update-ca-certificates` 

## Afficher les distributions lancées  
`wsl --list --running`

## Créer une nouvelle session  
1. Créer une backup d'une session existante  
2. Restaurer la distribution avec un nouveau nom de distribution  
3. Lancer la nouvelle distribution (voir les commandes ci-dessus)   

## Emplacement de stockage session
connaître le dossier où est stockée l'image Ubuntu-22.04  
```
"Get-ChildItem ""HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss"" | ForEach-Object {
    Get-ItemProperty $_.PSPath
} | Where-Object { $_.DistributionName -eq ""Ubuntu-22.04"" } | Select-Object BasePath"
```

## changer hostname  
```
vim /etc/wsl.conf
[network]  
hostname = MyCustomHostname
generateHosts = false
```
## Lancement de session après démarrage Windows  
Ouvrir un cmd et taper  
```
notepad %USERPROFILE%\.wslconfig
```
Ajouter le paramètre ci-dessous au fichier et enregistrer
```
[boot]
command="wsl -d MaSession"
```
