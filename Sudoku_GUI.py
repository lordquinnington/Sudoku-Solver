#~~~~~ Sudoku GUI ~~~~~#

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Sudoku Puzzle GUI")
backgroundColour = (255,255,255)
mainButtonColour = (255,255,255)
mainButtonColourHover = (200,200,200)
squareColour = (255,255,255)
squareColourHover = (175,195,200)
squareColourPressed = (145,185,200)
RCSColourSelected = (180,180,180)    # RCS = row/column/square
otherButtonColour = (65,140,220)    # for the new games buttons etc
otherButtonColourHover = (75,135,200)
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    gameDisplay.fill(backgroundColour)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
