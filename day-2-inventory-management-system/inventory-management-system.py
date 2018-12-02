from collections import Counter

with open('data.txt', 'r') as f:
    ids = [id.strip() for id in f.readlines()]

accumulator = {}

for id in ids:
    id_counter = Counter(list(id))
    counts = set(id_counter.values())
    for letter_count in counts:
        if letter_count not in accumulator:
            accumulator[letter_count] = 0
        accumulator[letter_count] += 1

print(accumulator[2] * accumulator[3])
