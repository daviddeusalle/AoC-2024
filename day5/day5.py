def read(filename):
    with open(filename, 'r') as file:
        return file.read()


def one_star(lines):
    sum = 0
    parts = lines.split("\n\n")
    rules_part = parts[0].split("\n")
    updates_part = parts[1].strip().split("\n")
    rules = {}
    for rule_part in rules_part:
        numbers = rule_part.split("|")
        if numbers[0] not in rules:
            rules[numbers[0]] = []
        rules[numbers[0]].append(numbers[1])
    for updates in updates_part:
        numbers = updates.split(",")
        acc = 0
        for index, page in enumerate(numbers):
            if page not in rules:
                continue
            illegals = [x for x in numbers[:index] if x in rules[page]]
            acc += len(illegals)
        if acc == 0:
            sum += int(numbers[int(len(numbers)/2)])
    return sum

def two_star(lines):
    sum = 0
    parts = lines.split("\n\n")
    rules_part = parts[0].split("\n")
    updates_part = parts[1].strip().split("\n")
    rules = {}
    for rule_part in rules_part:
        numbers = rule_part.split("|")
        if numbers[0] not in rules:
            rules[numbers[0]] = []
        rules[numbers[0]].append(numbers[1])
    for updates in updates_part:
        numbers = updates.split(",")
        acc = 0
        for index, page in enumerate(numbers):
            if page not in rules:
                continue
            illegals = [x for x in numbers[:index] if x in rules[page]]
            acc += len(illegals)

        if acc > 0:
            new_list = []
            for number in numbers:
                if new_list == []:
                    new_list.append(number)
                    continue
                if number not in rules:
                    new_list.append(number)
                    continue
                i = 0
                while i < len(new_list):
                    if new_list[i] in rules[number]:
                        new_list.insert(i, number)
                        break

                    i+=1
                if i == len(new_list):
                    new_list.append(number)

            sum += int(new_list[int(len(new_list)/2)])
    return sum

text = read('input.txt')
print(two_star(text))
