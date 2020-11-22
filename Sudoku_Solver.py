#~~~~ Sudoku Solver ~~~~#

import csv

def formatSudokuGrid():    # function to turn the 2D csv grid into a 5D array
    with open ("Sudoku_Grid.csv","r") as sudokuGrid:    # opens the csv file in read mode and converts into a 2D array
        gridArray2D = list(csv.reader(sudokuGrid))
    squareSize = int(len(gridArray2D[0])**0.5)    # finds the size of the squares, so not limited by a 3x3 grid
    gridArray4D = []
    for w in range(squareSize):
        tempArray1 = []
        for x in range(squareSize):
            tempArray2 = []
            for y in range(squareSize):
                tempArray3 = []
                for z in range(squareSize):
                    tempArray4 = [gridArray2D[3*w+y][3*x+z]]    # adds each number from the 2D array to the 5D array
                    tempArray3.append(tempArray4)
                tempArray2.append(tempArray3)
            tempArray1.append(tempArray2)
        gridArray4D.append(tempArray1)    # those arrays are then appended onto each other till a 4D array is formed                
    return gridArray4D, squareSize

def formatToAddAllNumbers(gridArray, squareSize):    # function to add all possible numbers to each blank position
    for w in range(squareSize):
        for x in range(squareSize):
            for y in range(squareSize):
                for z in range(squareSize):
                    if gridArray[w][x][y][z][0] == '0':
                        for i in range(squareSize*squareSize):
                            gridArray[w][x][y][z].append(str(i+1))    # adds the numbers 1 to 9 to each blank position
    return gridArray    # another function will go through and remove any invalid numbers later

gridArray, squareSize = formatSudokuGrid()
print(gridArray, '\n')
gridArary = formatToAddAllNumbers(gridArray, squareSize)
print(gridArray)
print(gridArray[0][0][0][1])
