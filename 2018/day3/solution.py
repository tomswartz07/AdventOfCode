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

overlap = 0
for strip in fabric:
    # they use freedom units, ugh
    for inch in strip:
        if int(inch) >= 2:
            overlap += 1
print(overlap)

#print(values)
#v = 0
#claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), values)
#for (claim_number, start_x, start_y, width, height) in claims:
#    squares = lambda c: ((i, j) for i in range(start_x, start_x+width)
#                         for j in range(start_y, start_y+height))
#    fabric = Counter(s for c in values for s in squares(c))
#    print("Claim {}: x: {} y: {} {}x{}".format(claim_number, start_x, start_y, width, height))
#    #print(fabric)
#    print(sum(1 for v in fabric.values() if v > 1))

