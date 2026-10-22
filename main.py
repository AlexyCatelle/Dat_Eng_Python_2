# Récupérer la liste de mots
with open("mots.txt", "r", encoding="utf-8") as file:
    all_words = [line.strip().lower() for line in file]

print(len(all_words))

# Possibilité de choisir sa longeur de mots, par défaut 5.

# filtrer liste selon longueur définie par le joueur

# choisir un mot aléatoire dans la liste filtrée par longueur

# Liste qui stock les lettres tentées bien placée et leur index (vert)

# Liste qui stock les lettres trouvées mais mal placée (orange)

# Liste qui stock les lettres tentées et absentes (noir)

# Boucle tentative pour max 6:
    # Demander un mot au joueur
    # Vérifier la longueur du mot proposer par le joueur
        # Si bonne longueur :
            # augmente le compteur de 1

        # vérifier si le mot est le bon
            # si bon : terminé victoire 

        # si différent :
            # Split les mots cible (array_1) et tentative(array_2) pour stocker en tableau

                # bouble pour comparer chaque index des deux tableaux

        # Si mauvaise longueur alors retour demander un mot avec message d'erreur

