#~~~~~ Sudoku GUI ~~~~~#

import pygame, time, copy
from Sudoku_Generator_v2 import generateCompletedGrid
from Sudoku_Creator_v2 import createNewPuzzle
from Sudoku_Solver import formatSudokuGridTo5DFrom2D, formatSudokuGridTo2DFrom5D

def formatSudokuGridTo3DFrom2D(gridArray,size):    # for converting the array to 3D for use in the main program
    gridArray3D = []
    for i in range(size):
        tempArray1 = []
        for j in range(size):
            tempArray2 = []
            for k in range(1):
                tempArray2.append(gridArray[i][j])
            tempArray1.append(tempArray2)
        gridArray3D.append(tempArray1)
    return gridArray3D

def addUndoArray(gridArray3D,size):    # adds an undo array at position 1 to store the necessary things used for undoing the moves
    for i in range(size):
        for j in range(size):
            if gridArray3D[i][j][0] == 0:
                gridArray3D[i][j].append([])
    return gridArray3D

def findTimeTaken(timeTaken):    # finds the time taken in hours, minutes and seconds, which is more human readable than just seconds
    mins,secs = divmod(timeTaken,60)
    hrs,mins = divmod(mins,60)
    return hrs, mins, secs

def flipValue(prevValue):    # flips the on/off value used for the toggle buttons
    if prevValue == "On":
        return "Off"
    return "On"

def flipBooleanValue(prevValue):    # flips the boolean value used for the show answers
    if prevValue == True:
        return False
    return True

