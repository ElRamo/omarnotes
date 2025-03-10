# Python  

## Définitions  
### Module   
Un seul fichier `.py` contenant du code (fonctions, variables, classes). Exemple : `math_utils.py`.  
```
# math_utils.py
def addition(a, b):
    return a + b
Vous pouvez l'utiliser dans un autre fichier comme ceci :
import math_utils

result = math_utils.addition(2, 3)
print(result)  # Affiche 5
```

### Bibliothèque (Library)    
Un ensemble de modules regroupés pour une fonctionnalité spécifique. Par exemple, `requests` est une bibliothèque pour les requêtes HTTP qui contient plusieurs modules internes.  
```
import requests

response = requests.get('https://example.com') # Utilise le module get de la lib request
print(response.status_code)
```

### Package  
Un dossier contenant plusieurs modules et un fichier `__init__.py`. C'est une façon d'organiser des modules liés.

```
mon_package/
│
├── __init__.py       # Indique que c'est un package
├── module1.py
└── module2.py
On importe alors avec
from mon_package import module1
```

### Fonction vs Méthode    
- **Fonction** = Indépendante, définie en dehors d'une classe.
- **Méthode** = Fonction liée à une classe/objet, définie **à l'intérieur** de la classe.
### Résumé  
- **Librairie** = Plusieurs **modules** (fichiers `.py`) regroupés pour fournir des fonctionnalités spécifiques.  
- **Module** = Un **fichier `.py`** qui contient des **classes**, des **fonctions** et des **variables**.  
- **Classe** = Un **plan** (blueprint) pour créer des objets, contenant plusieurs **méthodes** et **attributs**.  
- **Méthode** = Une **fonction** définie à l'intérieur d'une classe qui décrit le comportement des objets de cette classe.  

## Librairies  

- **Bibliothèques standard** : La documentation officielle de Python [https://docs.python.org/3/library/](https://docs.python.org/3/library/).
- **PyPI (Python Package Index)** : Un dépôt de bibliothèques tierces que vous pouvez installer avec `pip`. Visitez [https://pypi.org/](https://pypi.org/) pour explorer les bibliothèques disponibles.
## Classes et méthodes  


```
# Définition de la classe Chien
class Chien:
    def aboyer(self):
        return "Woof!"  # Méthode qui retourne le son que fait le chien
    
    def manger(self):
        return "Le chien mange."  # Méthode qui décrit l'action de manger
    
    def jouer(self):
        return "Le chien joue."  # Méthode qui décrit l'action de jouer

# Création d'une instance de la classe Chien
mon_chien = Chien()

# Appel des méthodes de l'instance
print(mon_chien.aboyer())  # Affiche "Woof!"
print(mon_chien.manger())   # Affiche "Le chien mange."
print(mon_chien.jouer())    # Affiche "Le chien joue."
```

