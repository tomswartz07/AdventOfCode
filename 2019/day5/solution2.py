#!/usr/bin/python
"Advent of Code Day 5, Part 2"

with open('input.txt', 'r') as f:
    code = f.read().split(',')

# Convert em to ints, instead of strings
code = [int(i) for i in code]

def intcodeArray(int1):
    "Function to return 5 element array representing the intcode"
    intcode = list(str(int1))
    if len(intcode) < 5:
        for _ in range(5 - len(intcode)):
            intcode.insert(0, "0")
    intcode = [int(i) for i in intcode]
    return intcode

# inst[4] and inst[3] are the opcode
# inst[2] is the mode of the first parameter
# inst[1] is the mode of the second parameter
# inst[0] is the mode of the third parameter

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
        choice = int(input("What is the System ID? "))

        if inst[2] == 0:
            code[code[pos+1]] = choice
        else:
            code[pos+1] = choice
        pos += 2

    # Print an output value
    elif inst[4] == 4:
        print(value(inst[2], (pos+1)))
        pos += 2

    # If first parameter != 0, jump to position given by the second parameter
    elif inst[4] == 5:

        opcodeTwo = pos+1
        opcodeThree = pos+2

        if value(inst[2], opcodeTwo) != 0:
            pos = value(inst[1], opcodeThree)
        else:
            pos += 3

    # If first parameter is zero, jump to position given by the second parameter
    elif inst[4] == 6:

        opcodeTwo = pos+1
        opcodeThree = pos+2

        if value(inst[2], opcodeTwo) == 0:
            pos = value(inst[1], opcodeThree)
        else:
            pos += 3

    # Based on if first parameter < second parameter,
    # Store 1 or 0 in the position given by the third parameter
    elif inst[4] == 7:

        opcodeTwo = pos+1
        opcodeThree = pos+2
        opcodeFour = code[pos+3]

        if value(inst[2], opcodeTwo) < value(inst[1], opcodeThree):
            code[opcodeFour] = 1
        else:
            code[opcodeFour] = 0
        pos += 4

    # Based on if first parameter == second parameter,
    # Store 1 or 1 in the position given by the third parameter.
    elif inst[4] == 8:

        opcodeTwo = pos+1
        opcodeThree = pos+2
        opcodeFour = code[pos+3]

        if value(inst[2], opcodeTwo) == value(inst[1], opcodeThree):
            code[opcodeFour] = 1
        else:
            code[opcodeFour] = 0
        pos += 4
