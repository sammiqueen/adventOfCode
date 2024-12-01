#! /usr/bin/python3

import sys

def listSorter(unsortedList):

    sortedList = []
    
    for i in range(len(unsortedList[1])):
        
        firstValue = min(unsortedList[0])
        unsortedList[0].remove(firstValue)

        secondValue = min(unsortedList[1])
        unsortedList[1].remove(secondValue)

        sortedList.append([firstValue, secondValue, (abs(firstValue - secondValue))])

    return(sortedList)

def diffCounter(sortedList):

    diff = 0

    for i in range (len(sortedList)):
        diff = diff + sortedList[i][2]

    return(diff)

firstID = []
secondID = []

i = 0
for line in sys.stdin:
    print(line)
    firstID.append(int(line[:5]))
    secondID.append(int(line[-6:]))
    print(firstID[i],secondID[i])
    i = i + 1

unsortedList = [firstID,secondID]

sortedList = listSorter(unsortedList)
print(sortedList)
print(diffCounter(sortedList))