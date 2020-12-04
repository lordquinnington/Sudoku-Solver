#~~~~ Sudoku Solver ~~~~#

import csv, copy, time

################################################ formatting functions ################################################

def formatSudokuGrid():    # function to turn the 2D csv grid into a 5D array
    with open ("Sudoku_Grid_7.csv","r") as sudokuGrid:    # opens the csv file in read mode and converts into a 2D array
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
                    if tempArray4[0] == '0':
                        for m in range(squareSize*squareSize):
                            tempArray4.append(str(m+1))    # adds a list of the possible numbers to each blank grid (before removing them)
                    tempArray3.append(tempArray4)
                tempArray2.append(tempArray3)
            tempArray1.append(tempArray2)
        gridArray4D.append(tempArray1)    # those arrays are then appended onto each other till a 5D array is formed                
    return gridArray4D, squareSize

def formatTo2DArray(gridArray, squareSize):    # function to turn the 5D array back into a 2D array to be more human readable
    gridArray1D = []
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    gridArray1D.append(gridArray[i][k][j][l][0])    # appends all the values in the 5D array initially to a 1D array
    gridArray2D = []    # i couldn't get it to go straight from a 5D to a 2D array so it had to be converted into a 1D array first then converted to a 2D array
    for i in range(squareSize*squareSize):
        tempArray = []
        for j in range(squareSize*squareSize):
            tempArray.append(gridArray1D[9*i+j])    # forms the 2D array
        gridArray2D.append(tempArray)
    return gridArray2D

def writeCompletedGridToCSV(gridArray2D, squareSize):     # function to write the completed grid back to a csv file to be more readable and checkable  
    try:    # tries to creat a file for the completed grid
        open("Sudoku_Grid_Completed_7.csv", "x")
        with open("Sudoku_Grid_Completed_7.csv", "w", newline='') as completedGridFile:
            toWrite = csv.writer(completedGridFile, delimiter=',')
            for row in gridArray2D:
                toWrite.writerow(row)   # writes the contents of the 2D array to the text file        
    except FileExistsError:    # if the file already exists, the program assumes the correct answer is already in there so skips it
        print("file already exists")
        pass

################################################ searching functions ################################################

def toSumUpTo(squareSize):    # function to find what each of the rows/columns/grids should sum up to
    return (((squareSize*squareSize)**2)+squareSize*squareSize)//2   # utilises that mathsy trick thing instead of recursion

def checkForCompletedSquare(gridArray,squareSize,toSumTo,a,b,c,d):    # function to check if the given large square is completed
    total = 0
    for i in range(squareSize):
        for j in range(squareSize):
            total += int(gridArray[a][b][i][j][0])    # adds each number in the square to running total
    if total == toSumTo:    # the sum of all the sudoku numbers is 45, so uf the sum is that then it must be completed
        return True
    return False    # returns false if not

def checkForCompletedRow(gridArray,squareSize,toSumTo,a,b,c,d):    # function to find if the row of the given coordinate is completed
    total = 0
    for i in range(squareSize):
        for j in range(squareSize):
            total += int(gridArray[a][i][c][j][0])    # finds the sum of all the numbers 
    if total == toSumTo:    # the sum of all the possible numbers is 45 so returns true if it is that
        return True
    return False    # returns false if not completed

def checkForCompletedColumn(gridArray,squareSize,toSumTo,a,b,c,d):     # function to find if the column of the given coordinate is comppleted
    total = 0
    for i in range(squareSize):
        for j in range(squareSize):
            total += int(gridArray[i][b][j][d][0])    # finds the sum of all the numbers in the column
    if total == toSumTo:
        return True    # returns true if all the numbers are present
    return False

