import pygame
import scenario
from couleur import NOIR, BLANC
img2=pygame.image.load('caisse.png') # Import l'image des caisses

T_GRILLE=30

def init(l,c):
    '''Initialise une caisse de coordonnees (l,c).
    int, int -> dict(int)
    '''
    att={}
    att['pos_l'] = l
    att['pos_c'] = c
    att['vit_l'] = 0
    att['vit_c'] = 0
    
    return att

def dessine(surface,att):
    '''Dessine une caisse.
    Pygame, dict(int) -> None
    '''
    # Permet de dessiner les caisses avec un cube marron sur la grille 
    surface.blit(img2,((400+30*att['pos_l']),(300+30*att['pos_c'])))


def update(l_caisses):
    '''Met a jour les caisses.
    list(dict(int)) -> None
    '''    
    for a in range (len (l_caisses)):
        l_caisses[a]['pos_l']+=l_caisses[a]['vit_l']
        l_caisses[a]['pos_c']+=l_caisses[a]['vit_c']
        l_caisses[a]['vit_l']=0
        l_caisses[a]['vit_c']=0
