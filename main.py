import game
import random

all_words = game.load_words()

longest_words = max(len(word) for word in all_words)
shortest_words = min(len(word) for word in all_words)

long_mot = int(input(
    f"Longueur du mot souhaité "
    f"(minimum : {shortest_words}, maximum : {longest_words}) : "
))

if long_mot < shortest_words or long_mot > longest_words:
    long_mot = random.randint(shortest_words, longest_words)