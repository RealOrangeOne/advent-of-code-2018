from collections import Counter

with open('data.txt', 'r') as f:
    ids = [id.strip() for id in f.readlines()]

accumulator = []

for id in ids:
    accumulator.extend(set(Counter(id).values()))

print(accumulator.count(2) * accumulator.count(3))

seen = set()

for id in ids:
    for checking_id in ids:
        different = 0
        for char1, char2 in zip(id, checking_id):
            if char1 != char2:
                different += 1
        if different != 1:
            continue
        common_letters = "".join([c for c in checking_id if c in id])
        if common_letters in seen:
            print(common_letters)
        seen.add(common_letters)
