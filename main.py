from termcolor import colored
# Récupérer la liste de mots
with open("mots.txt", "r", encoding="utf-8") as file:
    all_words = [line.strip().lower() for line in file]

#print(len(all_words))

#print(colored('hello', 'red'), colored('world', 'green'))



# Possibilité de choisir sa longeur de mots, par défaut 5.

# filtrer liste selon longueur définie par le joueur

# choisir un mot aléatoire dans la liste filtrée par longueur
cible = "tiret"
tentative = "texte"

liste_tentative = list(tentative)
liste_cible = list(cible)

# Liste qui stock les lettres tentées bien placée et leur index (vert)

# Liste qui stock les lettres trouvées mais mal placée et leur index (orange)

# Liste qui stock les lettres tentées et absentes (noir)

# Boucle tentative pour max 6:
    # Demander un mot au joueur
    # Vérifier que alpha
        #Si oui continue

        #Si non = Erreur et redemande un mot

    # Vérifier la longueur du mot proposer par le joueur
        # Si bonne longueur :
            # augmente le compteur de 1

        # vérifier si le mot est le bon
            # si bon : terminé victoire 
        # si différent :
            # Split les mots cible (array_1) et tentative(array_2) pour stocker en tableau
liste_tentative = list(tentative)
liste_cible = list(cible)
liste_affichage = []
dict_lettres = {"green":[],"red" :[], "light_grey" : []}          

                # boucle pour comparer chaque index des deux tableaux

for i in range ((len(tentative))) :
    #Si lettre correcte et bien placée
    if liste_tentative[i] == liste_cible[i] :
        liste_affichage.append([liste_tentative[i],"green"])
        dict_lettres["green"].append([liste_tentative[i],i])

    elif liste_tentative[i] in liste_cible :
        liste_affichage.append([liste_tentative[i],"red"])
        dict_lettres["red"].append([liste_tentative[i],i])

    else :
        liste_affichage.append([liste_tentative[i],"light_grey"])
        dict_lettres["light_grey"].append([liste_tentative[i],i])

def affichage (liste):
    res = ""
    for c in liste :
        res += f'{colored(c[0],c[1])}'
    return res

print(liste_cible)
print(affichage(liste_affichage))
print(dict_lettres)
    

                    # tant qu'il reste des lettres a vérifier 
                        
                            # Stock dans la liste verte
                            #continue
                        # Si lettre correcte mais mal placé
                            # Stock dans orange
                            # continue
                        #Si lettre incorrecte
                            # Stock dans noir
                            # Continue

                # Affichage résultat
                    #
                #(rendu) Si lettre ni verte ni orange alors noires

        # Si mauvaise longueur alors retour demander un mot avec message d'erreur

