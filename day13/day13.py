import re
from sympy import symbols, Eq, solve


def read(filename):
    with open(filename, 'r') as file:
        return file.read()




def one_star(text):
    games = text.strip().split("\n\n")
    acc = 0
    for game in games:

        matches = re.findall(r'X[\+=](\d+)|Y[\+=](\d+)', game)
        numbers = [int(num) for tuple in matches for num in tuple if num]
        A = [numbers[0],numbers[1]]
        B = [numbers[2],numbers[3]]
        R = [numbers[4],numbers[5]]

        cA= R[0] // A[0]
        cB = 0


        while cA > 0:
            if cA*A[0] + cB*B[0] == R[0] and cA*A[1] + cB*B[1] == R[1]:
                acc += cA*3+cB
            cB+=1
            while cA*A[0] + cB*B[0] > R[0]:
                cA-=1


    return acc


def two_star(text):
    games = text.strip().split("\n\n")
    acc = 0
    for game in games:
        matches = re.findall(r'X[\+=](\d+)|Y[\+=](\d+)', game)
        numbers = [int(num) for tuple in matches for num in tuple if num]
        A = [numbers[0], numbers[1]]
        B = [numbers[2], numbers[3]]
        R = [numbers[4]+10000000000000, numbers[5]+10000000000000]



        x, y = symbols('x,y')

        eq1 = Eq((A[0]*x + B[0]*y), R[0])
        eq2 = Eq((A[1]*x + B[1]*y), R[1])

        res = solve((eq1, eq2), (x, y))
        if float(res[x]).is_integer() and float(res[y]).is_integer():
            acc += res[x]*3+res[y]

    return acc

text = read('input.txt')
print(two_star(text))