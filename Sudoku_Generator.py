#~~~~~ Sudoku Generator ~~~~~#

import random
from Sudoku_Solver import formatSudokuGridTo5D, checkGridIsCompleted, eliminateNotPossibleNums

################################################ generating functions ################################################

def generateCompletedGrid():
    newGrid, squareSize = formatSudokuGridTo5D("Blank")
    print(newGrid)#
    completed = False
    while not completed:
        beenFilledIn = False
        while not beenFilledIn:
            randPos = []
            for i in range(4):
                randPos.append(random.randint(0,2))
            print(randPos)
            #beenFilledIn = True
            if newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]][0] == 0:
                newGrid = eliminateNotPossibleNums(newGrid,3,randPos[0],randPos[1],randPos[2],randPos[3])
                try:
                    newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]].remove(0)
                    choice = random.choice(newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]])
                    for i in range (len(newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]])):
                        if newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]][i] != choice:
                            newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]].remove(newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]][i])
                            beenFilledIn = True
                except ValueError:
                    pass

            beenFilledIn = False
                
        completed = True
        #for i in range(3):
        #    for j in range(3):
        #        for k in range(3):
        #            for l in range(3):
        #                if newGrid[i][j][k][l][0] == 0:
                            
generateCompletedGrid()

'''perhaps generate some random numbers and then fill in the rest from randomly choosing the least possible numbers (or both, generate 1 and then fill some in and generate again (but that might be slower))'''
'''need to check for possible invalid inputs when randomly filling in so perhaps utilise the find numbers to remove function?'''
