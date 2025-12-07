import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")

with open(file_path, "r") as f:
    lines = f.readlines()

def colHasDigits(col, matrix):
    m = len(matrix)
    for row in range(m):
        if matrix[row][col].isnumeric():
            return True
    return False

def multiplyVals(arr):
    mult = 1
    for val in arr:
        mult *= int(val)
    return mult

def addVals(arr):
    return sum(int(val) for val in arr)

def getSign(col, matrix):
    m = len(matrix)
    sign = matrix[m-1][col]
    return sign

def removeWhitespace(line):
    newLine = []
    for val in line:
        val = val.strip()
        if val.isnumeric() or val == "+" or val =="*":
            newLine.append(val)
    return newLine

def solveFirst(lines):
    newLines = []
    for line in lines:
        newLine = line.split(" ")
        newLines.append(removeWhitespace(newLine))
    m,n = len(newLines), len(newLines[0])

    total = 0
    for col in range(n):
        thisCol = []
        for row in range(m-1):
            thisCol.append(newLines[row][col])
        sign = newLines[m-1][col]
        if sign == "+":
            total += addVals(thisCol)
        elif sign == "*":
            total += multiplyVals(thisCol)
    return total

print(f"First Problem: {solveFirst(lines)}")


def createNum(col, matrix):
    m = len(matrix)
    num = []
    for i in range(m-1):
        num.append(matrix[i][col])
    return "".join(num)

def solveSecond(lines):
    n = len(lines[0])
    curVals = []
    sign = ""
    total = 0
    for col in range(n):
        hasDigits = colHasDigits(col, lines)
        if not hasDigits:
            if sign == '+':
                total += addVals(curVals)
            elif sign == '*':
                total += multiplyVals(curVals)
            curVals = []
            continue
        if not curVals:
            sign = getSign(col, lines)
        newNum = createNum(col, lines)
        curVals.append(newNum)

    if sign == '+':
        total += addVals(curVals)
    elif sign == '*':
        total += multiplyVals(curVals)
    return total

print(f"Second Problem: {solveSecond(lines)}")