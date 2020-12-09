#~~~~~ Sudoku Generator ~~~~~#

import random
from Sudoku_Solver import formatSudokuGridTo5D, checkGridIsCompleted

################################################ generating functions ################################################

def generateCompletedGrid():
    newGrid, squareSize = formatSudokuGridTo5D("blank")
    print(newGrid)#
    completed = False
    while not completed:
        alreadyFilledIn = True
        while alreadyFilledIn:
            randPos = []
            for i in range(4)
            
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if newGrid[i][j][k][l][0] == 0:
                            
generateCompletedGrid()

'''perhaps generate some random numbers and then fill in the rest from randomly choosing the least possible numbers (or both, generate 1 and then fill some in and generate again (but that might be slower))'''
'''need to check for possible invalid inputs when randomly filling in so perhaps utilise the find numbers to remove function?'''
