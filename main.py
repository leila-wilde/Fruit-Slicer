import pygame, sys, random 
from pygame.locals import *
import time
import json

# Constants

WIDTH = 1800
HEIGHT = 1200
MID_WIDTH = WIDTH // 2
MID_HEIGTH = HEIGHT // 2


def write_score(score):
    with open("./score.json", "w") as file:
        json.dump(score, file)

def read_score():
    with open("./score.json", "r") as file :
        score = json.load(file)
        return score


score_players = read_score()
print("Entrez votre nom :")
player_name = input()

# si le joueur n'existe pas dans "score.json":
#    on le créé avec un score égal à zéro
if player_name not in score_players :
    score_players[player_name] = 0

nb_lives = 3

pygame.init()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Slicer!')

run = True
reset_timer = False
time_zero = time.time()
minimum = 0
total_score = 0
ice_cube = False

# in final game version
# target_list will be empty
# we will use a function that creates a new fruit every second
# the newly created fruit is added to our list alive_items
alive_items = [("A", "fraise"), ("B", "pomme"), ("C", "glacon"), ("A", "glacon"), ("A", "banane"), ("G", "grenade")]


while run : # main game loop
    time_now = time.time()
    difference = time_now - time_zero
    current_score = 0
    fail = False

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            letter_input = pygame.key.name(event.key).upper()

            for i in range(0, len(alive_items)):
                if letter_input == alive_items[i][0]:
                    if alive_items[i][1] == "grenade":
                        game_over(current_score)

                        # fail is for scoring
                        fail = True
                        run = False
                    elif alive_items[i][1] == "glacon":
                        print("gele temps == freezes time")
                        ice_cube = True
                        ice_cube_time = time.time()
                        # freezes new items generation
                        # for 3 seconds
                        generate_new_fruit(ice_cube, ice_cube_time)
                        current_score += 1
                    else :
                        current_score += 1                

            # when user presses a key that is equal to the letter of the item
            # or the letter of more than 1 item
            # corresponding items disappear
            alive_items = [e for e in alive_items if e[0] != letter_input]

        if event.type == QUIT:
            run = False

    if fail:
        current_score = 0

    if current_score > 2:
        current_score -= 1

    total_score += current_score

    # if the fruit moves out of the screen :
        # nb_lives -= 1
        # fruit is removed from alive_items list

    if nb_lives == 0 :
        run = False

    pygame.display.update()

    # every seconds :
    # we call a function that generates a new fruit
    if time.time() - time_zero > 1 :
        if ice_cube is False :
            generate_new_fruit(ice_cube, None)
        reset_timer = True
        if reset_timer :
            time_zero = time.time()
            reset_timer = False

pygame.quit()
write_score(score_players)
print(total_score)
print(time_zero)
print(alive_items)