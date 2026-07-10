#simple hash function by modulo
#simple of D

def simple_hash(key, size):
    total = 0
    for char in key:
        total += ord(char)
    return total % size


size = 10
words = ["apple", "banana", "cherry", "date"]

for word in words:
    index = simple_hash(word, size)
    print(f"'{word}' → {index}")

for i in range(10):
    print('-', end=' ')


#hash in python

size = 10

words = ["apple", "banana", "cherry", "date"]

for word in words:
    index = hash(word) % size
    print(f"'{word}' → hash = {hash(word)}, index = {index}")