#~~~~~ Sudoku GUI ~~~~~#

import pygame, time, copy
from Sudoku_Generator import generateCompletedGrid
from Sudoku_Creator import createNewPuzzle
from Sudoku_Solver import formatSudokuGridTo5DFrom2D, formatSudokuGridTo2DFrom5D

def formatSudokuGridTo3DFrom2D(gridArray,size):
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

def runMainProgramGUI():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,601))
    pygame.display.set_caption("Sudoku by Mattyou Quinn")

    white = (255,255,255)    # use for backgroundColour, mainButtonColour and squareColour
    black = (20,20,20)
    lightGrey = (225,225,225)
    squareColourHover = (220,250,255)
    squareColourPressed = (150,220,240)
    keypadColour = (170,170,170)
    keypadColourPressed = (200,200,200)
    otherButtonColour = (65,150,240)    # for the new games buttons etc
    otherButtonColourHover = (95,170,255)
    smallLineColour = (170,170,170)
    filledInNumberColour = (30,134,232)
    wrongSquareColour = (255,135,135)

    gridNumbersFont = pygame.font.SysFont('lucidasansregular',43)
    newGameButtonsFont = pygame.font.SysFont('arial',23)
    difficultyFont = pygame.font.SysFont('lucidasansregular',15)
    keypadNumbersFont = pygame.font.SysFont('lucidasansregular',60)
    keypadTextFont = pygame.font.SysFont('arial',30)
    showMistakesFont = pygame.font.SysFont('arial',22)
    notesFont = pygame.font.SysFont('lucidasansregular',20)

    difficulty = "Please select game"
    enableNotes = "On"    # not boolean so it can be used in the button text saving 3 lines and doesnt affect functionality (same for show mistakes)
    showMistakes = "Off"
    finished = False
    squareClicked = False
    needToFillIn = False
    needToErase = False
    needToShowHint = False
    puzzleGrid = 0
    coords = 0
    keypad = [[1,2,3],[4,5,6],[7,8,9]]
    difficultyLevels = ["Easy","Medium","Hard","Expert",4,3,2,1]

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:    # takes keyboard inputs (dont really know how to make this any shorter)
                if event.key == pygame.K_1:
                    numPressed = 1
                    needToFillIn = True
                if event.key == pygame.K_2:
                    numPressed = 2
                    needToFillIn = True
                if event.key == pygame.K_3:
                    numPressed = 3
                    needToFillIn = True
                if event.key == pygame.K_4:
                    numPressed = 4
                    needToFillIn = True
                if event.key == pygame.K_5:
                    numPressed = 5
                    needToFillIn = True
                if event.key == pygame.K_6:
                    numPressed = 6
                    needToFillIn = True
                if event.key == pygame.K_7:
                    numPressed = 7
                    needToFillIn = True
                if event.key == pygame.K_8:
                    numPressed = 8
                    needToFillIn = True
                if event.key == pygame.K_9:
                    numPressed = 9
                    needToFillIn = True

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
                        difficulty = difficultyLevels[2*j+i]
                        answerGrid = generateCompletedGrid()
                        tempGrid  = formatSudokuGridTo5DFrom2D(answerGrid,3)
                        answerGrid = formatSudokuGridTo3DFrom2D(answerGrid,9)
                        puzzleGrid = formatSudokuGridTo3DFrom2D(formatSudokuGridTo2DFrom5D(createNewPuzzle(tempGrid,difficultyLevels[4+(2*j+i)]),3),9)
                        origGrid = copy.deepcopy(puzzleGrid)                    
        newEasyGameText = newGameButtonsFont.render("New easy game",False,black)    # adds the text to the buttons (seperate to ensure the text is in the right place)
        gameDisplay.blit(newEasyGameText,(636,42))
        newMediumGameText = newGameButtonsFont.render("New medium game",False,black)
        gameDisplay.blit(newMediumGameText,(800,42))
        newHardGameText = newGameButtonsFont.render("New hard game",False,black)
        gameDisplay.blit(newHardGameText,(636,102))
        newExpertGameText = newGameButtonsFont.render("New expert game",False,black)
        gameDisplay.blit(newExpertGameText,(808,102))

        difficultyInformText = difficultyFont.render("Difficulty:",False,black)    # displays the difficulty text, at the top
        gameDisplay.blit(difficultyInformText,(720,6))
        difficultyText = difficultyFont.render(difficulty,False,smallLineColour)
        gameDisplay.blit(difficultyText,(795,6))

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
                            if enableNotes == "On":    # for the toggle buttons, the value is flipped each time theyre pressed
                                enableNotes = "Off"
                            else:
                                enableNotes = "On"
                        if i == 0 and j == 0:
                            needToErase = True     # the other buttons can just be marked as needing to do
                        if i == 1 and j == 1:
                            if showMistakes == "On":
                                showMistakes = "Off"
                            else:
                                showMistakes = "On"
                        if i == 1 and j == 0:
                            needToShowHint = True            
        pygame.draw.rect(gameDisplay,keypadColour,(621,152,339,419),width=2)    # main keypad box
        for i in range(3):
            pygame.draw.line(gameDisplay,keypadColour,start_pos=(621,96*i+248),end_pos=(960,96*i+248),width=2)     # vertical lines
            pygame.draw.line(gameDisplay,keypadColour,start_pos=(113*i+621,152),end_pos=(113*i+621,440),width=2)    # horizontal lines
        pygame.draw.line(gameDisplay,keypadColour,start_pos=(621,506),end_pos=(960,506),width=2)    # buttons at the bottom
        pygame.draw.line(gameDisplay,keypadColour,start_pos=(791,440),end_pos=(791,571),width=2)
        for i in range(3):
            for j in range(3):
                numberToDisplay = str(keypad[i][j])
                keypadNumbers = keypadNumbersFont.render(numberToDisplay,False,black)    # adds numbers to the keypad
                gameDisplay.blit(keypadNumbers,(113*j+657,96*i+165))
        eraseButton = keypadTextFont.render("Erase",False,black)   # draws the text for the other keypad buttons
        gameDisplay.blit(eraseButton,(675,455))
        hintButton = keypadTextFont.render("Hint",False,black)
        gameDisplay.blit(hintButton,(850,455))
        enableNotesButton = keypadTextFont.render("Notes: "+enableNotes,False,black)
        gameDisplay.blit(enableNotesButton,(650,520))
        showMistakesButton = showMistakesFont.render("Show Mistakes: "+showMistakes,False,black)
        gameDisplay.blit(showMistakesButton,(798,526))

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
                        numberToShow = ""     # nothing is drawn in the square if it is being marked as empty 
                    else:
                        numberToShow = str(puzzleGrid[j][i][0])
                    if origGrid[j][i][0] == 0:
                        gridNumbers = gridNumbersFont.render(numberToShow,False,filledInNumberColour)    # the numbers the user fills in are coloured in blue
                    else:
                        gridNumbers = gridNumbersFont.render(numberToShow,False,black)    # the numbers given are coloured in black
                    gameDisplay.blit(gridNumbers,(60*i+48,60*j+34))
                    if len(puzzleGrid[j][i]) > 1 and puzzleGrid[j][i][0] == 0:   # displays the notes if there are any
                        toDisplay = [0,0,0,0,0,0,0,0,0]    # this is just to make it display nicer
                        for m in range(len(puzzleGrid[j][i])):
                            toDisplay[puzzleGrid[j][i][m]-1] = puzzleGrid[j][i][m]    # replaces a zero with the note in the correct place
                        for k in range(3):
                            for l in range(3):
                                if toDisplay[3*k+l] != 0:    # having the toDisplay array means for instance 5 will always be displayed in the middle, 9 in the bottom right etc etc
                                    numberToShow = str(toDisplay[3*k+l])
                                    noteNumbers = notesFont.render(numberToShow,False,filledInNumberColour)
                                    gameDisplay.blit(noteNumbers,(60*i+30+(20*l+5),60*j+30+(20*k-1)))
                                    
        if enableNotes == "Off":    # if notes are off, the square will be filled in
            if needToFillIn == True:
                if coords != 0 and puzzleGrid != 0 and origGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] == 0:
                    puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] = numPressed     # the 0 marking the square as not filled in is replaced by the number pressed
                needToFillIn = False
        else:
            if needToFillIn == True:
                if coords != 0 and puzzleGrid != 0 and puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] == 0:
                    if numPressed in puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)]:
                        puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].remove(numPressed)    # if the number is pressed a second time, it will be removed (so user can remove a note by clicking the number again)
                    else:
                        puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].append(numPressed)    # if notes are on, any numbers pressed will be appended on, indicating notes
                needToFillIn = False

        if needToErase == True:
            if coords != 0 and puzzleGrid != 0 and origGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] == 0:     # only erases filled in numbers
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].clear()    # cant just set it equal to 0 as the notes would not be erased
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)].append(0)
            needToErase = False

        if needToShowHint == True:
            if coords != 0 and puzzleGrid != 0 and origGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] == 0:
                puzzleGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0] = answerGrid[int((coords[1]-32)/60)][int((coords[0]-32)/60)][0]    # gets the number for the square from the answer array if hint is needed
            needToShowHint = False
        
        if puzzleGrid != 0:
            counter = 0
            for i in range(9):
                for j in range(9):
                    if puzzleGrid[i][j][0] == answerGrid[i][j][0]:
                        counter += 1
            if counter == 81:
                time.sleep(2)
                finished = True
                
        pygame.display.flip()    # updates the display
        time.sleep(0.082)    # time delay does hinder the visual performance ever so slightly but it was necessary for the buttons to function correctly

    pygame.quit()

