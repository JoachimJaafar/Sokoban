import pygame

from couleur import NOIR, BLANC

import scenario


def dessine(surface):
    '''Dessine l'ouverture du jeu.
    Pygame -> None
    '''
    # Image de fond pour illustrer l'ouverture
    image_fond = pygame.image.load_basic('Sokoban.bmp')# Permet de rechercher l'image dans le dossier
    surface.blit(image_fond, [0, 0])

def execute(surface):
    '''Exécute la présentation du jeu et permet de la quitter.
    Pygame -> bool
    '''
    dessine(surface)
    pygame.display.update()
    terminer = False
    while not terminer :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                return False
                terminer == True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    return False
                    terminer == True
                if event.key == pygame.K_RETURN :
                    return True
                    terminer == True
