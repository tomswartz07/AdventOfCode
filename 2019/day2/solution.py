#!/usr/bin/python

with open('input.txt', 'r') as f:
    code = f.read().split(',')

# Convert em to ints, instead of strings
for i in range(len(code)):
    code[i] = int(code[i])

code[1] = 12
code[2] = 2

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
print("Result:", code[0])