def runMainProgramGUI():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,687))
    pygame.display.set_caption("Sudoku Game by Mattyou Quinn")

    white = (255,255,255)    # use for backgroundColour, mainButtonColour and squareColour
    black = (20,20,20)
    lightGrey = (225,225,225)
    squareColourHover = (220,250,255)
    squareColourPressed = (150,220,240)
    keypadColour = (170,170,170)
    keypadColourPressed = (200,200,200)
    otherButtonColour = (65,150,240)    # for the new games buttons etc
    otherButtonColourHover = (95,170,255)
    otherButtonColourPressed = (60,140,225)
    smallLineColour = (170,170,170)
    filledInNumberColour = (30,134,232)
    wrongSquareColour = (255,135,135)
    answerColour = (26,217,33)

    gridNumbersFont = pygame.font.SysFont('lucidasansregular',43)
    newGameButtonsFont = pygame.font.SysFont('arial',23)
    difficultyFont = pygame.font.SysFont('lucidasansregular',15)
    keypadNumbersFont = pygame.font.SysFont('lucidasansregular',60)
    keypadTextFont = pygame.font.SysFont('arial',30)
    showMistakesFont = pygame.font.SysFont('arial',22)
    notesFont = pygame.font.SysFont('lucidasansregular',20)

    difficulty = "Please select game"
    enableNotes = "Off"    # not boolean so it can be used in the button text saving 3 lines and doesnt affect functionality (same for show mistakes)
    showMistakes = "Off"
    finished = False
    squareClicked = False
    needToFillIn = False
    needToErase = False
    solvePls = False
    needToShowHint = False
    undoMove = False
    restartGame = False
    showAnswer = False
    moveSquareUp = False
    moveSquareDown = False
    moveSquareLeft = False
    moveSquareRight = False
    puzzleGrid = 0
    coords = 0
    hintsShown = 0
    finishGrid = 0    # so the grid actually fills in the last square instead of going straight to the finsihing screen
    keypad = [[1,2,3],[4,5,6],[7,8,9]]
    difficultyLevels = ["Easy","Medium","Hard","Expert",4,3,2,1]

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pressedQuit = True
            if event.type == pygame.KEYDOWN:    # takes keyboard inputs (dont really know how to make this any shorter)
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
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
                if event.key == pygame.K_h:    # keyboard shortcuts
                    needToShowHint = True
                if event.key == pygame.K_e:
                    needToErase = True
                if event.key == pygame.K_u:
                    undoMove = True
                if event.key == pygame.K_r:
                    restartGame = True
                if event.key == pygame.K_s:
                    solvePls = True
                if event.key == pygame.K_UP:
                    moveSquareUp = True
                if event.key == pygame.K_DOWN:
                    moveSquareDown = True
                if event.key == pygame.K_LEFT:
                    moveSquareLeft = True
                if event.key == pygame.K_RIGHT:
                    moveSquareRight = True
                if event.key == pygame.K_n:
                    enableNotes = flipValue(enableNotes)
                if event.key == pygame.K_m:
                    showMistakes = flipValue(showMistakes)
                if event.key == pygame.K_a:
                    showAnswer = flipBooleanValue(showAnswer)
                    
        mousePos = pygame.mouse.get_pos()    # gets the mouse position
        gameDisplay.fill(white)    # background

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

        pygame.draw.rect(gameDisplay,black,(30,30,541,541),width=2)    # draws the main box (here for layering reasons)

        for i in range(2):    # draws the buttons for the new games
            for j in range(2):
                pygame.draw.rect(gameDisplay,otherButtonColour,(179*i+621,60*j+32,160,50),border_radius=4)
                if (179*i+621) < mousePos[0] < (179*i+781) and (60*j+32) < mousePos[1] < (60*j+82):
                    pygame.draw.rect(gameDisplay,otherButtonColourHover,(179*i+621,60*j+32,160,50),border_radius=4)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(gameDisplay,otherButtonColourPressed,(179*i+621,60*j+32,160,50),border_radius=4)
                        difficulty = difficultyLevels[2*j+i]
                        answerGrid = generateCompletedGrid()    # generates a complete grid to make the puzzle from
                        tempGrid  = copy.deepcopy(answerGrid)
                        answerGrid = formatSudokuGridTo3DFrom2D(answerGrid,9)
                        puzzleGrid = formatSudokuGridTo3DFrom2D(createNewPuzzle(tempGrid,difficultyLevels[4+(2*j+i)]),9)    # just be careful using v1 creator as it returns it as uses 5D as opposed to 2D
                        puzzleGrid = addUndoArray(puzzleGrid,9)
                        origGrid = copy.deepcopy(puzzleGrid)
                        showAnswer = False
                        undoPos = 0
                        startTime = time.time()
        gameDisplay.blit(newGameButtonsFont.render("New easy game",False,black),(636,42))    # adds the text to the buttons (seperate to ensure the text is in the right place)
        gameDisplay.blit(newGameButtonsFont.render("New medium game",False,black),(800,42))
        gameDisplay.blit(newGameButtonsFont.render("New hard game",False,black),(636,102))
        gameDisplay.blit(newGameButtonsFont.render("New expert game",False,black),(808,102))

        gameDisplay.blit(difficultyFont.render("Difficulty:",False,black),(720,6))    # displays the difficulty text, at the top
        gameDisplay.blit(difficultyFont.render(difficulty,False,smallLineColour),(795,6))

        gameDisplay.blit(difficultyFont.render("Erase:",False,black),(30,593))     # draws the keyboard shortcuts in the bottom left of the screen
        gameDisplay.blit(difficultyFont.render("E",False,smallLineColour),(78,593))
        gameDisplay.blit(difficultyFont.render("Undo:",False,black),(30,613))
        gameDisplay.blit(difficultyFont.render("U",False,smallLineColour),(76,613))
        gameDisplay.blit(difficultyFont.render("Toggle Notes:",False,black),(30,633))
        gameDisplay.blit(difficultyFont.render("N",False,smallLineColour),(133,633))
        gameDisplay.blit(difficultyFont.render("Show/Hide Answer:",False,black),(30,653))    # hard to make this shorter as they all need to be in specific places
        gameDisplay.blit(difficultyFont.render("A",False,smallLineColour),(172,653))
        gameDisplay.blit(difficultyFont.render("Hint:",False,black),(200,593))
        gameDisplay.blit(difficultyFont.render("H",False,smallLineColour),(238,593))
        gameDisplay.blit(difficultyFont.render("Restart:",False,black),(200,613))
        gameDisplay.blit(difficultyFont.render("R",False,smallLineColour),(258,613))
        gameDisplay.blit(difficultyFont.render("Toggle Show Mistakes:",False,black),(200,633))
        gameDisplay.blit(difficultyFont.render("M",False,smallLineColour),(366,633))
        gameDisplay.blit(difficultyFont.render("Navigate:",False,black),(200,653))
        gameDisplay.blit(difficultyFont.render("Arrow Keys",False,smallLineColour),(269,653))

        for i in range(3):    # the key pad (hovering)
            for j in range(3):
                if (113*i+621) < mousePos[0] < (113*i+734) and (96*j+152) < mousePos[1] < (96*j+248):    # for hovering (here so doesn't interfere with the other lines)
                    pygame.draw.rect(gameDisplay,lightGrey,(113*i+621,96*j+152,113,96))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(gameDisplay,keypadColourPressed,(113*i+621,96*j+152,113,96))
                        needToFillIn = True
                        numPressed = keypad[j][i]    # if the keypad button is pressed, the number (from an array in the same format) is recorded
        for i in range(2):    # the buttons at the bottom (hovering)
            for j in range(2):
                if (170*i+621) < mousePos[0] < (170*i+791) and (66*j+440) < mousePos[1] < (66*j+506):
                    pygame.draw.rect(gameDisplay,lightGrey,(170*i+621,66*j+440,170,66))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(gameDisplay,keypadColourPressed,(170*i+621,66*j+440,170,66))
                        if i == 0 and j == 1:
                            undoMove = True
                        if i == 0 and j == 0:
                            needToErase = True     # the other buttons can just be marked as needing to do
                        if i == 1 and j == 1:
                            restartGame = True
                        if i == 1 and j == 0:
                            needToShowHint = True            
        pygame.draw.rect(gameDisplay,keypadColour,(621,152,339,419),width=2)    # main keypad box
        for i in range(3):
            pygame.draw.line(gameDisplay,keypadColour,start_pos=(621,96*i+248),end_pos=(960,96*i+248),width=2)     # vertical lines
            pygame.draw.line(gameDisplay,keypadColour,start_pos=(113*i+621,152),end_pos=(113*i+621,440),width=2)    # horizontal lines
        pygame.draw.line(gameDisplay,keypadColour,start_pos=(621,506),end_pos=(960,506),width=2)    # buttons at the bottom of the keypad
        pygame.draw.line(gameDisplay,keypadColour,start_pos=(791,440),end_pos=(791,571),width=2)
        for i in range(3):
            for j in range(3):
                gameDisplay.blit(keypadNumbersFont.render(str(keypad[i][j]),False,black),(113*j+657,96*i+165))    # adds numbers to the keypad       
        gameDisplay.blit(keypadTextFont.render("Erase",False,black),(675,455))    # draws the text for the other keypad buttons
        gameDisplay.blit(keypadTextFont.render("Hint",False,black),(850,455))
        gameDisplay.blit(keypadTextFont.render("Undo",False,black),(677,520))
        gameDisplay.blit(keypadTextFont.render("Restart",False,black),(837,520))

        for i in range(9):
            for j in range(9):
                if (60*i+32) < mousePos[0] < (60*i+90) and (60*j+32) < mousePos[1] < (60*j+90):
                    pygame.draw.rect(gameDisplay,squareColourHover,(60*i+32,60*j+32,58,58))    # hovering over the grid square
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        squareClicked = True
                        coords = [(60*i+32),(60*j+32)]    # if the grid square is clicked on, its coordinates are marked
            
        if puzzleGrid != 0:
            for i in range(9):    # draws the numbers in the grid
                for j in range(9):
                    if showMistakes == "On" and origGrid[j][i][0] == 0 and puzzleGrid[j][i][0] != 0 and puzzleGrid[j][i][0] != answerGrid[j][i][0]:
                        pygame.draw.rect(gameDisplay,wrongSquareColour,(60*i+32,60*j+32,58,58))
                    if puzzleGrid[j][i][0] == 0:
                        if showAnswer == False:
                            numberToShow = ""     # nothing is drawn in the square if it is being marked as empty
                        else:
                            numberToShow = str(answerGrid[j][i][0])
                    else:
                        numberToShow = str(puzzleGrid[j][i][0])
                    if showAnswer == True:
                        if puzzleGrid[j][i][0] == 0:
                            gridNumbers = gridNumbersFont.render(numberToShow,False,answerColour)    # if the show answer is toggled, the correct number will also be displayed in green
                        elif origGrid[j][i][0] == 0:
                            gridNumbers = gridNumbersFont.render(numberToShow,False,filledInNumberColour)
                        else:
                            gridNumbers = gridNumbersFont.render(numberToShow,False,black)
                    else:
                        if origGrid[j][i][0] == 0:
                            gridNumbers = gridNumbersFont.render(numberToShow,False,filledInNumberColour)    # the numbers the user fills in are coloured in blue
                        else:
                            gridNumbers = gridNumbersFont.render(numberToShow,False,black)    # the numbers given are coloured in black
                    gameDisplay.blit(gridNumbers,(60*i+48,60*j+34))
                    if len(puzzleGrid[j][i]) > 1 and puzzleGrid[j][i][0] == 0 and showAnswer == False:   # displays the notes if there are any
                        toDisplay = [0,0,0,0,0,0,0,0,0]    # this is just to make it display nicer
                        for m in range(2,len(puzzleGrid[j][i])):
                            toDisplay[puzzleGrid[j][i][m]-1] = puzzleGrid[j][i][m]    # replaces a zero with the note in the correct place
                        for k in range(3):
                            for l in range(3):
                                if toDisplay[3*k+l] != 0:    # having the toDisplay array means for instance 5 will always be displayed in the middle, 9 in the bottom right etc etc
                                    numberToShow = str(toDisplay[3*k+l])
                                    noteNumbers = notesFont.render(numberToShow,False,filledInNumberColour)
                                    gameDisplay.blit(noteNumbers,(60*i+30+(20*l+5),60*j+30+(20*k-1)))

        for i in range(3):    # draws the buttons at the very bottom of the screen
            pygame.draw.rect(gameDisplay,keypadColour,(185*i+421,591,170,66),width=2)
            if (185*i+421) < mousePos[0] < (185*i+591) and 591 < mousePos[1] < 657:
                pygame.draw.rect(gameDisplay,lightGrey,(185*i+423,593,167,63))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(gameDisplay,keypadColourPressed,(185*i+423,593,167,63))     # have to be smaller squares so they dont over lap and are layered correctly
                    if i == 0:
                        showAnswer = flipBooleanValue(showAnswer)
                    if i == 1:
                        enableNotes = flipValue(enableNotes)
                    if i == 2:
                        showMistakes = flipValue(showMistakes)
        if showAnswer == False:
            gameDisplay.blit(keypadTextFont.render("Show Answer",False,black),(432,607))
        else:
            gameDisplay.blit(keypadTextFont.render("Hide Answer",False,black),(432,607))
        gameDisplay.blit(keypadTextFont.render("Notes: "+enableNotes,False,black),(637,607))
        gameDisplay.blit(showMistakesFont.render("Show Mistakes: "+showMistakes,False,black),(798,612))
                                    
        if enableNotes == "Off":    # if notes are off, the square will be filled in
            if needToFillIn == True:
                if coords != 0 and puzzleGrid != 0 and origGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] == 0:
                    undoPos += 1
                    prevNumber = 0
                    if puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] != 0:
                        prevNumber = puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0]
                    puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] = numPressed     # the 0 marking the square as not filled in is replaced by the number pressed
                    if prevNumber != 0:    # so undoing doesnt skip any numbers which were directly writtin over
                        puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append(undoPos)
                        puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append("erasedMainNumber")
                        puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append(prevNumber)
                        undoPos += 1
                    puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append(undoPos)
                    puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append("filledInMainNumber")
                    puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append(numPressed)
                needToFillIn = False
        else:
            if needToFillIn == True:
                if coords != 0 and puzzleGrid != 0 and puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] == 0 and showAnswer == False:
                    if numPressed in puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)]:
                        puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].remove(numPressed)    # if the number is pressed a second time, it will be removed (so user can remove a note by clicking the number again)
                    else:
                        puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].append(numPressed)    # if notes are on, any numbers pressed will be appended on, indicating notes
                needToFillIn = False

        if needToErase == True:
            if coords != 0 and puzzleGrid != 0 and origGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] == 0:     # only erases filled in numbers
                undoPos += 1
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append(undoPos)
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append("erasedMainNumber")
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1].append(puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0])
                squareUndoArray = copy.deepcopy(puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][1])
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].clear()    # cant just set it equal to 0 as the notes would not be erased
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].append(0)
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].append(squareUndoArray)
            needToErase = False

        if needToShowHint == True:
            if coords != 0 and puzzleGrid != 0 and origGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] == 0 and puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] != answerGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0]:
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] = answerGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0]    # gets the number for the square from the answer array if hint is needed
                hintsShown += 1
            needToShowHint = False

        if solvePls == True:
            if puzzleGrid != 0:
                puzzleGrid = copy.deepcopy(answerGrid)
            solvePls = False

        if restartGame == True:
            if puzzleGrid != 0:
                puzzleGrid = copy.deepcopy(origGrid)    # if the user wants to restart, the puzzle grid will just be set to the original grid
            restartGame = False

        if moveSquareUp == True:
            if coords != 0 and 0 < int((coords[1]-32)/60) <= 8:
                coords[1] = coords[1] - 60
            moveSquareUp = False

        if moveSquareDown == True:
            if coords != 0 and 0 <= int((coords[1]-32)/60) < 8:
                coords[1] = coords[1] + 60
            moveSquareDown = False

        if moveSquareLeft == True:
            if coords != 0 and 0 < int((coords[0]-32)/60) <= 8:
                coords[0] = coords[0] - 60
            moveSquareLeft = False

        if moveSquareRight == True:
            if coords != 0 and 0 <= int((coords[0]-32)/60) < 8:
                coords[0] = coords[0] + 60
            moveSquareRight = False

        if undoMove == True:
            if coords != 0 and puzzleGrid != 0 and undoPos > 0:
                lastChanged = [0]
                for i in range(9):
                    for j in range(9):
                        if origGrid[j][i][0] == 0:
                            for k in range(0,len(puzzleGrid[j][i][1]),3):
                                if puzzleGrid[j][i][1][k] > lastChanged[0]:     # loops through to find the position with the highest undoPos, indicating it was the most recently filled in
                                    lastChanged.clear()
                                    lastChanged.append(puzzleGrid[j][i][1][k])
                                    lastChanged.append(j)
                                    lastChanged.append(i)
                                    lastChanged.append(k)
                if puzzleGrid[lastChanged[1]][lastChanged[2]][1][lastChanged[3]+1] == "erasedMainNumber":
                    puzzleGrid[lastChanged[1]][lastChanged[2]][0] = puzzleGrid[lastChanged[1]][lastChanged[2]][1][lastChanged[3]+2]
                elif puzzleGrid[lastChanged[1]][lastChanged[2]][1][lastChanged[3]+1] == "filledInMainNumber":
                    puzzleGrid[lastChanged[1]][lastChanged[2]][0] = 0
                for i in range(3):
                    puzzleGrid[lastChanged[1]][lastChanged[2]][1].pop(lastChanged[3])
                undoPos -= 1
            undoMove = False
        
        if puzzleGrid != 0:
            counter = 0
            for i in range(9):
                for j in range(9):
                    if puzzleGrid[i][j][0] == answerGrid[i][j][0]:    # checks the grid is correct
                        counter += 1
            if counter == 81:
                finishTime = time.time()
                finishGrid += 1
                if finishGrid == 4:    # just so the last number is actually displayed (makes the screen update itself with the last number before going onto quitting)
                    time.sleep(1.5)
                    pressedQuit = False
                    finished = True                
        pygame.display.flip()    # updates the display
        time.sleep(0.082)    # time delay does hinder the visual performance ever so slightly but it was necessary for the buttons to function correctly

    pygame.quit()
    if pressedQuit == True:
        return None,None    # returns nothing if the user just quit
    return hintsShown, int(round(finishTime - startTime,0))

