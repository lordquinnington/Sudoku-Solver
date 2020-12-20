#~~~~~ Sudoku GUI ~~~~~#

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Sudoku Puzzle GUI")
backgroundColour = (255,255,255)
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
