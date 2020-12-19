#~~~~~ Sudoku Generator ~~~~~#

import random
from Sudoku_Solver import writeCompletedGridToCSV

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

def formatSudokuGridTo2DFrom3D(gridArray,squareSize):    # function to convert the grid (used to split the 9 small rows into the 3 main rows so they can be shuffled)
    newGrid = []
    for i in range(squareSize):
        for j in range(squareSize):
            newGrid.append(gridArray[i][j])
    return newGrid

def formatSudokuGridTo3DFrom2D(gridArray,squareSize):     # function to convert the grid back to a 2D array for convenience 
    newGrid = []
    for i in range(squareSize):
        tempArray1 = []
        for j in range(squareSize):
            tempArray1.append(gridArray[3*i+j])
        newGrid.append(tempArray1)
    return newGrid

################################################ generating functions ################################################

def shuffleSmallArea(gridArray,squareSize):    # function to randomly rearrange the small rows/columns (but have to be kept within their parent row/column to remain valid)
    newGrid = []
    for i in range(squareSize):
        tempArray1 = []
        options = [0,1,2]
        for j in range(squareSize):
            tempVar = random.choice(options)
            tempArray1.append(gridArray[i][tempVar])
            options.remove(tempVar)
        newGrid.append(tempArray1)
    return newGrid

def shuffleBigArea(gridArray,squareSize):    # function to randomly rearrange the big rows/columns
    newGrid = []
    options = [0,1,2]
    for i in range(squareSize):
        tempVar = random.choice(options)
        newGrid.append(gridArray[tempVar])
        options.remove(tempVar)
    return newGrid

def generateCompletedGrid():
    newGrid = []
    rowNums = []
    options = [1,2,3,4,5,6,7,8,9]
    for i in range(9):    # generates the initial random row which all the other rows will be shifted based on
        rowNums.append(random.choice(options))
        options.remove(rowNums[i])
    for i in range(3):    # generated the shifted grid
        for j in range(3):
            if i != 0:
                if j == 0:
                    rowNums = rowNums[8:]+rowNums[:8]    # shifts by 1 if the top row
                else:
                    rowNums = rowNums[6:]+rowNums[:6]    # other rows get shifted by 3
            else:
                rowNums = rowNums[6:]+rowNums[:6]
            newGrid.append(rowNums)
    bigRows = formatSudokuGridTo3DFrom2D(newGrid,3)
    newBigRowOrder = shuffleBigArea(bigRows,3)    # randomly rearrange the big rows
    newSmallRowOrder = shuffleSmallArea(newBigRowOrder,3)    # randomly rearrange the small rows inside the big rows
    bigColumnsTemp = []    # has to effectively rotate the grid by making the columns into 2D arrays (so can manipulate the same as the rows)
    for i in range(9):
        tempArray1 = []
        for j in range(3):
            for k in range(3):
                tempArray1.append(newSmallRowOrder[j][k][i])
        bigColumnsTemp.append(tempArray1)
    bigColumns = formatSudokuGridTo3DFrom2D(bigColumnsTemp,3)
    newBigColumnOrder = shuffleBigArea(bigColumns,3)    # randomly rearrange the big columns
    newSmallColumnOrder = shuffleSmallArea(newBigColumnOrder,3)    # randomly rearrange the small columns inside the big columns
    newGrid = formatSudokuGridTo2DFrom3D(newSmallColumnOrder,3)    # turns the grid back into a 2D array to make it more compatible later    
    return newGrid

def initialiseGenerating():
    gridNumber = input("enter a grid number> ")
    newGrid = generateCompletedGrid()
    print2DSudokuGrid(newGrid,3)
    writeCompletedGridToCSV(newGrid,gridNumber)
