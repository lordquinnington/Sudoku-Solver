#~~~~ Sudoku Solver ~~~~#

import csv

def formatSudokuGrid():
    with open ("Sudoku_Grid.csv","r") as sudokuGrid:
        gridArray2D = list(csv.reader(sudokuGrid))
    gridArray4D = []
    squareSize = int(len(gridArray2D[0])**0.5)
    for w in range(squareSize):
        tempArray1 = []
        for x in range(squareSize):
            tempArray2 = []
            for y in range(squareSize):
                tempArray3 = []
                for z in range(squareSize):
                    tempArray4 = []
                    #gridArray4D[w][x][y][z].append("2")
    return gridArray4D

gridArray = formatSudokuGrid()
print(gridArray[2][1][1][0])
