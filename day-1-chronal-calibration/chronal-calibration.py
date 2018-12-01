with open('data.txt', 'r') as f:
    frequencies = [int(line.strip()) for line in f.readlines()]

print(sum(frequencies))

current_frequency = 0
seen_frequencies = {current_frequency}
count = 0

while True:
    for frequency in frequencies:
        current_frequency += frequency
        if current_frequency in seen_frequencies:
            print(current_frequency)
            exit()
        seen_frequencies.add(current_frequency)
    count += 1
    print('pass {} {}'.format(count, current_frequency))
