import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("My First Game") # set the title of the window
while True:
    for event in pygame.event.get(): # check for events
        if event.type == pygame.QUIT: # if the event is the user quitting
            pygame.quit() # quit the game, when we call this it's the opposite of pygame.init()
            exit() # exit the program
    pygame.display.update() # keep the screen updated
