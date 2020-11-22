#~~~~ Sudoku Solver ~~~~#

import csv

def formatSudokuGrid():
    with open ("Sudoku_Grid.csv","r") as sudokuGrid:
        gridArray2D = list(csv.reader(sudokuGrid))
    gridArray4D = []
    squareSize = int(len(gridArray2D[0])**0.5)
    print(gridArray2D, '\n')
    tempArray1 = []
    for w in range(squareSize):
        tempArray2 = []
        for x in range(squareSize):
            tempArray3 = []
            for y in range(squareSize):
                tempArray4 = []
                for z in range(squareSize):
                    #tempArray4 = []
                    tempArray4.append(gridArray2D[3*w+y][z])
                #tempArray3.append(gridArray2D[3*w+y][3*x+z])
                tempArray3.append(tempArray4)
            #tempArray2.append(gridArray2D[3*w+y][3*x+z])
            tempArray2.append(tempArray3)
        #tempArray1.append(gridArray2D[w])
        tempArray1.append(tempArray2)
                    
    #gridArray4D.append(tempArray1)
    return tempArray1#gridArray4D

gridArray = formatSudokuGrid()
print(gridArray)