def runFinishingScreenGUI():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,601))
    pygame.display.set_caption("Sudoku by Mattyou Quinn")

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
                finished = True

        mousePos = pygame.mouse.get_pos()
        gameDisplay.fill(white)

        congratsText = congratsFont.render("Congratulations!",False,grey)     # can you merge the two lines of text displaying??? ################################################################################################
        gameDisplay.blit(congratsText,(210,100))
        timeText = statsFont.render("Time taken:",False,black)
        gameDisplay.blit(timeText,(320,200))
        timeText = statsFont.render("0h 5m 36s",False,lightGrey)
        gameDisplay.blit(timeText,(490,200))
        hintsText = statsFont.render("Hints shown:",False,black)
        gameDisplay.blit(hintsText,(303,250))
        hintsText = statsFont.render("4",False,lightGrey)
        gameDisplay.blit(hintsText,(545,250))
        
        for i in range(2):
            pygame.draw.rect(gameDisplay,buttonColour,(230*i+280,310,190,60),border_radius=4)
            if (230*i+280) < mousePos[0] < (230*i+470) and 310 < mousePos[1] < 370:
                pygame.draw.rect(gameDisplay,buttonColourHover,(230*i+280,310,190,60),border_radius=4)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(gameDisplay,buttonColourPressed,(230*i+280,310,190,60),border_radius=4)
                    if i == 0:
                        quitGame =  False
                    else:
                        quitGame = True
                    finished = True
        replayText = buttonsFont.render("Play Again",False,black)
        gameDisplay.blit(replayText,(295,320))
        quitText = buttonsFont.render("Quit Game",False,black)
        gameDisplay.blit(quitText,(523,320))


        pygame.display.flip()
        time.sleep(0.082)
        
    pygame.quit()
    if quitGame == False:
        return True
    return False

playAgain = True
while playAgain:
    runMainProgramGUI()
    playAgain = runFinishingScreenGUI()

#runFinishingScreenGUI()#
#runMainProgramGUI()#

print("thank you for doing sudoku-y stuff")


## pressing the cross takes you to the finishing screen NOT just quitting ###########################################################################################################
## the time delay happens before the number is filled in when completed so the box remains empty until it goes to the finishing screen ##############################################

'''
timer?
number of hints on finishing screen?
finishing screen
try add undo?
show answer
restart
keyboard shortcuts? h == hint, e = erase etc
make new games buttons flash when pressed
'''
