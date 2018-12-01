with open('data.txt', 'r') as f:
    data = [int(line.strip()) for line in f.readlines()]

print(sum(data))
