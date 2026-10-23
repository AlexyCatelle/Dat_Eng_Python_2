import game
import selection
import interface
import result


def main():
    # Récupérer la liste de mot complete
    all_words = game.load_words()

    if not all_words:
        raise ValueError("Le fichier mots.txt est vide.")
    
    # Récupérer les tailles de mots disponibles
    available_lengths = game.get_availables_lengths(all_words)

    while True:
        # Ecran de selection de la taille du mot
        word_length = selection.run(available_lengths)

        if word_length is None:
            break

        # Vérifier qu'il existe des mots pour cette longueur
        words_of_length = [
            word for word in all_words
            if len(word) == word_length
        ]

        if not words_of_length:
            print(
                f"Aucun mot de {word_length} lettres dans le dictionnaire."
            )
            continue

        # Choisir le mot secret
        target = game.choose_word(all_words, word_length)
        print(target)

        # Lancer la partie
        game_result = interface.run(word_length, target)

        if game_result == "quit":
            break

        # Afficher le résultat
        choice = result.run(game_result, target)

        if choice != "replay":
            break


if __name__ == "__main__":
    main()
