#~~~~~ Sudoku Solver GUI ~~~~~#

import pygame, time, csv
from Sudoku_Solver import formatSudokuGridTo5DFrom2D, formatSudokuGridTo2DFrom5D, solve, writeCompletedGridToCSV, findNumbersToRemove

def createBlank2DGrid(size):    # function to create a blank 2D grid array for the user to edit
    gridArray2D = []
    for i in range(size):
        tempArray1 = []
        for j in range(size):
            tempArray1.append(0)
        gridArray2D.append(tempArray1)
    return gridArray2D

def checkInitialGridIsValid(gridArray,squareSize):     # function to check the user has entered an initially valid grid (ie theres not two 5's in the same row)
    for i in range(squareSize):
        for j in range(squareSize):
            for k in range(squareSize):
                for l in range(squareSize):
                    if gridArray[i][j][k][l][0] != 0:
                        invalidNumbers = findNumbersToRemove(gridArray,squareSize,i,j,k,l)
                        counter = 0
                        for m in range(len(invalidNumbers)):
                            if invalidNumbers[m] == gridArray[i][j][k][l][0]:    # checks how many times the number appears
                                counter += 1
                        if counter > 3:    # the find numbers to remove function will return 3 of the number being looked at, as that square is in all 3 of the row/column/square
                            return False    # returns fase if it shows up elsewhere
    return True    # returns true if the grid is initially valid

def findGridName():     # finds the next available grid name to call the new file (to avoid overwriting previous grids)
    available = False
    x = 1
    while not available:
        try:
            open("Sudoku_Grid_"+str(x)+".csv","x")
            print("file is grid "+str(x))
            return str(x)
        except FileExistsError:
            x += 1

def writeUserGridToCSV(gridArray2D,gridNumber):    # function to write the user grid to a file 
    with open("Sudoku_Grid_"+gridNumber+".csv","w",newline='') as gridFile:
        toWrite = csv.writer(gridFile,delimiter=',')
        for row in gridArray2D:
            toWrite.writerow(row)
    
