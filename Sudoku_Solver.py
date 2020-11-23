#~~~~ Sudoku Solver ~~~~#

import csv

def formatSudokuGrid():    # function to turn the 2D csv grid into a 5D array
    with open ("Sudoku_Grid.csv","r") as sudokuGrid:    # opens the csv file in read mode and converts into a 2D array
        gridArray2D = list(csv.reader(sudokuGrid))
    squareSize = int(len(gridArray2D[0])**0.5)    # finds the size of the squares, so not limited by a 3x3 grid
    gridArray4D = []
    for i in range(squareSize):
        tempArray1 = []
        for j in range(squareSize):
            tempArray2 = []
            for k in range(squareSize):
                tempArray3 = []
                for l in range(squareSize):
                    tempArray4 = [gridArray2D[3*i+k][3*j+l]]    # adds each number from the 2D array to the 5D array
                    tempArray3.append(tempArray4)
                tempArray2.append(tempArray3)
            tempArray1.append(tempArray2)
        gridArray4D.append(tempArray1)    # those arrays are then appended onto each other till a 5D array is formed                
    return gridArray4D, squareSize

def formatToAddAllNumbers(gridArray, squareSize):    # function to add all possible numbers to each blank position
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    if gridArray[i][j][k][l][0] == '0':
                        for m in range(squareSize*squareSize):
                            gridArray[i][j][k][l].append(str(m+1))    # adds the numbers 1 to 9 to each blank position
    return gridArray    # another function will go through and remove any invalid numbers later

def checkForCompletedSquare(gridArray,squareSize,a,b,c,d):    # function to check if the given large square is completed
    total = 0
    for i in range(squareSize):
        for j in range(squareSize):
            total += int(gridArray[a][b][i][j][0])    # adds each number in the square to running total
    if total == 45:    # the sum of all the sudoku numbers is 45, so uf the sum is that then it must be completed
        return True
    return False    # returns false if not

def checkForCompletedRow(gridArray,squareSize,a,b,c,d):    # function to find if the row of the given coordinate is completed (pass in 1st and 3rd coordinate as parameters)
    total = 0
    for i in range(squareSize):
        for j in range(squareSize):
            total += int(gridArray[a][i][c][j][0])    # finds the sum of all the numbers 
    if total == 45:    # the sum of all the possible numbers is 45 so returns true if it is that
        return True
    return False    # returns false if not completed

def checkForCompletedColumn(gridArray,squareSize,a,b,c,d):     # function to find if the column of the given coordinate is comppleted (pass in 2nd and 4th coordinate as parameters)
    total = 0
    for i in range(squareSize):
        for j in range(squareSize):
            total += int(gridArray[i][b][j][d][0])    # finds the sum of all the numbers in the column
    if total == 45:
        return True    # returns true if all the numbers are present
    return False

def checkGridIsCompleted(gridArray, squareSize):    # function to check if all the squares in the grid are filled in (correct or not is decided later)
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    if gridArray[i][j][k][l][0] == '0':     # checks each space for a zero, which would indicate if it's been solved or not
                        return False
    gridsCorrect = 0
    for i in range(squareSize):
        for j in range(squareSize):
            correctGrid = checkForCompletedSquare(gridArray,squareSize,i,j,None,None)    # uses the other function to check if each grid is valid
            if correctGrid == True:
                gridsCorrect += 1    # adds one if the grid is returned as true
    rowsCorrect = 0
    for i in range(squareSize):
        for j in range(squareSize):
            correctRow = checkForCompletedRow(gridArray,squareSize,i,None,j,None)    # could combine all the checking into 1 <<<<<<<<<<<<< read pls ###########
            if correctRow == True:
                rowsCorrect += 1
    columnsCorrect = 0
    for i in range(squareSize):
        for j in range(squareSize):
            correctColumn = checkForCompletedColumn(gridArray,squareSize,None,i,None,j)
            if correctColumn == True:
                columnsCorrect += 1
    if gridsCorrect and rowsCorrect and columnsCorrect == squareSize*squareSize:
        return True    # if the number of grids and rows and columns correct is equal to the squareSize squared, the grid is deemed to be correct
    return False

def findNumbersInRow(gridArray,squareSize,a,b,c,d):
    numbersInRow = []
    for i in range(squareSize):
        for j in range(squareSize):
            if gridArray[a][i][c][j][0] != '0':
                numbersInRow.append(gridArray[a][i][c][j][0])
    return numbersInRow

def findNumbersInColumn(gridArray,squareSize,a,b,c,d):
    numbersInColumn = []
    for i in range(squareSize):
        for j in range(squareSize):
            if gridArray[i][b][j][d][0] != '0':
                numbersInColumn.append(gridArray[i][b][j][d][0])
    return numbersInColumn

def findNumbersInSquare(gridArray,squareSize,a,b,c,d):
    numbersInSquare = []
    for i in range(squareSize):
        for j in range(squareSize):
            if gridArray[a][b][i][j][0] != '0':
                numbersInSquare.append(gridArray[a][b][i][j][0])
    return numbersInSquare

def eliminateNotPossibleNumbers(gridArray,squareSize,a,b,c,d):
    numbersToRemove = []
    numbersToRemove.append(findNumbersInSquare(gridArray,squareSize,a,b,None,None))
    numbersToRemove.append(findNumbersInRow(gridArray,squareSize,a,None,c,None))
    numbersToRemove.append(findNumbersInColumn(gridArray,squareSize,None,b,None,d))
    for i in range(squareSize):
        for j in range(len(numbersToRemove[i])):
            #print(numbersToRemove[i][j])
            try:
                gridArray[a][b][c][d].remove(numbersToRemove[i][j])
            except ValueError:
                pass
    return gridArray
    

gridArray, squareSize = formatSudokuGrid()
print(gridArray, '\n')
gridArary = formatToAddAllNumbers(gridArray, squareSize)
print(gridArray)
##print(gridArray[0][0][0][1])
##completedSquare = checkForCompletedSquare(gridArray,squareSize,0,0,0,1)
##print(completedSquare)
##completedRow = checkForCompletedRow(gridArray,squareSize,0,0,0,1)
##print(completedRow)
##completedColumn = checkForCompletedColumn(gridArray,squareSize,0,0,0,1)
##print(completedColumn)
finished = checkGridIsCompleted(gridArray, squareSize)
print(finished)
print(findNumbersInRow(gridArray,squareSize,0,0,0,2))
print(findNumbersInColumn(gridArray,squareSize,0,0,0,2))
print(findNumbersInSquare(gridArray,squareSize,0,0,0,2))
eliminateNotPossibleNumbers(gridArray,squareSize,0,0,0,2)
# write functions which return a list of numbers in that row/square/column etc
