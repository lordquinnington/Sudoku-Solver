#~~~~~ Sudoku GUI ~~~~~#

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1000,601))
pygame.display.set_caption("Sudoku Puzzle GUI")
white = (255,255,255)    # use for backgroundColour, mainButtonColour and squareColour
black = (28,28,28)
mainButtonColourHover = (200,200,200)
squareColourHover = (175,195,200)
squareColourPressed = (145,185,200)
RCSColourSelected = (180,180,180)    # RCS = row/column/square
otherButtonColour = (65,140,220)    # for the new games buttons etc
otherButtonColourHover = (75,135,200)
smallLineColour = (170,170,170)
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    gameDisplay.fill(white)
    for j in range(8):
        #if j == 2 or j == 5:
        #    pygame.draw.line(gameDisplay,black,start_pos=(60*j+90,30),end_pos=(60*j+90,571),width=2)
        #    pygame.draw.line(gameDisplay,black,start_pos=(30,60*j+90),end_pos=(571,60*j+90),width=2)
        if j != 2 or j != 5:
            pygame.draw.line(gameDisplay,smallLineColour,start_pos=(60*j+90,30),end_pos=(60*j+90,571),width=2)
            pygame.draw.line(gameDisplay,smallLineColour,start_pos=(30,60*j+90),end_pos=(571,60*j+90),width=2)
    pygame.draw.rect(gameDisplay,black,(30,30,541,541),width=2)    # (dist. from left edge,dist. from top edge,width,height)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
