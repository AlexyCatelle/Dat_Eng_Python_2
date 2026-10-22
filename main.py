import game
import random

all_words = game.load_words()

longest_words = max(len(word) for word in all_words)
shortest_words = min(len(word) for word in all_words)


nb_tentative = 0
winner = False


long_mot = int(input(
    f"Longueur du mot souhaité "
    f"(minimum : {shortest_words}, maximum : {longest_words}) : "
))

if long_mot < shortest_words or long_mot > longest_words:
    long_mot = random.randint(shortest_words, longest_words)


target = game.choose_word(all_words, long_mot)

print(target)

while nb_tentative < 6 and not winner:

    # Demander un mot jusqu'à ce qu'il soit valide
    while True:
        attempt = input("What is your word: ").upper()

        is_valid, message = game.validate_word(attempt, long_mot)

        if not is_valid:
            print(message)
        else:
            break

    # Une tentative valide consomme un essai
    nb_tentative += 1

    # Vérifier si le joueur a gagné
    if attempt == target:
        winner = True
        print("Vous avez gagné !")
    else:
        # Afficher le résultat de la tentative
        print(game.check_word(attempt, target))

if not winner:
    print(f"Perdu ! Le mot était {target}.")

print(game.check_letters(attempt, target))