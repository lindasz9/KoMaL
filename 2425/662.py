import random

def hash(word, nm):
    number = sum(ord(i) for i in word)
    number = number ** 2
    return number % nm

n, m = map(int, input().split())

table = ["——" for i in range(n + m)]

with open("word5000.txt", "r") as file:
    words = [i.strip() for i in file]

n_words = random.sample(words, n)

T, L = 0, n
for i in n_words:
    index = hash(i, n + m)
    if table[index] != "——":
        T += 1
    while table[index] != "——":
        index = (index + 1) % (n + m)
        L += 1
    table[index] = i

with open("hashtab.txt", "w", encoding="utf-8") as file:
    for i in table:
        file.write(f"{i}\n")

print(T, L)