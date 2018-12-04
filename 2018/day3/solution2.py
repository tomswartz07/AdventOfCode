#!/usr/bin/python

with open('input.txt', 'r') as f:
    data = f.read().rstrip('\n').splitlines()

fabric = [list('0'*1000) for i in range(1000)]

def get_x_y_w_h(line):
    _, _, coord, dim = line.split()
    x, y = map(int, coord[:-1].split(','))
    w, h = map(int, dim.split('x'))
    return x, y, w, h

for line in data:
    x, y, w, h = get_x_y_w_h(line)
    for row in range(h):
        for col in range(w):
            fabric[y+row][x+col] = int(fabric[y+row][x+col]) + 1

for line in data:
    x, y, w, h = get_x_y_w_h(line)
    failed = False
    for row in range(h):
        for col in range(w):
            try:
                if fabric[y+row][x+col] != 1:
                    failed = True
                    #print(fabric[y+row][x+col])
                    #print("Trying {}:{}: Failed? {}".format(row, col, failed))
            except IndexError:
                failed = True
    if not failed:
        print(line.split()[0])
