import pygame, sys, random 
from pygame.locals import *
from random import choice




WIDTH = 900
HEIGHT = 600




pygame.init()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Slicer!')




def random_image():
    """ fonction that built an objet rectangle from a random element (for a random image)
    and a random letter.
    letter and element are added in a dictionnary 
    return the rectangle object and the dictionnary"""
    target_element = {}
    fruits = ["abricot", "ananas", "chamallow", "citron", "courge", "fraise", "glaçon", "grenade", "kiwi", "melon",
            "noix-coco", "noix-kungfu", "orange", "pamplemousse", "passion", "pasteque", "poire", "pomme-pelee", "pomme"]
    element = choice(fruits)
    # Surface pour l'image :
    image_surface =pygame.image.load("assets/"+element+".png").convert_alpha() 
    image_surface = pygame.transform.scale(image_surface, (85, 85))
    font = pygame.font.Font(None, 40) # attention changer la font !!!
    letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letter_render = font.render(letter, True, (255, 255, 255))
    image_surface.blit(letter_render, (10, 60))
    DISPLAYSURF.blit(image_surface, (100, 100))

    rect_fruit = image_surface.get_rect()

    target_element[letter] = element

    return target_element, rect_fruit


    # def random_movement():
    #     # construction du rectangle pour le mouvement : 
    #     rect_fruit = image_surface.get_rect()
    #     coordonnées d'entrée
    #     x est choisit au hasard dans un interval (-100, 1000)
    #     y esst choisit au hasard dans un interval (-100, 700)

    #     direction (pixel_x, pixel_y)








    # def freeze_time():

    # def bomb():

    





while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    
    pygame.display.update()