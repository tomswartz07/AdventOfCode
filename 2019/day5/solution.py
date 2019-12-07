#!/usr/bin/python
"Advent of Code Day 5, Part 1"

with open('input.txt', 'r') as f:
    code = f.read().split(',')

# Convert em to ints, instead of strings
code = [int(i) for i in code]

def intcodeArray(int1):
    "Function to return array representing intcode"
    intcode = list(str(int1))
    if len(intcode) < 5:
        for _ in range(5 - len(intcode)):
            intcode.insert(0, "0")
    intcode = [int(i) for i in intcode]
    return intcode

def value(mode, position):
    "Function  to return the value of a position given the mode"
    val = 0
    if mode == 0:
        val = code[code[position]]
    else:
        val = code[position]
    return val

pos = 0

while code[pos] != 99:
    inst = intcodeArray(code[pos])

    # Add em up
    if inst[4] == 1:
        opcodeTwo = pos + 1
        opcodeThree = pos + 2
        opcodeFour = code[pos+3]

        code[opcodeFour] = value(inst[2], opcodeTwo) + value(inst[1], opcodeThree)
        pos += 4

    # Multiply em up
    elif inst[4] == 2:
        opcodeTwo = pos + 1
        opcodeThree = pos + 2
        opcodeFour = code[pos+3]

        code[opcodeFour] = value(inst[2], opcodeTwo) * value(inst[1], opcodeThree)
        pos += 4

    elif inst[4] == 3:
        choice = int(input("What is the input instruction? "))

        if inst[2] == 0:
            code[code[pos+1]] = choice
        else:
            code[pos+1] = choice
        pos += 2

    # Print an output value
    elif inst[4] == 4:
        print(value(inst[2], (pos+1)))
        pos += 2
