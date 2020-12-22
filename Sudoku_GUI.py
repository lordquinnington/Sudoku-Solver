#~~~~~ Sudoku GUI ~~~~~#

import pygame, time
from Sudoku_Generator import generateCompletedGrid, print2DSudokuGrid
from Sudoku_Creator import createNewPuzzle
from Sudoku_Solver import formatSudokuGridTo5DFrom2D, formatSudokuGridTo2DFrom5D

pygame.init()
gameDisplay = pygame.display.set_mode((1000,601))
pygame.display.set_caption("Sudoku GUI")
white = (255,255,255)    # use for backgroundColour, mainButtonColour and squareColour
black = (20,20,20)
#mainButtonColourHover = (200,200,200)
squareColourHover = (220,250,255)
squareColourPressed = (150,220,240)
RCSColourSelected = (225,225,225)    # RCS = row/column/square
keypadColour = (170,170,170)
keypadColourHover = (225,225,225)
keypadColourPressed = (200,200,200)
otherButtonColour = (65,150,240)    # for the new games buttons etc
otherButtonColourHover = (95,170,255)
smallLineColour = (170,170,170)
clock = pygame.time.Clock()
gridNumbersFont = pygame.font.SysFont('lucidasansregular',43)
newGameButtonsFont = pygame.font.SysFont('arial',23)
difficultyFont = pygame.font.SysFont('lucidasansregular',15)
keypadNumbersFont = pygame.font.SysFont('lucidasansregular',60)
keypadTextFont = pygame.font.SysFont('arial',35)
difficulty = "Please select game"
finished = False
squareClicked = False
puzzleGrid = 0
keypad = [[1,2,3],[4,5,6],[7,8,9]]


