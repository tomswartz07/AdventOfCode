#!/usr/bin/python
"Advent of Code Day 5, Part 1"

with open('input.txt', 'r') as f:
    orbits = f.read().split('\n')
orbits = filter(None, orbits)
print(orbits)

orbits = [i.split(")") for i in orbits]
#print(orbits)

list1 = []

for x in range(len(orbits)):
    for y in range(len(orbits[x])):
        list1.append(orbits[x][y])

#planets is a list of all planets, with no duplicates
planets = list(set(list1))

for i in range(len(planets)-1):     #delete COM from planets
    if planets[i] == "COM":
        print("Removing:", i, planets[i])
        del planets[i]

def findOrbits(orbitArray, world, count):
    """
    #recursive function to find and count all direct and indirect orbits of a given planet,
    #going backwards
    """
    for j in orbitArray:

        localCount = count
        endCheck = j[0]
        worldCheck = j[1]

        if worldCheck == world:
            if endCheck != "COM":
                localCount += 1
                returnValue = findOrbits(orbitArray, endCheck, localCount)
            else:
                localCount += 1
                returnValue = localCount

    return returnValue

def clearChecks(orbitArray):
    "Clear orbit checks"
    for j in orbitArray:
        j[2] = 0

#total count of all direct and indirect orbits
orbitCount = 0

#loop to find and count all orbits of every planet
for z in planets:
    number = findOrbits(orbits, z, 0)
    orbitCount += number

#print the resulting orbit count
print("The total direct and indirect orbits is " + str(orbitCount))
