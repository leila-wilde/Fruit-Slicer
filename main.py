import pygame, sys, random 
from pygame.locals import *
import time
import json

# Constants

WIDTH = 1800
HEIGHT = 1200
MID_WIDTH = WIDTH // 2
MID_HEIGTH = HEIGHT // 2

class Fruit(pygame.sprite.Sprite):
    """déplace un fruit a travers l'écran. Le fruit se transforme en 
    flaque de sang quand il est validé par une saisie clavier."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # appel du constructeur sprite
        self.image = pygame.image.load('abricot.png')


def write_score(score):
    with open("./score.json", "w") as file:
        json.dump(score, file)

def read_score():
    with open("./score.json", "r") as file :
        score = json.load(file)
        return score

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

score_players = read_score()
print("Entrez votre nom :")
player_name = input()

# si le joueur n'existe pas dans "score.json":
#    on le créé avec un score égal à zéro


nb_lives = 3

pygame.init()

PINK = (255, 153, 204)
DARK_BLUE = (0, 0, 153)

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Slicer!')
upper = pygame.Rect(0, 0, WIDTH, MID_HEIGTH)       # left, top, width, height
lower = pygame.Rect(0, MID_HEIGTH, WIDTH, MID_HEIGTH)       # left, top, width, height

letter = "A"

upper_font = pygame.font.SysFont(None, 72)
lower_font  = pygame.font.SysFont(None, 72)

upper_img = upper_font.render(letter, True, (0, 0, 0))
lower_img = lower_font.render("", True, (255, 255, 255))

run = True
time_zero = time.time()

while run : # main game loop
    termine = False
    while not termine :

        pygame.draw.rect(DISPLAYSURF, PINK, upper)
        pygame.draw.rect(DISPLAYSURF, DARK_BLUE, lower)

        time_now = time.time()
        difference = time_now - time_zero
        if difference >= 3 :
            # Condition of losing one life :
            # Player loses if he/she doesn't type the rirght letter
            # within 3 seconds

            lower_img = lower_font.render("Perdu", True, (255, 255, 255))
            time.sleep(3)
            nb_lives -= 1
            run = False
            termine = True

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                lettre_input = pygame.key.name(event.key).upper()

                if lettre_input == letter :
                    lower_img = lower_font.render("Bravo", True, (255, 255, 255))
                    termine = True
                    run = False
                    if player_name in score_players :
                        score_players[player_name] += 1
                    else :
                        score_players [player_name] = 1
                    print(f"score = {score_players}")

            if event.type == QUIT:
                run = False
                termine = True

        DISPLAYSURF.blit(upper_img, (MID_WIDTH, 300))
        DISPLAYSURF.blit(lower_img, (MID_WIDTH, 150 + MID_HEIGTH))

        pygame.display.update()

pygame.quit()
write_score(score_players)
#sys.exit()
print(time_zero)