while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # gets the mouse position
    mousePos = pygame.mouse.get_pos()

    # background
    gameDisplay.fill(white)

    # square after they have been clicked (here so the drawing of the big square goes behind the lines)
    if squareClicked == True:
        for i in range(3):
            for j in range(3):
                if (180*i+30) < coords[0] < (180*i+210) and (180*j+30) < coords[1] < (180*j+210):
                    pygame.draw.rect(gameDisplay,RCSColourSelected,(180*i+30,180*j+30,180,180))     # big square
        for i in range(9):
            pygame.draw.rect(gameDisplay,RCSColourSelected,(coords[0],60*i+32,58,58))    # column
            pygame.draw.rect(gameDisplay,RCSColourSelected,(60*i+32,coords[1],58,58))    # row
        pygame.draw.rect(gameDisplay,squareColourPressed,(coords[0],coords[1],58,58))    # square selected 

    # small grid lines
    for j in range(8):
        pygame.draw.line(gameDisplay,smallLineColour,start_pos=(60*j+90,30),end_pos=(60*j+90,571),width=2)
        pygame.draw.line(gameDisplay,smallLineColour,start_pos=(30,60*j+90),end_pos=(571,60*j+90),width=2)

    # big grid lines
    for i in range(2):
        pygame.draw.line(gameDisplay,black,start_pos=(180*(i+1)+30,30),end_pos=(180*(i+1)+30,571),width=2)
        pygame.draw.line(gameDisplay,black,start_pos=(30,180*(i+1)+30),end_pos=(571,180*(i+1)+30),width=2)

    # main box
    pygame.draw.rect(gameDisplay,black,(30,30,541,541),width=2)    # (dist. from left edge,dist. from top edge,width,height)

    # new game buttons
    pygame.draw.rect(gameDisplay,otherButtonColour,(621,32,160,50),border_radius=4)
    if 621 < mousePos[0] < 781 and 32 < mousePos[1] < 82:
        pygame.draw.rect(gameDisplay,otherButtonColourHover,(621,32,160,50),border_radius=4)
        if event.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(0.1)
            difficulty = "Easy"
            answerGrid = generateCompletedGrid()
            tempGrid  = formatSudokuGridTo5DFrom2D(answerGrid,3)
            puzzleGrid = createNewPuzzle(tempGrid,4)
            puzzleGrid = formatSudokuGridTo2DFrom5D(puzzleGrid,3)
    newEasyGameText = newGameButtonsFont.render("New easy game",False,black)
    gameDisplay.blit(newEasyGameText,(636,42))
        
    pygame.draw.rect(gameDisplay,otherButtonColour,(800,32,160,50),border_radius=4)
    if 800 < mousePos[0] < 960 and 32 < mousePos[1] < 82:
        pygame.draw.rect(gameDisplay,otherButtonColourHover,(800,32,160,50),border_radius=4)
        if event.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(0.1)    # time delay stops the button from accidentally being pressed twice
            difficulty = "Medium"
            answerGrid = generateCompletedGrid()
            tempGrid  = formatSudokuGridTo5DFrom2D(answerGrid,3)
            puzzleGrid = createNewPuzzle(tempGrid,3)
            puzzleGrid = formatSudokuGridTo2DFrom5D(puzzleGrid,3)
    newMediumGameText = newGameButtonsFont.render("New medium game",False,black)
    gameDisplay.blit(newMediumGameText,(800,42))
    
    pygame.draw.rect(gameDisplay,otherButtonColour,(621,92,160,50),border_radius=4)
    if 621 < mousePos[0] < 781 and 92 < mousePos[1] < 142:
        pygame.draw.rect(gameDisplay,otherButtonColourHover,(621,92,160,50),border_radius=4)
        if event.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(0.1)
            difficulty = "Hard"
            answerGrid = generateCompletedGrid()
            tempGrid  = formatSudokuGridTo5DFrom2D(answerGrid,3)
            puzzleGrid = createNewPuzzle(tempGrid,2)
            puzzleGrid = formatSudokuGridTo2DFrom5D(puzzleGrid,3)
    newHardGameText = newGameButtonsFont.render("New hard game",False,black)
    gameDisplay.blit(newHardGameText,(636,102))
    
    pygame.draw.rect(gameDisplay,otherButtonColour,(800,92,160,50),border_radius=4)
    if 800 < mousePos[0] < 960 and 92 < mousePos[1] < 142:
        pygame.draw.rect(gameDisplay,otherButtonColourHover,(800,92,160,50),border_radius=4)
        if event.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(0.1)
            difficulty = "Expert"
            answerGrid = generateCompletedGrid()
            tempGrid  = formatSudokuGridTo5DFrom2D(answerGrid,3)
            puzzleGrid = createNewPuzzle(tempGrid,1)
            puzzleGrid = formatSudokuGridTo2DFrom5D(puzzleGrid,3)     # could you remove this line from all of them and just have one at the bottom, as it does the same job? #####################################
    newExpertGameText = newGameButtonsFont.render("New expert game",False,black)
    gameDisplay.blit(newExpertGameText,(808,102))

    # difficulty text
    difficultyInformText = difficultyFont.render("Difficulty:",False,black)
    gameDisplay.blit(difficultyInformText,(720,6))
    difficultyText = difficultyFont.render(difficulty,False,smallLineColour)
    gameDisplay.blit(difficultyText,(795,6))

    # keypad buttons
    for i in range(3):
        for j in range(3):
            if(113*i+621) < mousePos[0] < (113*i+734) and (96*j+152) < mousePos[1] < (96*j+248):    # for hovering (here so doesn't interfere with the other lines)
                pygame.draw.rect(gameDisplay,keypadColourHover,(113*i+621,96*j+152,113,96))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(gameDisplay,keypadColourPressed,(113*i+621,96*j+152,113,96))

    for i in range(2):
        for j in range(2):
            
            
    pygame.draw.rect(gameDisplay,keypadColour,(621,152,339,419),width=2)
    for i in range(3):
        pygame.draw.line(gameDisplay,keypadColour,start_pos=(621,96*i+248),end_pos=(960,96*i+248),width=2)     # vertical lines
        pygame.draw.line(gameDisplay,keypadColour,start_pos=(113*i+621,152),end_pos=(113*i+621,440),width=2)    # horizontal lines
    pygame.draw.line(gameDisplay,keypadColour,start_pos=(621,506),end_pos=(960,506),width=2)
    pygame.draw.line(gameDisplay,keypadColour,start_pos=(791,440),end_pos=(791,571),width=2)

    # keypad numbers
    for i in range(3):
        for j in range(3):
            numberToDisplay = str(keypad[i][j])
            keypadNumbers = keypadNumbersFont.render(numberToDisplay,False,black)
            gameDisplay.blit(keypadNumbers,(113*j+657,96*i+165))

    # grid square hovering
    for i in range(9):
        for j in range(9):
            if (60*i+32) < mousePos[0] < (60*i+90) and (60*j+32) < mousePos[1] < (60*j+90):
                pygame.draw.rect(gameDisplay,squareColourHover,(60*i+32,60*j+32,58,58))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    squareClicked = True
                    coords = [(60*i+32),(60*j+32)]
        
    # numbers in the grid
    if puzzleGrid != 0:
        for i in range(9):
            for j in range(9):
                if puzzleGrid[j][i] == 0:
                    numberToShow = ""
                else:
                    numberToShow = str(puzzleGrid[j][i])
                gridNumbers = gridNumbersFont.render(numberToShow,False,black)     # is it possible to combine these 2 lines? put top in brackets in bottom  ##############################################
                gameDisplay.blit(gridNumbers,(60*i+48,60*j+34))
                
            
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
