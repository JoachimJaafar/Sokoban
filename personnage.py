import pygame
import couleur
import scenario
from couleur import NOIR, BLANC
image = pygame.image.load('down.png') # Import l'image de l'personnage
T_GRILLE = 30

def init(l,c,d,att):
    '''Initialise le personnage.
    int, int, int, dict(int) -> dict(int,list(),dict(int))
    '''
    personnage={}
    personnage['pos_l']=l
    personnage['pos_c']=c 
    personnage['direc']=1
    personnage['vit_l']=0
    personnage['vit_c']=0
    personnage['img']=[]
    personnage['att']=att

    return personnage

def dessine(surface,att):
    '''Dessine le personnage.
    Pygame, dict(int) -> None
    '''    
    surface.blit(image,[att['pos_l']*T_GRILLE+400,att['pos_c']*T_GRILLE+300])

    
def update(att):
    '''Met a jour la position du personnage selon sa vitesse de deplacement.
    dict(int) -> None
    '''
    pfla=att['pos_l']+att['vit_l']        
    pfca=att['pos_c']+att['vit_c']

    for o in range (len(att["att"]["caisses"])):
        if (att['pos_l'],att['pos_c'])==(att["att"]["caisses"][o]['pos_l'],att["att"]["caisses"][o]['pos_c']) and att['direc']==1:
            pflc=att["att"]["caisses"][o]['pos_l']
            pfcc=att["att"]["caisses"][o]['pos_c']+1
            if est_sur_mur(pflc,pfcc,att)==False and est_sur_caisse(pflc,pfcc,att)==False:
                att["att"]["caisses"][o]['vit_c']+=1
            else:
                att['pos_c']-=1


        if (att['pos_l'],att['pos_c'])==(att["att"]["caisses"][o]['pos_l'],att["att"]["caisses"][o]['pos_c']) and att['direc']==3:
            pflc=att["att"]["caisses"][o]['pos_l']
            pfcc=att["att"]["caisses"][o]['pos_c']-1
            if est_sur_mur(pflc,pfcc,att)==False and est_sur_caisse(pflc,pfcc,att)==False:
                att["att"]["caisses"][o]['vit_c']-=1
            else:
                att['pos_c']+=1



        if (att['pos_l'],att['pos_c'])==(att["att"]["caisses"][o]['pos_l'],att["att"]["caisses"][o]['pos_c']) and att['direc']==2:
            pflc=att["att"]["caisses"][o]['pos_l']+1
            pfcc=att["att"]["caisses"][o]['pos_c']
            if est_sur_mur(pflc,pfcc,att)==False and est_sur_caisse(pflc,pfcc,att)==False:
                att["att"]["caisses"][o]['vit_l']+=1
            else:
                att['pos_l']-=1



        if (att['pos_l'],att['pos_c'])==(att["att"]["caisses"][o]['pos_l'],att["att"]["caisses"][o]['pos_c']) and att['direc']==0:
            pflc=att["att"]["caisses"][o]['pos_l']-1
            pfcc=att["att"]["caisses"][o]['pos_c']
            if est_sur_mur(pflc,pfcc,att)==False and est_sur_caisse(pflc,pfcc,att)==False:
                att["att"]["caisses"][o]['vit_l']-=1
            else:
                att['pos_l']+=1


    if est_sur_mur(pfla,pfca,att)==False:
        att['pos_l']+=att['vit_l'] 
        att['pos_c']+=att['vit_c']

    att['vit_l']=0
    att['vit_c']=0



                
def est_sur_mur(lig,col,att):
    '''Retourne si l'objet de coordonnees (lig,col) est sur un mur.
    int, int, dict(int) -> bool
    '''
    for y in range (len(att["att"]["grille"])):
        if (col,lig)==att["att"]["grille"][y]:
            return True
    return False



def est_sur_caisse(lig,col,att):
    '''Retourne si l'objet de coordonnees (lig,col) est une caisse.
    int, int, dict(int) -> bool
    '''
    for z in range (len(att["att"]["caisses"])):
        a=(att["att"]["caisses"][z]["pos_l"],att["att"]["caisses"][z]["pos_c"])
        if (lig,col)==a:
            return True
    return False
                

