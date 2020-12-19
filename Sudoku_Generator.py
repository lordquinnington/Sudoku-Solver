#~~~~~ Sudoku Generator ~~~~~#

import random
from Sudoku_Solver import writeCompletedGridToCSV

################################################ generating functions ################################################

def generateCompletedGrid():
    newGrid = []
    # generate the initial random row
    rowNums = []
    options = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        rowNums.append(random.choice(options))
        options.remove(rowNums[i])
    # generate the shifted grid
    for i in range(3):
        for j in range(3):
            if i != 0:
                if j == 0:
                    rowNums = rowNums[8:]+rowNums[:8]
                else:
                    rowNums = rowNums[6:]+rowNums[:6]
            else:
                rowNums = rowNums[6:]+rowNums[:6]
            newGrid.append(rowNums)
    # randomly rearrange the big rows
    bigRows = []
    for i in range(3):
        tempArray1 = []
        for j in range(3):
            tempArray1.append(newGrid[3*i+j])
        bigRows.append(tempArray1)
    newBigRowOrder = []
    options = [0,1,2]
    for i in range(3):
        x = random.choice(options)
        newBigRowOrder.append(bigRows[x])
        options.remove(x)
    # randomly rearrange the small rows inside the big rows
    newSmallRowOrder = []
    for i in range(3):
        tempArray1 = []
        options = [0,1,2]
        for j in range(3):
            x = random.choice(options)
            tempArray1.append(newBigRowOrder[i][x])
            options.remove(x)
        newSmallRowOrder.append(tempArray1)
    # randomly rearrange the big columns
    bigColumnsTemp = []
    for i in range(9):
        tempArray1 = []
        for j in range(3):
            for k in range(3):
                tempArray1.append(newSmallRowOrder[j][k][i])
        bigColumnsTemp.append(tempArray1)
    bigColumns = []
    for i in range(3):
        tempArray1 = []
        for j in range(3):
            tempArray1.append(bigColumnsTemp[3*i+j])
        bigColumns.append(tempArray1)
    newBigColumnOrder = []
    options = [0,1,2]
    for i in range(3):
        x = random.choice(options)
        newBigColumnOrder.append(bigColumns[x])
        options.remove(x)
    # randomly rearrange the small columns inside the big columns
    newSmallColumnOrder = []
    for i in range(3):
        tempArray1 = []
        options = [0,1,2]
        for j in range(3):
            x = random.choice(options)
            tempArray1.append(newBigColumnOrder[i][x])
            options.remove(x)
        newSmallColumnOrder.append(tempArray1)
    # converts to a 2D array
    newGrid = []
    for i in range(3):
        for j in range(3):
            newGrid.append(newSmallColumnOrder[i][j])
    # prints the grid
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    print(newGrid[3*i+j][3*k+l],end=' ')
                print("|",end=' ')
            print()
        print("-----------------------")
    
    return newGrid
        
        
newGrid = generateCompletedGrid()
writeCompletedGridToCSV(newGrid,"22")