def checkGridIsCompleted(gridArray, squareSize):    # function to check if all the squares in the grid are filled in
    counter = 0
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    try:#
                        counter += len(gridArray[i][j][k][l])    # has a counter for later (to check if the grid is full yet still returning false for being finished)
                    except TypeError:#
                        return False, counter#
                    if gridArray[i][j][k][l][0] == '0':     # checks each space for a zero, which would indicate if it's been solved or not
                        return False, counter                
    toSumTo = toSumUpTo(squareSize)
    gridsCorrect = 0
    rowsCorrect = 0
    columnsCorrect = 0
    for i in range(squareSize):
        for j in range(squareSize):    # checks to see if all 9 rows/columns/grids are completed
            try:
                correctGrid = checkForCompletedSquare(gridArray,squareSize,toSumTo,i,j,None,None)
                if correctGrid == True:
                    gridsCorrect += 1
                correctRow = checkForCompletedRow(gridArray,squareSize,toSumTo,i,None,j,None)
                if correctRow == True:
                    rowsCorrect += 1
                correctColumn = checkForCompletedColumn(gridArray,squareSize,toSumTo,None,i,None,j)
                if correctColumn == True:
                    columnsCorrect += 1
            except TypeError:
                return False, counter
    if gridsCorrect and rowsCorrect and columnsCorrect == squareSize*squareSize:
        return True, counter    # if the number of grids, rows and columns correct is equal to the squareSize squared, the grid is deemed to be correct
    return False, counter

def findNumbersInRow(gridArray,squareSize,a,b,c,d):    # function to find which numbers are in a given row
    numbersInRow = []
    for i in range(squareSize):
        for j in range(squareSize):
            if gridArray[a][i][c][j][0] != '0':
                numbersInRow.append(gridArray[a][i][c][j][0])     # appends the value there to an array
    return numbersInRow

def findNumbersInColumn(gridArray,squareSize,a,b,c,d):      # function to find which numbers are in a given row
    numbersInColumn = []
    for i in range(squareSize):
        for j in range(squareSize):
            if gridArray[i][b][j][d][0] != '0':
                numbersInColumn.append(gridArray[i][b][j][d][0])    # appends the values to an array
    return numbersInColumn

def findNumbersInSquare(gridArray,squareSize,a,b,c,d):    # function to find which numbers are in a given column
    numbersInSquare = []
    for i in range(squareSize):
        for j in range(squareSize):
            if gridArray[a][b][i][j][0] != '0':
                numbersInSquare.append(gridArray[a][b][i][j][0])    # appends them to an array
    return numbersInSquare

def findNumbersToRemove(gridArray,squareSize,a,b,c,d):    # function to finf the numbers which can be removed as possibilities for a given square
    numbersToRemove = []
    numbersToRemove.append(findNumbersInSquare(gridArray,squareSize,a,b,None,None))
    numbersToRemove.append(findNumbersInRow(gridArray,squareSize,a,None,c,None))
    numbersToRemove.append(findNumbersInColumn(gridArray,squareSize,None,b,None,d))
    return numbersToRemove

################################################ eliminating functions ################################################

def eliminateNotPossibleNumbers(gridArray,squareSize,a,b,c,d):    # function to eliminate the numbersa square can't be
    numbersToRemove = findNumbersToRemove(gridArray,squareSize,a,b,c,d)
    for i in range(squareSize):
        for j in range(len(numbersToRemove[i])):
            if gridArray[a][b][c][d][0] == '0':
                #if len(gridArray[a][b][c][d]) == 2:
                #    gridArray[a][b][c][d].remove('0')    # if there is only one possible number, the 0 is removed, effectively filling in the square
                #else:
                try:
                    gridArray[a][b][c][d].remove(numbersToRemove[i][j])    # tries to remove the numbers from the list to remove
                except ValueError:    # if it returns a value error, the possible number has already been removed so it gets ignored
                    pass
    if len(gridArray[a][b][c][d]) == 1:#
        return None#
    elif len(gridArray[a][b][c][d]) == 2:#
        gridArray[a][b][c][d].remove('0')#
    return gridArray

