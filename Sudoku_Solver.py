#~~~~ Sudoku Solver ~~~~#

import csv

def formatSudokuGrid():    # function to turn the 2D csv grid into a 5D array
    with open ("Sudoku_Grid_3.csv","r") as sudokuGrid:    # opens the csv file in read mode and converts into a 2D array
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
            if gridArray[a][b][c][d][0] == '0':
                if len(gridArray[a][b][c][d]) == 2:
                    gridArray[a][b][c][d].remove('0')
                else:
                    try:
                        gridArray[a][b][c][d].remove(numbersToRemove[i][j])
                    except ValueError:
                        pass
    return gridArray
    
def formatTo2DArray(gridArray, squareSize):
    gridArray1D = []
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    gridArray1D.append(gridArray[i][k][j][l][0])
    gridArray2D = []
    for i in range(squareSize*squareSize):
        tempArray = []
        for j in range(squareSize*squareSize):
            tempArray.append(gridArray1D[9*i+j])
        gridArray2D.append(tempArray)
    return gridArray2D

def writeCompletedGridToCSV(gridArray2D, squareSize):      
    try:
        open("Sudoku_Grid_Completed_3.csv", "x")
        with open("Sudoku_Grid_Completed_3.csv", "w", newline='') as completedGridFile:
            toWrite = csv.writer(completedGridFile, delimiter=',')
            for row in gridArray2D:
                toWrite.writerow(row)
                
    except FileExistsError:
        pass

gridArray, squareSize = formatSudokuGrid()
gridArary = formatToAddAllNumbers(gridArray, squareSize)

finished = checkGridIsCompleted(gridArray,squareSize)

while not finished:
    print(gridArray)
    input("enter to continue")
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    gridArray = eliminateNotPossibleNumbers(gridArray,squareSize,i,j,k,l)
    finished = checkGridIsCompleted(gridArray,squareSize)

print(gridArray)
print("finished")

gridArray2D = formatTo2DArray(gridArray, squareSize)
writeCompletedGridToCSV(gridArray2D, squareSize)
# write something to guess at the solution
# change what it sums to 9+8+7+6 etc not just 45



    
