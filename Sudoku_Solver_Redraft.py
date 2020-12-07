#~~~~ Sudoku Solver ~~~~#

import csv, copy, time

################################################ formatting functions ################################################

def formatSudokuGridTo5D(gridNumber):
    with open("Sudoku_Grid_"+gridNumber+".csv","r") as sudokuGrid:
        gridArray2D = list(csv.reader(sudokuGrid))
    squareSize = int(len(gridArray2D[0])**0.5)
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
    return gridArray5D, squareSize

def formatSudokuGridTo2D(gridArray,squareSize,gridNumber):
    gridArray2D = []
    for i in range(squareSize):
        for j in range(squareSize):
            tempArray1 = []
            for k in range(squareSize):
                for l in range(squareSize):
                    tempArray1.append(gridArray[i][k][j][l][0])
            gridArray2D.append(tempArray1)
    return writeCompletedGridToCSV(gridArray2D,gridNumber)

def writeCompletedGridToCSV(gridArray2D,gridNumber):
    with open("Sudoku_Grid_"+gridNumber+"_Completed.csv","w",newline='') as completedGridFile:
        toWrite = csv.writer(completedGridFile,delimiter=',')
        for row in gridArray2D:
            toWrite.writerow(row)

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
    for i in range(numberOfPossibleGrids-1):    #############does it only work for when the length of the smallest possibilities is 2. ANY MORE AND IT TURNS IT INTO [5, 9] ETC. find a way to remove all but 1
        y = copy.deepcopy(gridArray)
        print(i)
        print(y[a][b][c][d])
        y[a][b][c][d].remove(0)
        y[a][b][c][d].remove(gridArray[a][b][c][d][i+1])
        possibleGrids.append(y)
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
                print("solved:")
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

    
gridNumber = str(input("enter the grid number >"))
gridArray, squareSize = formatSudokuGridTo5D(gridNumber)
print(gridArray,"\n")
print(solve(gridArray,squareSize))
#formatSudokuGridTo2D(gridArray,squareSize,gridNumber)
x = [[[[[5], [3], [4]], [[6], [7], [2]], [[1], [9], [8]]], [[[6], [7], [8]], [[1], [9], [5]], [[3], [4], [2]]], [[[9], [1], [2]], [[3], [4], [8]], [[5], [6], [7]]]], [[[[8], [0, 1, 5], [0, 5, 9]], [[4], [2], [6]], [[7], [1], [3]]], [[[7], [6], [1]], [[8], [5], [3]], [[9], [2], [4]]], [[[4], [2], [3]], [[7], [9], [1]], [[8], [5], [6]]]], [[[[9], [6], [1]], [[2], [8], [7]], [[3], [0, 4, 5], [5]]], [[[5], [3], [7]], [[4], [1], [9]], [[2], [8], [6]]], [[[2], [8], [4]], [[6], [3], [5]], [[1], [7], [9]]]]]
x = [[[[[5], [3], [4]], [[6], [7], [2]], [[1], [9], [8]]], [[[6], [7], [8]], [[1], [9], [5]], [[3], [4], [2]]], [[[9], [1], [2]], [[3], [4], [8]], [[5], [6], [7]]]], [[[[8], [0, 1, 5, 7], [0, 5, 6, 9]], [[4], [2], [6]], [[7], [1], [3]]], [[[7], [6], [1]], [[8], [5], [3]], [[9], [2], [4]]], [[[4], [2], [3]], [[7], [9], [1]], [[8], [5], [6]]]], [[[[9], [6], [1]], [[2], [8], [7]], [[3], [0, 4, 5, 9], [5]]], [[[5], [3], [7]], [[4], [1], [9]], [[2], [8], [6]]], [[[2], [8], [4]], [[6], [3], [5]], [[1], [7], [9]]]]]
