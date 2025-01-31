import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 900
HEIGHT = 600
MID_WIDTH = WIDTH * 0.5
MID_HEIGHT = HEIGHT * 0.5
RED = (217, 1, 21)   
TANGERINE = (255, 127, 0)
FPS = 60
DROP_SPEED = 10 

# Set up the display
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Slicer')
background_image_game = pygame.image.load("assets/massacre.jpg")
background_image_game = pygame.transform.scale(background_image_game, (WIDTH, HEIGHT)) 
DISPLAYSURF.blit(background_image_game, (0, 0))

# Function to draw button
def draw_button(text, x, y, hover=False):
    """ function to create a button"""
    font = pygame.font.Font('fonts/DoubleFeature20.ttf', 60)
    color = RED if hover else TANGERINE
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x , y))
    DISPLAYSURF.blit(text_surface, text_rect)
    return text_rect

# Function to display the Menu screen
def menu(): 
    # background design
    background_image = pygame.image.load("assets/massacre_tronconneuse.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    DISPLAYSURF.blit(background_image, (0, 0)) 

    # Display title
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and button1_rect.collidepoint(mouse_x, mouse_y):
                game_loop()

            if event.type == pygame.MOUSEBUTTONDOWN and button2_rect.collidepoint(mouse_x, mouse_y):
                # add code
                pass

        pygame.display.update()

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

def game_over():
    # display message victory/defeat
    pass

def create_random_item():
    """Function that creates a target with a random letter and position."""
    items = ["abricot", "ananas", "chamallow", "citron", "courge", "fraise", "glacon", "grenade", "grenade", "grenade", "kiwi", "melon",
              "noix-coco", "noix-kungfu", "orange", "pamplemousse", "passion", "pasteque", "poire", "pomme-pelee", "pomme"]
    item = random.choice(items)
    letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    x = random.randint(0, WIDTH - 85)  # Random x position minus size of item
    y = 0  # Start from the top of the screen

    # Surface pour l'image :
    image_surface = pygame.image.load("assets/" + item + ".png").convert_alpha()
    image_surface = pygame.transform.scale(image_surface, (85, 85))
    font = pygame.font.Font(None, 40) # attention changer la font !!!
    letter_render = font.render(letter, True, (255, 255, 255))
    image_surface.blit(letter_render, (10, 60))

    return item, letter, y, image_surface, image_surface.get_rect(topleft=(x, y))

def game_loop():
    clock = pygame.time.Clock()
    target_list = []
    generate_new_item = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Variable that controls the frequency of new items being created. (if FPS = 60 then 30 frames = 0.5 seconds)
        generate_new_item += 2 # increments by 2 on each iteration of the loop
        if generate_new_item >= 30:  # at 30 a new item is created by calling create_random_item()
            item, letter, y, surface, rect = create_random_item() # returns the item details (including its position)
            target_list.append({'item': item, 'letter': letter, 'y': y, 'surface': surface, 'rect': rect}) # new item is added to the target_list
            generate_new_item = 0 # reset to 0

        # Update positions of falling items
        for obj in target_list:
            obj['rect'].y += DROP_SPEED  # we can change this speed in the constants 

        # Clear the screen
        background_image = pygame.image.load("assets/massacre_tronconneuse.jpg")
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        DISPLAYSURF.blit(background_image, (0, 0))

        # Draw all falling items
        for obj in target_list:
            DISPLAYSURF.blit(obj['surface'], obj['rect'].topleft)

        # Remove items that have fallen off the screen
        target_list = [obj for obj in target_list if obj['rect'].y < HEIGHT]

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

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


# Main function to run the game
def main():
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            menu()
            
        pygame.display.update()

if __name__ == "__main__":
    main()