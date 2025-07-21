import pandas as pd

# Chemin vers ton fichier Excel
input_file = r"C:\Users\oelallali\Documents\Sommaire.xlsx"
output_file = "Git\Git.md"

# Lire les données de la feuille 'git'
df = pd.read_excel(input_file, sheet_name='git')

# Vérifier les noms des colonnes pour s'assurer qu'ils sont bien définis
print("Colonnes disponibles :", df.columns)

# Convertir le DataFrame en Markdown manuellement
with open(output_file, "w", encoding="utf-8") as f:
    # Ajouter un titre pour la section Git
    f.write("# Git - Commandes et Notes\n\n")
    
    # Parcourir chaque ligne et convertir en format Markdown
    for index, row in df.iterrows():
        # Accéder à la seule colonne 'Git stash'
        command = str(row[0])  # Convertir la valeur en chaîne (string)
        
        # Ajouter une description ou un texte par défaut si nécessaire
        description = "Description de la commande : " + command  # Remplacer par la logique de description
        
        # Ajouter la commande et la description au fichier markdown
        f.write(f"### {command}\n\n{description}\n\n")

print(f"Le fichier Markdown a été créé : {output_file}")
