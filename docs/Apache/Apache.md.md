# Apache  
## Script connection htaccess  
```
if [ -z "$user" ]; then
    echo -n 'LDAP User > '
    read user
fi

if [ -z "$password" ]; then
    echo -n 'LDAP Password > '
    read -s password
    echo
fi

curl -u "$user:$password" -k 'http://mywebsite/deleteme.php'

```  
## Call php  
vim test.php  
`<?php sleep(600);>`  
curl http://vhost/test.php  
