# Ansible  

## Commandes pratiques  
**`ansible-lint playbook.yaml:`** Vérifier leur conformité aux bonnes pratiques et aux standards de codage   
**`ansible playbook.yaml --syntax-check:`** Check syntaxe  
**`ansible-doc:`** information sur les modules  
**`ansible-inventory --list -i hosts`:** Afficher la liste des hosts  
**`ansible all -m ping:`** Test la connectivité

## Ansible Galaxy   
Plateforme pour partager, découvrir et télécharger des collections, rôles, et plugins Ansible créés par la communauté et les éditeurs.  
**`ansible-galaxy init rolename:`** Créer l'arborescence pour un nouveau role rolename  
**`ansible-galaxy install rolename:`** Installer un role (dans /etc/ansible/roles/rolename)  
**`ansible-galaxy install rolename -p /chemin:`** Installer role dans /chemin/rolename
**`ansible-galaxy list:`** Afficher les rôles téléchargés

## Handlers  
Les **handlers** dans Ansible sont des tâches spéciales exécutées uniquement lorsqu'elles sont "notifiées" par d'autres tâches  
<details><summary>Exemple</summary>  
```
tasks:  
  - name: Update configuration file  
    copy:  
      src: config.cfg  
      dest: /etc/myapp/config.cfg  
    notify: Restart myapp  
    
handlers:  
  - name: Restart myapp  
    service:  
      name: myapp  
      state: restarted  
```
</details>  
