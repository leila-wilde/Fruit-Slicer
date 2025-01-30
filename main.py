import pygame, sys, random 
from pygame.locals import *

pygame.init()


# Constants

WIDTH = 900
HEIGHT = 600
MID_WIDTH = WIDTH * 0.5
MID_HEIGHT = HEIGHT * 0.5

RED = (217, 1, 21)   
TANGERINE = (255, 127, 0)



def draw_button(text, x, y, hover=False):
    """ function to create a button"""
    font = pygame.font.Font('fonts/DoubleFeature20.ttf', 60)
    color = RED if hover else TANGERINE
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x , y))
    DISPLAYSURF.blit(text_surface, text_rect)
    return text_rect


def menu(): 
    """ function with loop to display menu and chose options"""
    # background design
    background_image = pygame.image.load("assets/massacre_tronconneuse.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    DISPLAYSURF.blit(background_image, (0, 0)) 

    # diplay tittle
    text = "FRUIT SLICER"
    font_text = pygame.font.Font('fonts/DoubleFeature20.ttf', 100)
    text_surf = font_text.render(text, True, RED)
    text_rect = text_surf.get_rect(center=(MID_WIDTH, 100))
    DISPLAYSURF.blit(text_surf, text_rect)

    while True: 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button1_rect = draw_button("JOUER", MID_WIDTH, MID_HEIGHT - 40, button1_rect.collidepoint(mouse_x, mouse_y) if 'button1_rect' in locals()else False)
        button2_rect = draw_button("SCORES", MID_WIDTH, MID_HEIGHT + 80, button2_rect.collidepoint(mouse_x, mouse_y) if 'button2_rect' in locals()else False)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and button1_rect.collidepoint(mouse_x, mouse_y):
                # add code
                pass

            if event.type == pygame.MOUSEBUTTONDOWN and button2_rect.collidepoint(mouse_x, mouse_y):
                # add code
                pass

        pygame.display.update()





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



# DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Fruit Slicer')
# background_image_game = pygame.image.load("assets/massacre.jpg")
# background_image_game = pygame.transform.scale(background_image_game, (WIDTH, HEIGHT)) 
# DISPLAYSURF.blit(background_image_game, (0, 0))


def game_over_screen(current_score):

    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Fruit Slicer')
    background_image_game = pygame.image.load("assets/massacre_tronconneuse.jpg")
    background_image_game = pygame.transform.scale(background_image_game, (WIDTH, HEIGHT)) 
    DISPLAYSURF.blit(background_image_game, (0, 0))

    blood_image = pygame.image.load("assets/flaque1.png").convert_alpha()
    blood_image = pygame.transform.smoothscale(blood_image, (500, 500))
    DISPLAYSURF.blit(blood_image, (150, 50))

    game_over_text = "GAME OVER"
    font_game_over_text = pygame.font.Font('fonts/DoubleFeature20.ttf', 100)
    game_over_text_surf = font_game_over_text.render(game_over_text, True, RED)
    game_over_text_rect = game_over_text_surf.get_rect(center=(MID_WIDTH, MID_HEIGHT))
    DISPLAYSURF.blit(game_over_text_surf, game_over_text_rect)

    score_text = f"ton score est : {current_score} !"
    font_score_text = pygame.font.Font('fonts/DoubleFeature20.ttf', 40)
    score_text_surf = font_score_text.render(score_text, True, RED)
    score_text_rect = score_text_surf.get_rect(center = (MID_WIDTH, 450))
    DISPLAYSURF.blit(score_text_surf, score_text_rect)
    # boutton menu



# current_score = 200
def display_score(current_score):
    score = f"score : {current_score}"
    font_score = pygame.font.Font('fonts/DoubleFeature20.ttf', 35)
    score_surf = font_score.render(score, True, RED)
    score_rect = score_surf.get_rect(topleft = (10, 10))
    DISPLAYSURF.blit(score_surf, score_rect)

# lives = 3

def display_lives(lives):
    """ display heart pictures to count down lives """
    x_heart = 5
    for i in range(0, lives):
        heart_surface =pygame.image.load("assets/heart.png").convert_alpha() 
        heart_surface = pygame.transform.scale(heart_surface, (60, 60))
        DISPLAYSURF.blit(heart_surface, (x_heart, 60))
        x_heart += 60



    



# timer 

# Loop that calls all the fuctions

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()

