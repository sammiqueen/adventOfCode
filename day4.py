#! /usr/bin/python3

import sys

def matrixChecker(inputLines):

    xmasAmnt = 0
    totAmnt = 0

    for y in range(len(inputLines)):
        for x in range(len(inputLines[y])):
            if inputLines[y][x] == "X":
                
                amntHorizontal = horChecker(inputLines[y],x)

                amntVertical = verChecker(inputLines,x,y)

                amntDiagRising = diagRisingChecker(inputLines,x,y)

                amntDiagFalling = diagFallingChecker(inputLines,x,y)

                totAmnt = totAmnt + amntHorizontal + amntVertical + amntDiagRising + amntDiagFalling

    return xmasAmnt

def horChecker(line, x):

    for i in range(len(line)):
        try:
            if
        try:
            
        except Exception:
            pass

    return amntHorizontal
    
def verChecker(inputLines, x, y):

    return amntVertical
    
def diagRisingChecker(inputLines, x, y):

    return amntDiagRising
    
def diagFallingChecker(inputLines, x, y):
        
    return amntDiagFalling

inputLines=[]
for line in sys.stdin:
    inputLines.append(line.replace("\n",""))

print(inputLines)

xmasAmnt = matrixChecker(inputLines)