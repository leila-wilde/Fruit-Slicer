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
    target_list = []
    fruits = ["abricot", "ananas", "chamallow", "citron", "courge", "fraise", "glaçon", "grenade", "kiwi", "melon",
            "noix-coco", "noix-kungfu", "orange", "pamplemousse", "passion", "pasteque", "poire", "pomme-pelee", "pomme"]
    element = choice(fruits)
    # Surface pour l'image :
    image_surface =pygame.image.load("assets/"+element+".png").convert_alpha() 
    image_surface = pygame.transform.scale(image_surface, (85, 85))
    font = pygame.font.Font(None, 40) 
    letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    letter_render = font.render(letter, True, (255, 255, 255))
    image_surface.blit(letter_render, (10, 60))

    rect_target = image_surface.get_rect()

    target_list.append((letter, element))

    return target_list, rect_target










    





while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    
    pygame.display.update()