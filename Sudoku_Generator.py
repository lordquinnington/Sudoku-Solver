#~~~~~ Sudoku Generator ~~~~~#

import random
#from Sudoku_Solver import formatSudokuGridTo5D

################################################ generating functions ################################################

def generateCompletedGrid():
##    newGrid, squareSize = formatSudokuGridTo5D("Blank")
##    print(newGrid)#
##    rowNums = []
##    for i in range(3):
##        for j in range(3):
##            newGrid = eliminateNotPossibleNums(newGrid,3,0,i,0,j)
##            try:
##                newGrid[0][i][0][j].remove(0)
##                choiceToFillIn = random.choice(newGrid[0][i][0][j])
##                newGrid[0][i][0][j].clear()
##                newGrid[0][i][0][j].append(choiceToFillIn)
##            except ValueError:
##                pass
##            rowNums.append(newGrid[0][i][0][j][0])
##    newGrid.clear()
    rowNums = []
    possibilities = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        choiceToFillIn = 
    for i in range(3):
        for j in range(3):
            if i != 0: #and j == 0:
                if j == 0:
                    rowNums = rowNums[8:]+rowNums[:8]
                    print(rowNums)#
                else:
                    rowNums = rowNums[6:]+rowNums[:6]
                    print(rowNums)#
            else:
                rowNums = rowNums[6:]+rowNums[:6]
                print(rowNums)
            newGrid.append(rowNums)
        
    
    return newGrid
        
        
newGrid = generateCompletedGrid()
print(newGrid)

'''perhaps generate some random numbers and then fill in the rest from randomly choosing the least possible numbers (or both, generate 1 and then fill some in and generate again (but that might be slower))'''
'''need to check for possible invalid inputs when randomly filling in so perhaps utilise the find numbers to remove function?'''