def findPossibleGridArrays(gridArray, squareSize):    # function to start guessing and returning multiple grid arrays it could be
    leastPossibleNums = 9
    leastPossibleNumsPos = []
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    if gridArray[i][j][k][l][0] == '0': 
                        if len(gridArray[i][j][k][l]) < leastPossibleNums:    # first, it finds the position with the least number of possibilities and uses that position as that will give the least amount of possible grid arrays
                            leastPossibleNums = len(gridArray[i][j][k][l])
                            leastPossibleNumsPos = [i,j,k,l]
    leastPossibleNums -= 1
    if leastPossibleNums == 8:
        #return None, None
        return gridArray, leastPossibleNums
    a = leastPossibleNumsPos[0]
    b = leastPossibleNumsPos[1]
    c = leastPossibleNumsPos[2]
    d = leastPossibleNumsPos[3]
    gridArray[a][b][c][d].remove('0')    # removes the 0 as it needs to fill in numbers to guess
    possibleGridsArray = []
    for i in range(leastPossibleNums):
        x = gridArray[a][b][c][d][i]    # creates a temporary copy of the value which was in there
        gridArray[a][b][c][d].remove(gridArray[a][b][c][d][i])    # removes that value from the grid array
        y = copy.deepcopy(gridArray)    # makes a temporary copy of the new grid array
        possibleGridsArray.append(y)    # appends the copy to the list of possible arrays
        gridArray[a][b][c][d].insert(i,x)     # inserts the value it removed back in so it is included next time
    return possibleGridsArray, leastPossibleNums

def solve(gridArray,squareSize):    # function to loop through once removing as many numbers as it can
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    gridArray = eliminateNotPossibleNumbers(gridArray,squareSize,i,j,k,l)    # removes as many numbers as it can from  the grid
                    if gridArray == None:
                        return None
                        
    return gridArray

def initialiseSolving(gridArray,squareSize):
    '''need to add a way of detecting if its reached a dead end, so if there is a free space where no number can go in etc'''
    '''do the functions need to be more robust in deciding which ones to remove'''
    '''add removing the zero perhaps after so it can return a problem if the len of the position is 1 (eliminate possible nums function?)'''
    changed = False
    while not notChanged:
        finished, counter = checkgridIsCompleted(gridArray,squareSize)
        if finished == True:
            return gridArray
        previousCounter = counter
        gridArray = solve(gridArray,squareSize)
        if gridArray == None:
            return None
        finished, counter = checkGridIsCompleted(gridArray,squareSize)
        if previousCounter == counter:
            notChanged = True
    possibleGridsArray, leastPossibleNums = findPossibleGridArrays(gridArray,squareSize)
    for i in range(leastPossibleNums):
        deadEnd = False
        while not deadEnd:
            gridArray = solve(possibleGridArray[i],squareSize)
            if gridArray == None:
                deadEnd = True

################################################ main program ################################################

gridArray, squareSize = formatSudokuGrid()    # the grid is first formatted into a 5D array
print("grid array: \n", gridArray)
input("press enter to solve")

startTime = time.time()
finished, gridSize = checkGridIsCompleted(gridArray,squareSize)
while not finished:
    #print(gridArray)#
    #input("next eliminate")#
    previousGridArray = copy.deepcopy(gridArray)    # makes a copy of the first array to use to check later
    gridArray = solve(gridArray, squareSize)
    if gridArray == previousGridArray:    # sees if the previous grid is the same as the new grid, indicating no numbers can be removed, which should be better than an attempts system
        print(gridArray)
        possibleGridsArray, leastPossibleNums = findPossibleGridArrays(gridArray,squareSize)
        print(possibleGridsArray)
        gridArray = guess(possibleGridsArray,squareSize,leastPossibleNums)        
    finished, gridSize = checkGridIsCompleted(gridArray,squareSize)    
finishTime = time.time()    # times how long it takes for research purposes


print("finished (in "+str(round(finishTime-startTime, 3))+"s):")
print(gridArray)

gridArray2D = formatTo2DArray(gridArray, squareSize)    # formats the grid back into human readable form
writeCompletedGridToCSV(gridArray2D, squareSize)

'''use it to work backwards to make a puzzle'''
'''add a GUI'''
'''see if it can get to solve harder grids'''
'''try copying the array with list instead of deepcopy'''
