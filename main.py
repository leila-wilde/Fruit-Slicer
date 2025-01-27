import pygame, sys, random 
from pygame.locals import *


# Constants

WIDTH = 1800
HEIGHT = 1200


# def menu():  

# def show_random_object():
#     # select object - fruit, ice cube or bomb
#     # select random x,y vector? speed
    
# def manage_score():
    
# def player_lives():
    
# def game_over():
#     # display message victory/defeat

pygame.init()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Slicer!')

# Loop that calls all the fuctions

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()

