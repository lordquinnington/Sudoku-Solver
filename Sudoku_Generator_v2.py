#~~~~~ Sudoku Generator version 2 ~~~~~#

import random, time
from Sudoku_Solver import writeCompletedGridToCSV, solve, formatSudokuGridTo5DFrom2D, formatSudokuGridTo2DFrom5D
from Sudoku_Solver_GUI import createBlank2DGrid

################################################ formatting functions ################################################

def print2DSudokuGrid(gridArray,squareSize):     # function to print out the completed grid
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    print(gridArray[squareSize*i+j][squareSize*k+l],end=' ')
                print("|",end=' ')
            print()
        print("-----------------------")

def findGridName():     # finds the next available grid name to call the new file (to avoid overwriting previous grids)
    available = False
    x = 1
    while not available:
        try:
            open("Sudoku_Grid_"+str(x)+"_Completed.csv","x")
            print("file is completed grid "+str(x))
            return str(x)
        except FileExistsError:
            x += 1

################################################ generating functions ################################################

def generateGrid(size):
    validGrid = False
    while not validGrid:
        blankGrid = createBlank2DGrid(9)
        options = [1,2,3,4,5,6,7,8,9]
        for i in range(2):
            coords = []
            for i in range(2):
                x = random.randint(0,8)
                coords.append(x)
            blankGrid[coords[0]][coords[1]] = random.choice(options)
            options.remove(blankGrid[coords[0]][coords[1]])
        tempGrid = formatSudokuGridTo5DFrom2D(blankGrid,3)
        newGrid = solve(tempGrid,3)
        if newGrid == None:
            validGrid = False
        else:
            validGrid = True
    newGrid = formatSudokuGridTo2DFrom5D(newGrid,3)
    return newGrid
        
def initialiseGenerating():
    gridNumber = findGridName()
    startTime = time.time()
    newGrid = generateGrid(9)
    finishTime = time.time()
    print("grid generated (in "+str(round(finishTime-startTime,3))+"s):")
    print2DSudokuGrid(newGrid,3)
    writeCompletedGridToCSV(newGrid,gridNumber)
