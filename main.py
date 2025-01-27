import pygame, sys, random 
from pygame.locals import *


# Constants

WIDTH = 1800
HEIGHT = 1200

def menu():  
    pass


# def menu():  
    # return les différent objet présent sur le menu

# def show_random_object():
    # créé un ojet fruit avec une image, une lettre, une taille (variable : image, letter, size(width, height))
    # cet objet à une coordonée de départ RANDOM, une direction RANDOM et une vitesse (variable : x, y, speed)
#     # select object - fruit, ice cube or bomb
#     # select random x,y vector? speed

# def ice_cube():
    # si la saisie clavier relative au glacon == gèle les mouvements pendant X temps 
    # 

# def game_score():
    # si un fruit est validé 
    # le score augmente 
    # le fruit se transforme en flaque de sang 
    
# def manage_score():
    # ajoute le score de la pratie fini à l'ancien score 
    # varaible : game_score, hystory_score
    # return le nouveau score

#def input_new_player()
    # lie un nom à un score dans un historique 
    # ajoute un fichier txt ou json
    
# def player_lives():
    # retire une vie à chaque fruit manqué
    # le joueur débute avec 3 vies
    # lives = 3
    # si fruit manqué -> déduit une vie
    # return le nombre de vie courant
    
# def game_over():
    # deux condition de défaite : la bombe (saisie de clavier)
#     # display message victory/defeat
def show_random_object():
    # select object - fruit, ice cube or bomb
    # select random x,y vector? speed
    pass
    
def manage_score():
    pass
def player_lives():
    pass
    
def game_over():
    # display message victory/defeat
    pass

pygame.init()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Slicer')

# timer 

# Loop that calls all the fuctions

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()

