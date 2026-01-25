from itertools import *

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

with open("words.js") as file:
    words = file.readlines()[0].split()[3:-1]
    words[0] = words[0][1:]
    words[-1] = words[-1][:-9]

    words = [(set(word), word) for word in words]

puzzles = {puzzle: sum(len(word) for letters, word in words if letters <= set(puzzle)) for puzzle in combinations(ALPHABET, 7)}

print(*sorted(puzzles.items(), key=lambda t: t[1])[:100], sep="\n")