def runMainProgramGUI():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,601))
    pygame.display.set_caption("Sudoku Solver by Mattyou Quinn")

    white = (255,255,255)
    black = (20,20,20)
    smallLineColour = (170,170,170)
    lightGrey = (225,225,225)
    errorBoxColour = (242,242,242)
    errorBoxOutlineColour = (255,135,135)
    squareColourHover = (220,250,255)
    squareColourPressed = (150,220,240)
    keypadColour = (170,170,170)
    keypadColourPressed = (200,200,200)
    otherButtonColour = (65,150,240)
    otherButtonColourHover = (95,170,255)
    otherButtonColourPressed = (60,140,225)
    solvedColour = (26,217,33)

    gridNumbersFont = pygame.font.SysFont('lucidasansregular',43)
    keypadNumbersFont = pygame.font.SysFont('lucidasansregular',60)
    keypadTextFont = pygame.font.SysFont('arial',30)
    solveButtonTextFont = pygame.font.SysFont('arial',40)
    otherTextFont = pygame.font.SysFont('lucidasansregular',22)
    errorBoxFont1 = pygame.font.SysFont('arial',70)
    errorBoxFont2 = pygame.font.SysFont('arial',25)

    timeTaken = "N/A"     # set as N/A as this is what will be displayed
    savedAs = "N/A"
    finished = False
    squareClicked = False
    needToErase = False
    restartGrid = False
    solveGrid = False
    moveSquareUp = False
    moveSquareDown = False
    moveSquareLeft = False
    moveSquareRight = False
    needToFillIn = False
    solved = False
    notPossible = False
    coords = 0
    userGrid = 0
    solvedGrid = 0
    keypad = [[1,2,3],[4,5,6],[7,8,9]]

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:     # can use the keyboard to input numebrs
                    numPressed = 1
                    needToFillIn = True
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:     # can use the keypad too
                    numPressed = 2
                    needToFillIn = True
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    numPressed = 3
                    needToFillIn = True
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    numPressed = 4
                    needToFillIn = True
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    numPressed = 5
                    needToFillIn = True
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    numPressed = 6
                    needToFillIn = True
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    numPressed = 7
                    needToFillIn = True
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    numPressed = 8
                    needToFillIn = True
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    numPressed = 9
                    needToFillIn = True
                if event.key == pygame.K_e:    # keyboard shortcuts
                    needToErase = True
                if event.key == pygame.K_r:
                    restartGrid = True
                if event.key == pygame.K_s:
                    solveGrid = True
                if event.key == pygame.K_RETURN:    # for the error message with the button
                    notPossible = False
                if event.key == pygame.K_UP:     # to navigate with the arrow keys
                    moveSquareUp = True
                if event.key == pygame.K_DOWN:
                    moveSquareDown = True
                if event.key == pygame.K_LEFT:
                    moveSquareLeft = True
                if event.key == pygame.K_RIGHT:
                    moveSquareRight = True

        mousePos = pygame.mouse.get_pos()    # gets the mouse position on the window
        gameDisplay.fill(white)    # sets the background to white

        if userGrid == 0:
            userGrid = createBlank2DGrid(9)     # if there is currently no user grid, one will be created

        if squareClicked == True:    # square after they have been clicked (here so the drawing of the big square goes behind the lines)
            for i in range(3):
                for j in range(3):
                    if (180*i+30) < coords[0] < (180*i+210) and (180*j+30) < coords[1] < (180*j+210):
                        pygame.draw.rect(gameDisplay,lightGrey,(180*i+30,180*j+30,180,180))     # big square
            for i in range(9):
                pygame.draw.rect(gameDisplay,lightGrey,(coords[0],60*i+32,58,58))    # column
                pygame.draw.rect(gameDisplay,lightGrey,(60*i+32,coords[1],58,58))    # row
            pygame.draw.rect(gameDisplay,squareColourPressed,(coords[0],coords[1],58,58))    # square selected

        for j in range(8):    # small grid lines
            pygame.draw.line(gameDisplay,smallLineColour,start_pos=(60*j+90,30),end_pos=(60*j+90,571),width=2)
            pygame.draw.line(gameDisplay,smallLineColour,start_pos=(30,60*j+90),end_pos=(571,60*j+90),width=2)
        for i in range(2):    # big grid lines
            pygame.draw.line(gameDisplay,black,start_pos=(180*(i+1)+30,30),end_pos=(180*(i+1)+30,571),width=2)
            pygame.draw.line(gameDisplay,black,start_pos=(30,180*(i+1)+30),end_pos=(571,180*(i+1)+30),width=2)

        pygame.draw.rect(gameDisplay,black,(30,30,541,541),width=2)     # main square box

        for i in range(3):    # the key pad (hovering)
            for j in range(3):
                if (113*i+621) < mousePos[0] < (113*i+734) and (96*j+30) < mousePos[1] < (96*j+126):    # for hovering (here so doesn't interfere with the other lines)
                    pygame.draw.rect(gameDisplay,lightGrey,(113*i+621,96*j+30,113,96))
                    if event.type == pygame.MOUSEBUTTONDOWN and notPossible == False:
                        pygame.draw.rect(gameDisplay,keypadColourPressed,(113*i+621,96*j+30,113,96))
                        needToFillIn = True
                        numPressed = keypad[j][i]    # if the keypad button is pressed, the number (from an array in the same format) is recorded - to avoid a lot of if statements
                        
        for i in range(2):
            if (170*i+621) < mousePos[0] < (170*i+791) and (318) < mousePos[1] < (384):
                pygame.draw.rect(gameDisplay,lightGrey,(170*i+621,318,170,66))
                if event.type == pygame.MOUSEBUTTONDOWN and notPossible == False:
                    pygame.draw.rect(gameDisplay,keypadColourPressed,(170*i+621,318,170,66))
                    if i == 0:
                        needToErase = True    # if i is 0 then the mouse must have been hovering over the erase button
                    if i == 1:
                        restartGrid = True

        pygame.draw.rect(gameDisplay,keypadColour,(621,30,339,353),width=2)    # main keypad box
        pygame.draw.line(gameDisplay,keypadColour,start_pos=(791,318),end_pos=(791,382),width=2)
        gameDisplay.blit(keypadTextFont.render("Erase",False,black),(673,332))    # adds the text to the keypad boxes
        gameDisplay.blit(keypadTextFont.render("Restart",False,black),(833,332))
        
        for i in range(3):    # draws the lines for the number pad
            pygame.draw.line(gameDisplay,keypadColour,start_pos=(621,96*i+126),end_pos=(960,96*i+126),width=2)     # vertical lines
            pygame.draw.line(gameDisplay,keypadColour,start_pos=(113*i+621,30),end_pos=(113*i+621,318),width=2)    # horizontal lines
        
        for i in range(3):
            for j in range(3):
                gameDisplay.blit(keypadNumbersFont.render(str(keypad[i][j]),False,black),(113*j+657,96*i+43))    # adds numbers to the keypad

        pygame.draw.rect(gameDisplay,otherButtonColour,(671,409,240,66),border_radius=8)      # the big blue solve button
        if solved == False:
            if 671 < mousePos[0] < 911 and 409 < mousePos[1] < 474:
                pygame.draw.rect(gameDisplay,otherButtonColourHover,(671,409,240,66),border_radius=8)
                if event.type == pygame.MOUSEBUTTONDOWN and notPossible == False:
                    pygame.draw.rect(gameDisplay,otherButtonColourPressed,(671,409,240,66),border_radius=8)
                    solveGrid = True
            gameDisplay.blit(solveButtonTextFont.render("Solve",False,black),(745,419))
        else:
            gameDisplay.blit(solveButtonTextFont.render("Solved!",False,black),(737,419))    # if the grid has been solved, all the button will do is inform them it has been solved

        gameDisplay.blit(otherTextFont.render("Erase:",False,black),(621,495))     # the list of keyboard shortcuts at the bottom of the screen
        gameDisplay.blit(otherTextFont.render("E",False,smallLineColour),(688,495))
        gameDisplay.blit(otherTextFont.render("Restart:",False,black),(621,522))
        gameDisplay.blit(otherTextFont.render("R",False,smallLineColour),(704,522))
        gameDisplay.blit(otherTextFont.render("Solve:",False,black),(621,549))
        gameDisplay.blit(otherTextFont.render("S",False,smallLineColour),(687,549))
        gameDisplay.blit(otherTextFont.render("Navigate:",False,black),(750,495))
        gameDisplay.blit(otherTextFont.render("Arrow Keys",False,smallLineColour),(851,495))
        gameDisplay.blit(otherTextFont.render("Time Taken:",False,black),(750,522))
        if timeTaken == "N/A":
            gameDisplay.blit(otherTextFont.render(timeTaken,False,smallLineColour),(885,522))    # if the grid hasn't been solved, N/A is displayed for the time (same with saved as)
        else:
            gameDisplay.blit(otherTextFont.render(str(timeTaken)+"s",False,smallLineColour),(885,522))    # if the grid has been solved, the user will be informed as to how long it took
        gameDisplay.blit(otherTextFont.render("Saved As:",False,black),(750,549))
        if savedAs == "N/A":
            gameDisplay.blit(otherTextFont.render(savedAs,False,smallLineColour),(853,549))
        else:
            gameDisplay.blit(otherTextFont.render("Grid "+str(savedAs),False,smallLineColour),(853,549))

        for i in range(9):
            for j in range(9):
                if (60*i+32) < mousePos[0] < (60*i+90) and (60*j+32) < mousePos[1] < (60*j+90):
                    pygame.draw.rect(gameDisplay,squareColourHover,(60*i+32,60*j+32,58,58))    # hovering over the grid square in the sudoku grid
                    if event.type == pygame.MOUSEBUTTONDOWN and notPossible == False:
                        squareClicked = True
                        coords = [(60*i+32),(60*j+32)]    # if the grid square is clicked on, its coordinates are marked

        if userGrid != 0:
            for i in range(9):
                for j in range(9):     # displays the numbers if the user grid exists
                    if userGrid[j][i] == 0 and solvedGrid == 0:
                        gridNumbers = gridNumbersFont.render("",False,black)    # adds nothing to spaces marked as empty by the 0
                    elif userGrid[j][i] == 0 and solvedGrid != 0 and solvedGrid != None:
                        gridNumbers = gridNumbersFont.render(str(solvedGrid[j][i]),False,solvedColour)    # any solved spaces will be drawn in in green
                    else:
                        gridNumbers = gridNumbersFont.render(str(userGrid[j][i]),False,black)    # any user input will be drawn in in black
                    gameDisplay.blit(gridNumbers,(60*i+48,60*j+34))

        if restartGrid == True and notPossible == False:
            if userGrid != 0:
                userGrid = 0     # when it loops back around again, the if statement at the start will make a new grid so don't need to initialise it back to a blank array here
                solvedGrid = 0
                solved = False
            timeTaken = "N/A"    # time taken and saved as are initialised back to N/A
            savedAs = "N/A"
            restartGrid = False

        if needToErase == True and notPossible == False:     # not possible has to be true so that the user cant do anything else while the error message is displayed
            if coords != 0 and userGrid != 0 and solved == False:
                userGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)] = 0     # the square the user clicked on is just set back to 0 if it needs to be erased
            needToErase = False

        if needToFillIn == True and notPossible == False:
            if coords != 0 and userGrid != 0 and solved == False:
                userGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)] = numPressed     # the square the user clicked on is set to whichever number they inputted
            needToFillIn = False

        if solveGrid == True and notPossible == False:
            if userGrid != 0 and solved == False:
                tempGrid = formatSudokuGridTo5DFrom2D(userGrid,3)    # the grid needs to be converted into a 5D array so it can be solved
                validUserGrid = checkInitialGridIsValid(tempGrid,3)
                if validUserGrid == True:
                    startTime = time.time()    # the solving is timed for research purposes 
                    solvedGrid5D = solve(tempGrid,3)
                    finishTime = time.time()
                    if solvedGrid5D != None:    # if the grid doesnt come back as none then it has been solved
                        savedAs = findGridName()     # a grid name is found before it is saved to a csv file
                        writeUserGridToCSV(userGrid,str(savedAs))
                        timeTaken = round(finishTime-startTime,3)     # finds the time taken to display to the user
                        solvedGrid = formatSudokuGridTo2DFrom5D(solvedGrid5D,3)
                        writeCompletedGridToCSV(solvedGrid,str(savedAs))
                        solved = True
                    if solvedGrid5D == None:    # if the grid comes back as none, the algorithm can't solve it
                        notPossible = True     # not possible is set to true to bring up the error message
                else:
                    notPossible = True    # if the grid is not initially valid, the error message is displayed
            solveGrid = False

        if moveSquareUp == True:     # navigating with the keypad
            if coords != 0 and 0 < int((coords[1]-32)/60) <= 8 and notPossible == False:
                coords[1] = coords[1] - 60
            moveSquareUp = False

        if moveSquareDown == True:
            if coords != 0 and 0 <= int((coords[1]-32)/60) < 8 and notPossible == False:
                coords[1] = coords[1] + 60
            moveSquareDown = False

        if moveSquareLeft == True:
            if coords != 0 and 0 < int((coords[0]-32)/60) <= 8 and notPossible == False:
                coords[0] = coords[0] - 60
            moveSquareLeft = False

        if moveSquareRight == True:
            if coords != 0 and 0 <= int((coords[0]-32)/60) < 8 and notPossible == False:
                coords[0] = coords[0] + 60
            moveSquareRight = False

        if notPossible == True:
            pygame.draw.rect(gameDisplay,errorBoxColour,(300,200,400,200),border_radius=10)    # draws the error box 
            pygame.draw.rect(gameDisplay,errorBoxOutlineColour,(298,198,404,204),border_radius=10,width=2)     # adds a red line round it for dramatic effect
            gameDisplay.blit(errorBoxFont1.render("Oh dear...",False,black),(377,207))
            gameDisplay.blit(errorBoxFont2.render("This grid doesn't appear to be solvable.",False,black),(323,287))
            gameDisplay.blit(errorBoxFont2.render("Please change it :)",False,black),(415,317))    # the user needs to change their grid if it is unsolvable
            pygame.draw.rect(gameDisplay,otherButtonColour,(438,350,120,43),border_radius=4)
            if 438 < mousePos[0] < 558 and 350 < mousePos[1] < 393:
                pygame.draw.rect(gameDisplay,otherButtonColourHover,(438,350,120,43),border_radius=4)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(gameDisplay,otherButtonColourPressed,(438,350,120,43),border_radius=4)
                    notPossible = False    # if the user understands they need to change the grid then the error message goes away
            gameDisplay.blit(errorBoxFont2.render("Will do!",False,black),(465,357))

        pygame.display.flip()     # updates the display
        time.sleep(0.082)     # annoying time delay to get the buttons to function correctly

    pygame.quit()
    print("thank you for doing sudoku-y stuff")     # mandatory gratitude giving

def initialiseSolverGUI():
    runMainProgramGUI()
