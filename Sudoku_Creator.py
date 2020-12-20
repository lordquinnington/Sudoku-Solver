#~~~~~ Sudoku Creator ~~~~~#

import random, csv, time
from Sudoku_Generator import generateCompletedGrid
from Sudoku_Solver import formatSudokuGridTo5DFrom2D, print5DSudokuGrid, formatSudokuGridTo2DFrom5D

################################################ formatting functions ################################################

def writeNewGridToCSV(gridArray2D,gridNumber):
    with open("Sudoku_Grid_New_"+gridNumber+".csv","w",newline='') as completedGridFile:
        toWrite = csv.writer(completedGridFile,delimiter=',')
        for row in gridArray2D:
            toWrite.writerow(row)
    print("written to file")

################################################ creating functions ################################################

def removeRandomNumber(gridArray):
    zero = True
    while zero:
        options = [0,1,2]
        a = random.choice(options)
        b = random.choice(options)
        c = random.choice(options)
        d = random.choice(options)
        if gridArray[a][b][c][d][0] != 0:
            gridArray[a][b][c][d][0] = 0
            zero = False
        else:
            zero = True
    return gridArray
    
def createNewPuzzle(newGrid,difficulty):
    squaresToKeep = random.randint((25+5*difficulty),((25+5*difficulty)+5))
    for i in range(81-squaresToKeep):
        newGrid = removeRandomNumber(newGrid)
    return newGrid

def initialiseCreating():
    gridNumber = input("enter a grid number >")
    validInput = False
    while not validInput:
        try:
            difficulty = int(input("enter a difficulty: \n1) expert \n2) hard \n3) medium \n4) easy \noption>"))
            if difficulty >= 1 and difficulty <= 4:
                validInput = True
            else:
                print("enter a valid input")
                validInput = False
        except ValueError:
            print("enter a valid option")
            validInput = False
    completedGrid = formatSudokuGridTo5DFrom2D(generateCompletedGrid(),3)
    startTime = time.time()
    newPuzzle = createNewPuzzle(completedGrid,difficulty-1)
    finishTime = time.time()
    print("new grid created (in "+str(round(finishTime-startTime,3))+"s):")
    print5DSudokuGrid(newPuzzle,3)
    writeNewGridToCSV(formatSudokuGridTo2DFrom5D(newPuzzle,3),gridNumber)
