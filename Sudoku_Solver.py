#~~~~ Sudoku Solver ~~~~#

import csv, copy, time

################################################ formatting functions ################################################

def formatSudokuGridTo5DFrom2D(gridArray2D,squareSize):
    gridArray5D = []
    for i in range(squareSize):
        tempArray1 = []
        for j in range(squareSize):
            tempArray2 = []
            for k in range(squareSize):
                tempArray3 = []
                for l in range(squareSize):
                    tempArray4 = [int(gridArray2D[3*i+k][3*j+l])]
                    if tempArray4[0] == 0:
                        for m in range(squareSize*squareSize):
                            tempArray4.append(m+1)
                    tempArray3.append(tempArray4)
                tempArray2.append(tempArray3)
            tempArray1.append(tempArray2)
        gridArray5D.append(tempArray1)
    return gridArray5D

def formatSudokuGridTo2DFrom5D(gridArray,squareSize,gridNumber):
    gridArray2D = []
    for i in range(squareSize):
        for j in range(squareSize):
            tempArray1 = []
            for k in range(squareSize):
                for l in range(squareSize):
                    tempArray1.append(gridArray[i][k][j][l][0])
            gridArray2D.append(tempArray1)
    return writeCompletedGridToCSV(gridArray2D,gridNumber)

def print5DSudokuGrid(gridArray,squareSize):
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    if not isinstance(gridArray[i][k][j][l][0],int):
                        print(0,end=' ')
                    else:
                        print(gridArray[i][k][j][l][0],end=' ')
                print("|",end=' ')
            print()
        print("-----------------------")

def writeCompletedGridToCSV(gridArray2D,gridNumber):
    with open("Sudoku_Grid_"+gridNumber+"_Completed.csv","w",newline='') as completedGridFile:
        toWrite = csv.writer(completedGridFile,delimiter=',')
        for row in gridArray2D:
            toWrite.writerow(row)
    print("written to file")

def readIncompleteGridFromCSV(gridNumber):
    with open("Sudoku_Grid_"+gridNumber+".csv","r") as sudokuGrid:
        gridArray2D = list(csv.reader(sudokuGrid))
    squareSize = int(len(gridArray2D[0])**0.5)
    return gridArray2D, squareSize

################################################ searching functions ################################################

def toSumUpTo(squareSize):
    return (((squareSize*squareSize)**2)+squareSize*squareSize)//2

def checkForCompletedAreas(gridArray,squareSize,toSumTo,a,b,c,d):
    rowTotal = 0
    columnTotal = 0
    squareTotal = 0
    for i in range(squareSize):
        for j in range(squareSize):
            rowTotal += gridArray[a][i][c][j][0]
            columnTotal += gridArray[i][b][j][d][0]
            squareTotal += gridArray[a][b][i][j][0]
    if rowTotal + columnTotal + squareTotal == toSumTo*3:
        return True
    return False

def checkGridIsCompleted(gridArray,squareSize):
    toSumTo = toSumUpTo(squareSize)
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    if gridArray[i][j][k][l][0] == 0:
                        return False
                    if checkForCompletedAreas(gridArray,squareSize,toSumTo,i,j,k,l) == False:
                        return False
    return True

def findNumbersToRemove(gridArray,squareSize,a,b,c,d):
    numbersToRemove = []
    for i in range(squareSize):
        for j in range(squareSize):
            if gridArray[a][i][c][j][0] != 0:    # row
                numbersToRemove.append(gridArray[a][i][c][j][0])
            if gridArray[i][b][j][d][0] != 0:    # column
                numbersToRemove.append(gridArray[i][b][j][d][0])
            if gridArray[a][b][i][j][0] != 0:    # square
                numbersToRemove.append(gridArray[a][b][i][j][0])
    return numbersToRemove

################################################ solving functions ################################################

def eliminateNotPossibleNums(gridArray,squareSize,a,b,c,d):
    numbersToRemove = findNumbersToRemove(gridArray,squareSize,a,b,c,d)
    for i in range(len(numbersToRemove)):
        try:
            gridArray[a][b][c][d].remove(numbersToRemove[i])
        except ValueError:
            pass
    if len(gridArray[a][b][c][d]) == 1:
        return None
    if len(gridArray[a][b][c][d]) == 2:
        gridArray[a][b][c][d].remove(0)
    return gridArray

def findPossibleGrids(gridArray,squareSize):
    numberOfPossibleGrids = 9
    leastPossibleOptionsPos = []
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    if gridArray[i][j][k][l][0] == 0:
                        if (len(gridArray[i][j][k][l])-1) < numberOfPossibleGrids:
                            numberOfPossibleGrids = len(gridArray[i][j][k][l])
                            leastPossibleOptionsPos = [i,j,k,l]
    if numberOfPossibleGrids == 9:
        return None, None
    a = leastPossibleOptionsPos[0]
    b = leastPossibleOptionsPos[1]
    c = leastPossibleOptionsPos[2]
    d = leastPossibleOptionsPos[3]
    possibleGrids = []
    for i in range(numberOfPossibleGrids-1):
        x = copy.deepcopy(gridArray)
        x[a][b][c][d].remove(0)
        y = x[a][b][c][d][i]
        x[a][b][c][d].clear()
        x[a][b][c][d].append(y)
        possibleGrids.append(x)
    return possibleGrids, numberOfPossibleGrids-1

def solve(gridArray,squareSize):
    finished = checkGridIsCompleted(gridArray,squareSize)
    while not finished:
        notChanged = False
        while not notChanged:
            previousGrid = copy.deepcopy(gridArray)
            for i in range(squareSize):
                for j in range(squareSize):
                    for k in range(squareSize):
                        for l in range(squareSize):
                            if gridArray[i][j][k][l][0] == 0:
                                gridArray = eliminateNotPossibleNums(gridArray,squareSize,i,j,k,l)
                                if gridArray == None:
                                    return None
            finished = checkGridIsCompleted(gridArray,squareSize)
            if finished == True:
                return gridArray
            if gridArray == previousGrid:
                notChanged = True
        possibleGrids, numberOfPossibleGrids = findPossibleGrids(gridArray,squareSize)
        if possibleGrids == None:
            return None
        for i in range(numberOfPossibleGrids):
            gridAttempt = copy.deepcopy(possibleGrids[i])
            gridAttempt = solve(gridAttempt,squareSize)
            if gridAttempt != None:
                return gridAttempt
        return None

def initialiseSolving():
    gridNumber = str(input("enter the grid number >"))
    gridArray2D, squareSize = readIncompleteGridFromCSV(gridNumber)
    gridArray = formatSudokuGridTo5DFrom2D(gridArray2D,squareSize)
    print5DSudokuGrid(gridArray,squareSize)
    startTime = time.time()
    gridArray = solve(gridArray,squareSize)
    finishTime = time.time()
    if gridArray != None:
        print("finished in "+str(round(finishTime-startTime,3))+"s")
        print("solved:")
        print5DSudokuGrid(gridArray,squareSize)
        formatSudokuGridTo2DFrom5D(gridArray,squareSize,gridNumber)
    else:
        print("grid unsolvable")
