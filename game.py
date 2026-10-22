from termcolor import colored
import random

# Récupérer la liste de mots
def load_words():
    with open("mots.txt", "r", encoding="utf-8") as file:
        all_words = [line.strip().upper() for line in file]
    return all_words

# Choisir un mot aléatoirement dans la liste en fonction de la taille
def choose_word(words, length):
    filtered_words = [
        word for word in words
        if len(word) == length
    ]

    return random.choice(filtered_words)

# Check_letters()
def check_letters(attempt, target):
    result = []

    for i in range(len(attempt)):
        if attempt[i] == target[i]:
            result.append("green")
        elif attempt[i] in target:
            result.append("yellow")
        else:
            result.append("grey")

    return result


# Vérifie si le mot est le bon
def is_winner(attempt, target) :
     if attempt == target :
        return True

def validate_word(attempt, length):
    if not attempt.isalpha():
        return False, "Ne doit contenir que des lettres"

    elif len(attempt) != length:
        return False, f"Your word should be {length} characters"

    return True, ""