with open('data.txt', 'r') as f:
    frequencies = [int(line.strip()) for line in f.readlines()]

print(sum(frequencies))

current_frequency = 0
seen_frequencies = [current_frequency]
for i in range(9999):
    for frequency in frequencies:
        current_frequency += frequency
        if current_frequency in seen_frequencies:
            print(current_frequency)
            exit()
        seen_frequencies.append(current_frequency)
    print('pass {} {}'.format(i, current_frequency))
