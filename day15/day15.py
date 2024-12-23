def read(filename):
    with open(filename, 'r') as file:
        return file.read()

def one_star(input):
    parts = input.strip().split("\n\n")
    print(parts[0])
    return None

text = read('input.txt')
print(one_star(text))
