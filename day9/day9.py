def read(filename):
    with open(filename, 'r') as file:
        return file.read()

def decompress(input):
    text = list(input.strip())
    id = 0
    disk = []
    for index, letter in enumerate(text):
        if index % 2 == 0:
            disk.extend([str(id)] * int(letter))
            id += 1
        else:
            disk.extend(['.'] * int(letter))
    return disk

def one_star(input):
    text = decompress(input)
    l = 0
    r = len(text) -1
    ok = set()
    checksum = 0
    while l < len(text)-1:
        if text[l] != '.':
            ok.add(l)
            checksum += (l * int(text[l]))
        else:
            while text[r] == '.' and r not in ok:
                r-=1
            if l < r:
                text[l], text[r] = text[r], text[l]
                ok.add(l)
                checksum += (l * int(text[l]))
        l+=1
    return checksum

def decompress_part_two(input):
    text = list(input.strip())
    id = 0
    disk = []
    for index, letter in enumerate(text):
        if index % 2 == 0:
            disk.append([str(id)] * int(letter))
            id += 1
        else:
            disk.append(['.'] * int(letter))
    return disk

def two_star(input):
    text = decompress_part_two(input)
    l = 0
    r = len(text) -1
    ok = set()
    checksum = 0

    for i in reversed(range(len(text))):
        if len(text[i]) == 0:
            continue
        if text[i][0] != '.':
            for j in range(len(text)):
                if j > i:
                    break
                if len(text[j]) == 0:
                    continue
                if text[j][0] == '.' and len(text[j]) >= len(text[i]):
                    diff = len(text[j]) - len(text[i])
                    text[j]= text[i].copy()
                    text[i] =  ['.']* len(text[i])
                    text.insert(j +1, ['.']* diff)
                    break

    text = [item for sublist in text for item in sublist]
    for i in range(len(text)):
        if text[i] != '.':
            checksum+= i*int(text[i])

    return checksum


text = read('input.txt')
print(two_star(text))
