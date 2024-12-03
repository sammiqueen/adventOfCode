#! /usr/bin/python3

import sys

def similarityChecker(IDs):

    similarityScore = 0
    for id in IDs[0]:
        frequency = 0
        for i in range(len(IDs[1])):
            if(IDs[1][i] == id):
                frequency = frequency + 1
        similarityScore = similarityScore + (id * frequency)
        print("similarity score = ", similarityScore, "+", id, "*", frequency)
        print(similarityScore)
    
    return similarityScore

firstID = []
secondID = []

i = 0
for line in sys.stdin:
    firstID.append(int(line[:5]))
    secondID.append(int(line[-6:]))
    i = i + 1

IDs = [firstID, secondID]
print(IDs)

similarityScore = similarityChecker(IDs)