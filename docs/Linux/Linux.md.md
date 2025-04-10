# Linux  
## APT  
**Trouver la source d'un package installé**  
`apt-cache policy $package`  

**Installer un package depuis un repo spécifique**  
`apt -t $repo install $package`  

**Afficher les packages disponibles dans le repo**  
`apt-cache search $package`  
`apt-cache showpkg $package`  

**Installer un package depuis internet**  
`wget -P $url`  
`dpkg -i $package`  

**Créer un repo local**   
1/ Télécharger paquets  
`apt-get download  $paquet`   
`rename 's/%3a/:/' *.deb`  
2/ Créer le référenciel    
`dpkg-scanpackages ./ /dev/null | gzip -9c > Packages.gz`    
3/ Configurer le repo local  
```
rm -f /etc/apt/sources.list.d/*
echo "deb [trusted=yes] file:/var/repo-local ./" > /etc/apt/sources.list
apt-get update
```


**Répertoires à connaitre**  
Archive des .deb téléchargé avec apt-get install  
`/var/cache/apt/archives/`  

**Créer un .deb depuis un paquet installé**  
`dpkg-repack gparted`  

**Supprimer et purger un paquet**  
`apt-get autoremove --purge   
`
  