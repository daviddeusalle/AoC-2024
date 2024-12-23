import re

codes = [code.strip() for code in open('input.txt').readlines()]
print(codes)
keypad = {'7':(0,0), '8':(0,1), '9':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '1':(2,0), '2':(2,1),'3':(2,2),'0':(3,1), 'A':(3,2) }

directional= {'^': (0,1), 'A': (0,2), '<': (1,0), 'v': (1,1), '>': (1,2)}

def calculate(dir1, dir2):
    return dir1[0] - dir2[0], dir1[1] - dir2[1]

def get_new_directions(dx, dy):
    directions = []
    if dx < 0:
        directions.extend('^'*-dx)
    else:
        directions.extend('v'*dx)
    if dy < 0:
        directions.extend('<'*-dy)
    else:
        directions.extend('>'*dy)

    directions.extend('A')
    return directions
# keys represent arrows and numbers
def get_directions(keys, pad, pos):

    directions = []
    for key in keys:
        new_pos = pad[key]
        dx, dy = calculate(new_pos, pos)
        directions.extend(get_new_directions(dx,dy, pos))

        pos = new_pos
    return directions

def typing():
    acc = 0
    pos_keypad = (3, 2)
    dir1 = (0,2)
    dir2 = (0,2)
    for code in codes:
        print(code)
        directions1 = get_directions(code, keypad, pos_keypad)
        directions2 = get_directions(directions1, directional, dir1)
        print(directions2)
        directions3 = get_directions(directions2, directional, dir2)
        print((directions3))
        print(len(directions3))

typing()
