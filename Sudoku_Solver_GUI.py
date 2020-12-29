#~~~~~ Sudoku Solver GUI ~~~~~#

import pygame, time

def runMainProgramGUI():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,601))
    pygame.display.set_caption("Sudoku Solver by Mattyou Quinn")

    white = (255,255,255)
    black = (20,20,20)
    smallLineColour = (170,170,170)
    lightGrey = (225,225,225)
    squareColourHover = (220,250,255)
    squareColourPressed = (150,220,240)
    keypadColour = (170,170,170)
    keypadColourPressed = (200,200,200)
    otherButtonColour = (65,150,240)
    otherButtonColourHover = (95,170,255)
    otherButtonColourPressed = (60,140,225)

    gridNumbersFont = pygame.font.SysFont('lucidasansregular',43)
    keypadNumbersFont = pygame.font.SysFont('lucidasansregular',60)
    keypadTextFont = pygame.font.SysFont('arial',30)

    finished = False
    squareClicked = False
    needToErase = False
    restartGame = False
    solveGrid = False
    moveSquareUp = False
    moveSquareDown = False
    moveSquareLeft = False
    moveSquareRight = False
    coords = 0
    keypad = [[1,2,3],[4,5,6],[7,8,9]]

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moveSquareUp = True
                if event.key == pygame.K_DOWN:
                    moveSquareDown = True
                if event.key == pygame.K_LEFT:
                    moveSquareLeft = True
                if event.key == pygame.K_RIGHT:
                    moveSquareRight = True

        mousePos = pygame.mouse.get_pos()
        gameDisplay.fill(white)

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

        pygame.draw.rect(gameDisplay,black,(30,30,541,541),width=2)

        for i in range(3):    # the key pad (hovering)
            for j in range(3):
                if (113*i+621) < mousePos[0] < (113*i+734) and (96*j+30) < mousePos[1] < (96*j+126):    # for hovering (here so doesn't interfere with the other lines)
                    pygame.draw.rect(gameDisplay,lightGrey,(113*i+621,96*j+30,113,96))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(gameDisplay,keypadColourPressed,(113*i+621,96*j+30,113,96))
                        needToFillIn = True
                        numPressed = keypad[j][i]    # if the keypad button is pressed, the number (from an array in the same format) is recorded
                        
        for i in range(2):
            if (170*i+621) < mousePos[0] < (170*i+791) and (318) < mousePos[1] < (384):
                pygame.draw.rect(gameDisplay,lightGrey,(170*i+621,318,170,66))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(gameDisplay,keypadColourPressed,(170*i+621,318,170,66))
                    if i == 0:
                        needToErase = True
                    if i == 1:
                        restartGame = True

        pygame.draw.rect(gameDisplay,keypadColour,(621,30,339,353),width=2)    # main keypad box
        pygame.draw.line(gameDisplay,keypadColour,start_pos=(791,318),end_pos=(791,382),width=2)
        gameDisplay.blit(keypadTextFont.render("Erase",False,black),(673,332))
        gameDisplay.blit(keypadTextFont.render("Restart",False,black),(833,332))
        
        for i in range(3):
            pygame.draw.line(gameDisplay,keypadColour,start_pos=(621,96*i+126),end_pos=(960,96*i+126),width=2)     # vertical lines
            pygame.draw.line(gameDisplay,keypadColour,start_pos=(113*i+621,30),end_pos=(113*i+621,318),width=2)    # horizontal lines
        
        for i in range(3):
            for j in range(3):
                gameDisplay.blit(keypadNumbersFont.render(str(keypad[i][j]),False,black),(113*j+657,96*i+43))    # adds numbers to the keypad

        pygame.draw.rect(gameDisplay,otherButtonColour,(671,409,240,66),border_radius=8)      # the big blue solve button
        if 671 < mousePos[0] < 911 and 409 < mousePos[1] < 474:
            pygame.draw.rect(gameDisplay,otherButtonColourHover,(671,409,240,66),border_radius=8)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(gameDisplay,otherButtonColourPressed,(671,409,240,66),border_radius=8)
                solveGrid = True

        for i in range(9):
            for j in range(9):
                if (60*i+32) < mousePos[0] < (60*i+90) and (60*j+32) < mousePos[1] < (60*j+90):
                    pygame.draw.rect(gameDisplay,squareColourHover,(60*i+32,60*j+32,58,58))    # hovering over the grid square
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        squareClicked = True
                        coords = [(60*i+32),(60*j+32)]    # if the grid square is clicked on, its coordinates are marked

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

        pygame.display.flip()
        time.sleep(0.082)

    pygame.quit()

runMainProgramGUI()
