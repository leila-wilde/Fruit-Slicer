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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLOOD_FONT = 'fonts/DoubleFeature20.ttf'
BLOCK_FONT = 'fonts/Block_Helvetica.ttf'
SLASH_FONT = 'fonts/Parasite.ttf'
FPS = 60
DROP_SPEED = 2

# Set up the display
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Slicer')

# Add images
background_image_game = pygame.image.load('assets/massacre.jpg')
background_image_game = pygame.transform.scale(background_image_game, (WIDTH, HEIGHT))
background_image_menu = pygame.image.load('assets/massacre_tronconneuse.jpg')
background_image_menu = pygame.transform.scale(background_image_menu, (WIDTH, HEIGHT))

# Function to create a button
def draw_button(text, x, y, hover=False):
    font = pygame.font.Font(BLOOD_FONT, 60)
    color = RED if hover else TANGERINE
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x , y))
    DISPLAYSURF.blit(text_surface, text_rect)
    return text_rect

def game_over_screen(total_score):
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Fruit Slicer')
    DISPLAYSURF.blit(background_image_menu, (0, 0))

    blood_image = pygame.image.load('assets/flaque1.png').convert_alpha()
    blood_image = pygame.transform.smoothscale(blood_image, (WIDTH * 1.25, HEIGHT * 1.25))
    DISPLAYSURF.blit(blood_image, (WIDTH * 0.1, 0))

    game_over_text = 'GAME OVER'
    font_game_over_text = pygame.font.Font(BLOOD_FONT, 100)
    game_over_text_surf = font_game_over_text.render(game_over_text, True, RED)
    game_over_text_rect = game_over_text_surf.get_rect(center=(MID_WIDTH, MID_HEIGHT - 100))
    DISPLAYSURF.blit(game_over_text_surf, game_over_text_rect)

    score_text = f'ton score est : {total_score} !'
    font_score_text = pygame.font.Font(BLOOD_FONT, 60)
    score_text_surf = font_score_text.render(score_text, True, RED)
    score_text_rect = score_text_surf.get_rect(center = (MID_WIDTH, MID_HEIGHT + 40))
    DISPLAYSURF.blit(score_text_surf, score_text_rect)

    while True: 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_rect = draw_button('MENU', MID_WIDTH, 550, button_rect.collidepoint(mouse_x, mouse_y) if 'button_rect' in locals()else False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(mouse_x, mouse_y):
                menu()

        pygame.display.update()

def display_score(total_score):
    score = f'score : {total_score}'
    font_score = pygame.font.Font(BLOOD_FONT, 35)
    score_surf = font_score.render(score, True, RED)
    score_rect = score_surf.get_rect(topleft = (10, 10))
    DISPLAYSURF.blit(score_surf, score_rect)

# Function to display heart pictures to count down lives
def display_lives(lives):
    x_heart = 5
    for i in range(0, lives):
        heart_surface =pygame.image.load('assets/heart.png').convert_alpha() 
        heart_surface = pygame.transform.scale(heart_surface, (60, 60))
        DISPLAYSURF.blit(heart_surface, (x_heart, 60))
        x_heart += 60

# Function to display the Menu screen
def menu(): 
    DISPLAYSURF.blit(background_image_menu, (0, 0)) 
    text = 'FRUIT SLICER'
    font_text = pygame.font.Font(BLOOD_FONT, 100)
    text_surf = font_text.render(text, True, RED)
    text_rect = text_surf.get_rect(center=(MID_WIDTH, 100))
    DISPLAYSURF.blit(text_surf, text_rect)

    while True: 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button1_rect = draw_button('JOUER', MID_WIDTH, MID_HEIGHT - 40, button1_rect.collidepoint(mouse_x, mouse_y) if 'button1_rect' in locals()else False)
        button2_rect = draw_button('SCORES', MID_WIDTH, MID_HEIGHT + 80, button2_rect.collidepoint(mouse_x, mouse_y) if 'button2_rect' in locals()else False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and button1_rect.collidepoint(mouse_x, mouse_y):
                total_score = game_loop()
                game_over_screen(total_score)

            if event.type == pygame.MOUSEBUTTONDOWN and button2_rect.collidepoint(mouse_x, mouse_y):
                # add code
                pass

        pygame.display.update()

# Function to select and position a random item with a random letter
def create_random_item():
    items = ['abricot', 'ananas', 'chamallow', 'citron', 'courge', 'fraise', 'glacon', 'glacon', 'glacon', 'grenade', 'grenade', 'grenade', 'kiwi', 'melon',
              'noix-coco', 'noix-kungfu', 'orange', 'pamplemousse', 'passion', 'pasteque', 'poire', 'pomme-pelee', 'pomme']
    item = random.choice(items)
    letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    x = random.randint(0, WIDTH - 85)  # Random x position minus size of item
    y = 0  # Start from the top of the screen
    
    # Surface for the image:
    image_surface = pygame.image.load('assets/' + item + '.png').convert_alpha()
    image_surface = pygame.transform.scale(image_surface, (85, 85))
    font = pygame.font.Font(BLOCK_FONT, 40) # attention changer la font !!!
    letter_render = font.render(letter, True, (BLACK))
    image_surface.blit(letter_render, (0, 10))

    return item, letter, y, image_surface, image_surface.get_rect(topleft=(x, y))

def game_loop():
    clock = pygame.time.Clock()
    target_list = []
    generate_new_item = 0
    lives = 3
    total_score =0
    current_score = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                letter_input = pygame.key.name(event.key).upper()

                for i in range(0, len(target_list)):
                    if letter_input == target_list[i]['letter']:
                        print(f'letter input : {letter_input}')
                        print(f'fruit : {target_list[i]}')
                        if target_list[i]['item'] == 'grenade':
                            run = False
                        elif target_list[i]['item'] == 'glacon':
                            print('gele temps == freezes time')
                            # freezes new items generation
                            # for 3 seconds
                            current_score += 1
                        else :
                            current_score += 1
            
                # combo score
                if current_score > 2:
                    current_score -= 1  

                total_score += current_score
                current_score = 0
            
                # when user presses a key that is equal to the letter of the item
                # or the letter of more than 1 item
                # corresponding items disappear
                target_list = [obj for obj in target_list if obj['letter'] != letter_input]

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
        background_image = pygame.image.load('assets/massacre.jpg')
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
        DISPLAYSURF.blit(background_image, (0, 0))

        # Update positions of falling items
        for obj in target_list:
            DISPLAYSURF.blit(obj['surface'], obj['rect'].topleft)

        # Remove one life for each fruit fellen off the screen
        for obj in target_list :
            if obj['rect'].y >= HEIGHT:
                if obj['item'] != 'grenade' and obj['item'] != 'glacon':
                    lives -= 1
        
        # game over if no more life
            if lives <= 0 :
                run = False  

        # Remove items that have fallen off the screen
        target_list = [obj for obj in target_list if obj['rect'].y < HEIGHT]

        display_score(total_score)
        display_lives(lives)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    return total_score

# Main function to run the game
def main():
    while True:
        menu()

if __name__ == '__main__':
    main()