def runFinishingScreenGUI(hintsShown,hours,minutes,seconds):
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,601))
    pygame.display.set_caption("Sudoku Game by Mattyou Quinn")

    white = (255,255,255)
    black = (20,20,20)
    grey = (100,100,100)
    buttonColour = (65,150,240)
    buttonColourHover = (95,170,255)
    buttonColourPressed = (60,140,225)
    lightGrey = (170,170,170)

    congratsFont = pygame.font.SysFont('lucidasansregular',70)
    statsFont = pygame.font.SysFont('lucidasansregular',27)
    buttonsFont = pygame.font.SysFont('lucidasansregular',32)

    finished = False

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuePlaying = False    # if the user just quits, it is assumed they don't want to play again
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:    # keyboard shortcuts to quit or play again
                    continuePlaying = True
                    finished = True
                if event.key == pygame.K_q:
                    continuePlaying = False
                    finished = True

        mousePos = pygame.mouse.get_pos()
        gameDisplay.fill(white)
        gameDisplay.blit(congratsFont.render("Congratulations!",False,grey),(210,100))    # draws all the text on the screen
        gameDisplay.blit(statsFont.render("Time taken:",False,black),(320,200))
        gameDisplay.blit(statsFont.render(hours+"h "+minutes+"m "+seconds+"s",False,lightGrey),(490,200))
        gameDisplay.blit(statsFont.render("Hints shown:",False,black),(303,250))
        gameDisplay.blit(statsFont.render(hintsShown,False,lightGrey),(545,250))
        
        for i in range(2):    # draws the buttons for play again and quit
            pygame.draw.rect(gameDisplay,buttonColour,(230*i+280,310,190,60),border_radius=4)
            if (230*i+280) < mousePos[0] < (230*i+470) and 310 < mousePos[1] < 370:
                pygame.draw.rect(gameDisplay,buttonColourHover,(230*i+280,310,190,60),border_radius=4)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(gameDisplay,buttonColourPressed,(230*i+280,310,190,60),border_radius=4)
                    if i == 0:
                        continuePlaying = True     # when i is 0, the button drawn is the play again one
                    else:
                        continuePlaying = False
                    finished = True                    
        gameDisplay.blit(buttonsFont.render("Play Again",False,black),(295,320))    # adds the text to the buttons
        gameDisplay.blit(buttonsFont.render("Quit Game",False,black),(523,320))

        pygame.display.flip()
        time.sleep(0.082)
        
    pygame.quit()
    return continuePlaying

def initialiseGameGUI():     # when run, just check the window hasn't appeared under other open windows
    playAgain = True
    while playAgain:    # loops around as long as the user wants to play again
        hintsShown, timeTaken = runMainProgramGUI()
        if hintsShown == None or timeTaken == None:
            playAgain = False
        else:
            hrs, mins, secs = findTimeTaken(timeTaken)
            playAgain = runFinishingScreenGUI(str(hintsShown),str(hrs),str(mins),str(secs))
    print("thank you for doing sudoku-y stuff")
