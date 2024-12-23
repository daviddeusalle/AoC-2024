import re
import copy

A, B, C, *combo = list(map(int, re.findall(r'\d+', open('input.txt').read())))


def one_star(A):
    global B, C
    IP = 0
    output = []
    while IP < len(combo):
        opcode = combo[IP]
        operand = combo[IP+1]
        val = 0
        if operand <= 3:
            val = operand
        elif operand == 4:
            val = A
        elif operand == 5:
            val = B
        elif operand == 6:
            val = C

        if opcode == 0:
            A = A // (2**val)
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = val % 8
        elif opcode == 3:
            if A != 0:
                IP = operand
                continue
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            output.append(val%8)
        elif opcode == 6:
            B = A // (2**val)
        elif opcode == 7:
            C = A // (2**val)
        IP += 2
    return output


def two_star(a, i):
    if one_star(a) == combo: print(a)
    if one_star(a) == combo[-i:] or not i:
        for n in range(8): two_star(8*a+n, i+1)







print(",".join(map(str, one_star(A))))
two_star(0,0)