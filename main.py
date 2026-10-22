from termcolor import colored
import random
# Récupérer la liste de mots
with open("mots.txt", "r", encoding="utf-8") as file:
    all_words = [line.strip() for line in file]

longest_words = max(len(word) for word in all_words)
shortest_words = min(len(word) for word in all_words)

# Possibilité de choisir sa longeur de mots, par défaut 5.
long_mot = int(input(f'Longueur du mot souhaité (minimum : {shortest_words}, maximum : {longest_words}):'))


# Si valeur ne respecte pas les bornes alors choisi une longueur aléatoire entre les bornes :
if long_mot < shortest_words or long_mot > longest_words :
    long_mot = random.randint(shortest_words, longest_words)
    print(f'valeur incorrecte ! je décide moi-même ! ça sera : {long_mot}')

# filtrer liste selon longueur définie par le joueur

flitred_words = [word for word in all_words if len(word) == long_mot]

# choisir un mot aléatoire dans la liste filtrée par longueur
cible = random.choice(flitred_words)
print(cible)
liste_cible = list(cible)
dict_lettres = {"green":[],"red" :[], "light_grey" : []}


# Fonction affichage avec les couleurs
def affichage (liste):
        #print(f'liste : {liste}')
    res = ""
    for c in liste :
         #print(f'c : {c}')
            #print(f'c 0 : {c[0]}')
            #print(f'c 1 : {c[1]}')

        res += f'{colored(c[0],c[1])}'
        #print( f'res update : {res}')
    return res


# Boucle tentative pour max 6:
nb_tentative = 0
winner = False

while nb_tentative < 6 and not winner :
    # Demander un mot au joueur
    while True :
        tentative = input("What is your word: ").upper()
        
        # Vérifier que alpha
        if not tentative.isalpha():
            print(" Ne doit contenir que des lettres")
    
        # Vérifie la longueur du mot tentative    
        elif len(tentative) != long_mot:
            print(f'Your word should be {long_mot} characters')
        
        else:
            break;

    # vérifier si le mot est le bon
    if tentative == cible :
            # si bon : terminé victoire
        winner = True
        print("Vous avez gagnez !")


    # si différent :
    # Split le mot tentativepour stocker en tableau
    liste_tentative = list(tentative)
    liste_affichage = []

# boucle pour comparer chaque index des deux tableaux
    for i in range ((len(tentative))) :

        #Si lettre correcte et bien placée : Stock dans vert
        if liste_tentative[i] == liste_cible[i] :
            liste_affichage.append([liste_tentative[i],"green"])
            dict_lettres["green"].append([liste_tentative[i],i])


        # Si lettre correcte mais mal placé : Stock dans rouge
        elif liste_tentative[i] in liste_cible :
            liste_affichage.append([liste_tentative[i],"red"])
            dict_lettres["red"].append([liste_tentative[i],i])
    
        #Si lettre incorrecte : Stock dans noir
        else :
            liste_affichage.append([liste_tentative[i],"light_grey"])
            dict_lettres["light_grey"].append([liste_tentative[i],i])

    # Affichage résultat
    print(affichage(liste_affichage))


