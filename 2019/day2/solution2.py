#!/usr/bin/python
from itertools import product

for noun, verb in product(range(0, 100), range(0, 100)):
    with open('input.txt', 'r') as f:
        code = f.read().split(',')

    # Convert em to ints, instead of strings
    code = [int(i) for i in code]

    code[1] = noun
    code[2] = verb

    for i in range(0, len(code)-1, 4):
        opcodeOne = code[i]
        opcodeTwo = code[i+1]
        opcodeThree = code[i+2]
        opcodeFour = code[i+3]
        if opcodeOne == 1:
            code[opcodeFour] = code[opcodeTwo] + code[opcodeThree]
        elif opcodeOne == 2:
            code[opcodeFour] = code[opcodeTwo] * code[opcodeThree]
        elif opcodeOne == 99:
            break
    if code[0] == 19690720:
        print("Opcodes:", noun, verb, "produce result:", code[0])
        result = 100 * noun + verb
        print("Result is:", result)
        break
