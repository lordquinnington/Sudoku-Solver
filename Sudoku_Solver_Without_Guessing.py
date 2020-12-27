#~~~~ Sudoku Solver ~~~~#

import csv, copy, time

################################################ formatting functions ################################################

def formatSudokuGridTo5DFrom2D(gridArray2D,squareSize):    # function to turn a 2D array (read from file) into a 5D array to work with
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
                        for m in range(squareSize*squareSize):    # if the space is empty (a zero), then a list of possibilities is appended to that place to be removed later
                            tempArray4.append(m+1)
                    tempArray3.append(tempArray4)
                tempArray2.append(tempArray3)
            tempArray1.append(tempArray2)
        gridArray5D.append(tempArray1)
    return gridArray5D

def formatSudokuGridTo2DFrom5D(gridArray,squareSize):    # function to turn the 5D array back into a 2D array, to write to a file
    gridArray2D = []
    for i in range(squareSize):
        for j in range(squareSize):
            tempArray1 = []
            for k in range(squareSize):
                for l in range(squareSize):
                    tempArray1.append(gridArray[i][k][j][l][0])
            gridArray2D.append(tempArray1)
    return gridArray2D

def print5DSudokuGrid(gridArray,squareSize):     # function to print out the sudoku board in the terminal to make it look nicer (a gift from Gibbo in exchange for the QQWing converter code)
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    print(gridArray[i][k][j][l][0],end=' ')
                print("|",end=' ')
            print()
        print("-----------------------")

def writeCompletedGridToCSV(gridArray2D,gridNumber):    # function to write the grid to a file
    with open("Sudoku_Grid_"+gridNumber+"_Completed.csv","w",newline='') as completedGridFile:
        toWrite = csv.writer(completedGridFile,delimiter=',')
        for row in gridArray2D:
            toWrite.writerow(row)
    print("written to file")

def readIncompleteGridFromCSV(gridNumber):     # function to read in a grid from a CSV file
    with open("Sudoku_Grid_"+gridNumber+".csv","r") as sudokuGrid:
        gridArray2D = list(csv.reader(sudokuGrid))
    squareSize = int(len(gridArray2D[0])**0.5)    # finds the big square size by square rooting the side length
    return gridArray2D, squareSize

################################################ searching functions ################################################

def toSumUpTo(squareSize):
    return (((squareSize*squareSize)**2)+squareSize*squareSize)//2    # finds what the columns should sum to using that maths-y trick

def checkForCompletedAreas(gridArray,squareSize,toSumTo,a,b,c,d):    # function to check if the row/column/square of a given space is completed
    rowTotal = 0
    columnTotal = 0
    squareTotal = 0
    for i in range(squareSize):
        for j in range(squareSize):
            rowTotal += gridArray[a][i][c][j][0]    # appends the filled in numbers to the running total
            columnTotal += gridArray[i][b][j][d][0]    # if a space is not filled in, 0 will be added which obviously makes no difference
            squareTotal += gridArray[a][b][i][j][0]
    if rowTotal + columnTotal + squareTotal == toSumTo*3:    # check to see if each of them sum to 45
        return True
    return False

def checkGridIsCompleted(gridArray,squareSize):    # function to check if the grid is completed or not
    toSumTo = toSumUpTo(squareSize)
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    if gridArray[i][j][k][l][0] == 0:    # if any space is empty, the grid is not complete
                        return False
                    if checkForCompletedAreas(gridArray,squareSize,toSumTo,i,j,k,l) == False:     # if any rows don's sum to the correct amount, the grid is not complete
                        return False
    return True     # only when all the squares are filled in and all the rows sum to the correct number is the grid deemed correct

def findNumbersToRemove(gridArray,squareSize,a,b,c,d):    # function to find all the numbers to remove from the possibilities 
    numbersToRemove = []    # appends to an array any filled in numbers in the row/column/square of a given space which that space can't be
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

def eliminateNotPossibleNums(gridArray,squareSize,a,b,c,d):    # function to remove all the possibilities it can't be from a space
    numbersToRemove = findNumbersToRemove(gridArray,squareSize,a,b,c,d)
    for i in range(len(numbersToRemove)):
        try:
            gridArray[a][b][c][d].remove(numbersToRemove[i])    # uses the array of numbers in the same row/column/square to know what to remove from the posibilities
        except ValueError:    # need a try/except as there could be duplicates in the list
            pass
    if len(gridArray[a][b][c][d]) == 1:     # if all the possibilities have been removed leaving just the 0, the program can deduce the grid is invalid
        return None
    if len(gridArray[a][b][c][d]) == 2:    # once there are only two values, 0 and the correct one, the 0 is removed effectively filling it in
        gridArray[a][b][c][d].remove(0)
    return gridArray

def solve(gridArray,squareSize):    # function to solve the grid
    finished = checkGridIsCompleted(gridArray,squareSize)    # checks the grid first, just in case
    while not finished:
        previousGrid = copy.deepcopy(gridArray)
        for i in range(squareSize):
            for j in range(squareSize):
                for k in range(squareSize):
                    for l in range(squareSize):
                        if gridArray[i][j][k][l][0] == 0:
                            gridArray = eliminateNotPossibleNums(gridArray,squareSize,i,j,k,l)    # loops through and removes all the possibilities it can from each of the squares
                            if gridArray == None:    # returns none if it is an invalid grid
                                return None
        finished = checkGridIsCompleted(gridArray,squareSize)    # checks if the grid is complete
        if gridArray == previousGrid:    # if the grid hasn't changed, the program moves onto guessing
            return None
    return gridArray

def initialiseSolving():
    gridNumber = str(input("enter the grid number >"))
    gridArray2D, squareSize = readIncompleteGridFromCSV(gridNumber)
    gridArray = formatSudokuGridTo5DFrom2D(gridArray2D,squareSize)
    print5DSudokuGrid(gridArray,squareSize)
    startTime = time.time()
    gridArray = solve(gridArray,squareSize)
    finishTime = time.time()
    if gridArray != None:    # if the grid comes back as solved, it is printed to the screen etc
        print("finished in "+str(round(finishTime-startTime,3))+"s")
        print("solved:")
        print5DSudokuGrid(gridArray,squareSize)
        writeCompletedGridToCSV(formatSudokuGridTo2DFrom5D(gridArray,squareSize),gridNumber)
    else:     # if the grid is None, then it is unsolvable by the program
        print("grid unsolvable")
