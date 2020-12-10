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

            if newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]][0] == 0:
                newGrid = eliminateNotPossibleNums(newGrid,3,randPos[0],randPos[1],randPos[2],randPos[3])
                try:
                    newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]].remove(0)
                except ValueError:
                    break
                choice = random.choice(newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]])
                #print(newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]])
                print(choice)
                newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]].clear()
                print(newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]])
                newGrid[randPos[0]][randPos[1]][randPos[2]][randPos[3]].append(choice)
                break

            beenFilledIn = False
        print(newGrid)        
        completed = checkGridIsCompleted(newGrid,3)
    return newGrid

                            
#newGrid = generateCompletedGrid()
#print(newGrid)

'''perhaps generate some random numbers and then fill in the rest from randomly choosing the least possible numbers (or both, generate 1 and then fill some in and generate again (but that might be slower))'''
'''need to check for possible invalid inputs when randomly filling in so perhaps utilise the find numbers to remove function?'''
from Sudoku_Solver import *
grid = [[[[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [2], [6]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5]]], [[[5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7]], [[4], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9]], [[8], [6], [2]]], [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]]], [[[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [8], [7]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]], [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [2], [4]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [8]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]], [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [3]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9], [7]], [[6], [5], [4]]]], [[[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [6], [9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [4], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]], [[[2], [1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]], [[[4], [3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]]]]
formatSudokuGridTo2D(grid,3,"19")
