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

# Check_Word()

# Vérifie si le mot est le bon
def is_winner(attempt, target) :

