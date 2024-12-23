numbers = [int(numbers.strip()) for numbers in open('input.txt').readlines()]

def sequence(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

def solve():
    part1, part2 = 0, 0
    unique_sequences = set()
    all_sequences = []

    for number in numbers:
        prices = [number % 10]
        price_diff = []
        numbers_diff = {}
        for i in range(2000):

            number = sequence(number)
            price = number % 10
            prices.append(price)
            price_diff.append(prices[-1] - prices[-2])
            if i > 2:
                # Generate sequence of prices
                seq = tuple(price_diff[-4:])

                if seq not in unique_sequences:
                    unique_sequences.add(seq)

                if seq not in numbers_diff:
                    numbers_diff[seq] = prices[-1]

        all_sequences.append(numbers_diff)
        part1 += number
    for unique_sequence in unique_sequences:
        acc = 0
        for seq in all_sequences:
            if unique_sequence in seq:
                acc+= seq[unique_sequence]
        if acc > part2:
            part2 = acc

    return part1, part2

part1, part2 = solve()
print("Part 1: ", part1)
print("Part 2: ", part2)
