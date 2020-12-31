#~~~~~ Sudoku Creator ~~~~~#

import random, csv, time
from Sudoku_Generator_v2 import generateCompletedGrid
from Sudoku_Solver import formatSudokuGridTo5DFrom2D, print5DSudokuGrid, formatSudokuGridTo2DFrom5D

################################################ formatting functions ################################################

def writeNewGridToCSV(gridArray2D,gridNumber):    # function to write the new grid to a file 
    with open("Sudoku_Grid_New_"+gridNumber+".csv","w",newline='') as newGridFile:
        toWrite = csv.writer(newGridFile,delimiter=',')
        for row in gridArray2D:
            toWrite.writerow(row)
    print("written to file as grid "+gridNumber)

def findGridName():     # finds the next available grid name to call the new file (to avoid overwriting previous grids)
    available = False
    x = 1
    while not available:
        try:
            open("Sudoku_Grid_New_"+str(x)+".csv","x")
            print("file is grid "+str(x))
            return str(x)
        except FileExistsError:     # if the file already exists then it moves onto the next one
            x += 1

################################################ creating functions ################################################

def removeRandomNumber(gridArray):    # function to remove a random number from the grid
    zero = True
    while zero:
        options = [0,1,2]
        a = random.choice(options)    # generates 4 random coordinates to remove from
        b = random.choice(options)
        c = random.choice(options)
        d = random.choice(options)
        if gridArray[a][b][c][d][0] != 0:    # only removes it if the square is filled in
            gridArray[a][b][c][d][0] = 0
            zero = False
        else:    # if the square is 0, it will have to generate another set of random coordinates
            zero = True
    return gridArray
    
def createNewPuzzle(newGrid,difficulty):    # function to remove the right amount of numbers from the grid
    squaresToKeep = random.randint((25+5*difficulty),((25+5*difficulty)+5))    # decides how many numbers to keep - 40-45 easy, 35-40 medium, 30-35 hard, 25-30 expert
    for i in range(81-squaresToKeep):    # removes the correct amount of numbers
        newGrid = removeRandomNumber(newGrid)
    return newGrid

def initialiseCreating():
    gridNumber = findGridName()
    validInput = False
    while not validInput:    # ensures the user sets the difficulty correctly
        try:
            difficulty = int(input("enter a difficulty: \n1) expert \n2) hard \n3) medium \n4) easy \noption>"))    # user sets the difficulty they would like
            if difficulty >= 1 and difficulty <= 4:
                validInput = True
            else:    # the number entered is out of range of the valid inputs
                print("enter a valid input")
                validInput = False
        except ValueError:    # the input is not an integer
            print("enter a valid option")
            validInput = False
    completedGrid = formatSudokuGridTo5DFrom2D(generateCompletedGrid(),3)
    startTime = time.time()
    newPuzzle = createNewPuzzle(completedGrid,difficulty-1)
    finishTime = time.time()
    print("new grid created (in "+str(round(finishTime-startTime,3))+"s):")
    print5DSudokuGrid(newPuzzle,3)    # prints out the grid
    writeNewGridToCSV(formatSudokuGridTo2DFrom5D(newPuzzle,3),gridNumber)    # writes the grid to a file   
