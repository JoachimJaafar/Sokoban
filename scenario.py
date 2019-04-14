# -*- coding: cp1252 -*-

import pygame
from couleur import NOIR, BLANC
import ouverture
import caisse
import personnage
img1=pygame.image.load('mur.png')# Import l'image des murs
img3=pygame.image.load('destination.png')# Import l'image de la cible

#— # : mur
#— $ : caisse
#— . : destination 
#@ : personnage 

NIVEAU0= ["nnnnnnnnnnnnn",
          "nnnnnnnnnnnnn",
          "nnnnnn#######",
          "nnnnnn#@$  .#",
          "nnnnnn#######"]

NIVEAU1= ["nnnn########",
          "nnnn#.  .. #",
          "nnnn# #.   #",
          "nnnn#$ $$$ #",
          "nnnn#.$ $  #",
          "nnnn#. @   #",
          "nnnn########"]

NIVEAU2= ["nnnn######",
           "nnnn#... #",
           "nnnn# $. #",
           "nnnn# $$$#",
           "nnnn# $ .#",
           "nnnn#  @ #",
           "nnnn######"]

NIVEAU3= ["nnnn#####nnnnnnnnnn",
          "nnnn#   #nnnnnnnnnn",
          "nnnn#$  #nnnnnnnnnn",
          "nn###  $##nnnnnnnnn",
          "nn#  $ $ #nnnnnnnnn",
          "### # ## #SSS######",
          "#   # ## #####  ..#",
          "# $ $           ..#",
          "##### ### #@##  ..#",
          "nnnn#     #########",
          "nnnn#######nnnnnnnn"]

NIVEAU4= ["nnnn##########",
          "nnnn#.  #   .#",
          "nnnn#.  $ $  #",
          "nnnn#  .#.$  #",
          "nnnn## .#$$ @#",
          "nnnn#   $ $ $#",
          "nnnn###.#.#  #",
          "nnnn##########"]

NIVEAU5= ["nn######nn",
          "nn#    ##nn",
          "n##.##$ #nn",
          "n# ..$  #nn",
          "n#  #$  #nn",
          "n# @  ###nn",
          "n######nnnn"]

NIVEAU6= ["############nn",
          "#..  #     ###",
          "#..  # $  $  #",
          "#..  #$####  #",
          "#..    @ ##  #",
          "#..  # #  $ ##",
          "###### ##$ $ #",
          "nn# $  $ $ $ #",
          ",,#    #     #",
          "nn############"]

# Ajoute les niveaux dans une liste
GRILLE=[NIVEAU0,NIVEAU1,NIVEAU2,NIVEAU3,NIVEAU4,NIVEAU5,NIVEAU6]
T_GRILLE = 30


def init(num) :
    '''Initialise un niveau selon son indice num.
    int -> dict(int)
    '''
    lvl = GRILLE[num]
    att = {}
    att['personnage'] = []
    att['grille'] = []
    att['grille2'] = []
    att['caisses'] = []
    att['sol']=[]
    liste_caisses = []
    for i in range(len(lvl)) :
        for j in range(len(lvl[i])) :
            if lvl[i][j] == '#' :
                att['grille'] += [(i,j)]
            if lvl[i][j] == '.' :
                att['grille2'] += [(i,j)]
            if lvl[i][j]==" " or lvl[i][j]=="@" or lvl[i][j]=="$":
                att["sol"]+=[(i,j)]
            if lvl[i][j] == '$' :
                initialisation = caisse.init(j,i)
                liste_caisses += [initialisation]
                att['caisses'] = liste_caisses
            if lvl[i][j] == '@' :
                att['personnage'] += [(i,j)]
    att["joueur"]=personnage.init(att["personnage"][0][1],att["personnage"][0][0],2,att)
    return att

    

def dessine_mur(surface,l, c) :
    '''Dessine les murs du niveau.
    Pygame, int, int -> None
    '''
    # Dessine les murs du niveau avec des cubes blanc
    surface.blit(img1,[l*T_GRILLE+400,c*T_GRILLE+300])

def dessine_cible(surface, l, c) :
    '''Dessine les destinations du niveau.
    Pygame, int, int -> None
    '''
    # Dessine la cible du niveau avec des cubes rouge
    surface.blit(img3,[l*T_GRILLE+400,c*T_GRILLE+300])

def dessine_sol(surface,l,c):
    '''Dessine le sol du niveau.
    Pygame, int, int -> bool
    '''
    pygame.draw.rect(surface,NOIR,[l*T_GRILLE+400,c*T_GRILLE+300,T_GRILLE,T_GRILLE])

    
def dessine(att, surface) :
    '''Dessine tous les objets du scenario.
    dict(int), Pygame -> None
    '''
    surface.fill((NOIR)) # Choisis la couleur du fond du jeu
    for h in range (0,len(att['sol'])):
         dessine_sol(surface,(att["sol"][h][1]),(att["sol"][h][0]))
    for i in range(0,len(att['grille'])) :
         dessine_mur(surface,(att["grille"][i][1]),(att["grille"][i][0]))
    for j in range(0,len(att['grille2'])) :
         dessine_cible(surface,(att["grille2"][j][1]),(att["grille2"][j][0]))
    for l in range(0,len(att["caisses"])) :
         caisse.dessine(surface,(att["caisses"][l]))
    personnage.dessine(surface,att["joueur"])
    r_entry=pygame.font.Font(None,20)
    str_r_entry=r_entry.render("Appuyez sur R pour recommencer le niveau, et entrée pour le passer",True, BLANC)
    surface.blit(str_r_entry,[450,200])
    pygame.display.update()

def caisses_sur_cibles(att):
    '''Retourne True si toutes les caisses sont sur les destinations (et donc si le niveeau est gagné).
    dict(int) -> bool
    '''
    win=0
    for c in range (len(att["grille2"])):
        for b in range (len(att["caisses"])):
            if (att["caisses"][b]['pos_c'],att["caisses"][b]['pos_l'])== att["grille2"][c]:
                win+=1            
    if win==len(att["grille2"]):
        return True
    
def execute(att,niveau) :
    '''Execute le jeu.
    dict(int), int -> int
    '''
    clock=pygame.time.Clock()
    mouv=0
    terminer=False
    while not terminer:
        for event in pygame.event.get():
            if event.type== pygame.QUIT :
                return 0 
                terminer=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return 0 
                    terminer=True
                if event.key==pygame.K_r:
                    return 1 
                if event.key==pygame.K_RETURN:
                    
                    if niveau+1==len(GRILLE):
                        return 3
                    else:
                        return 2
                if event.key==pygame.K_LEFT:
                    att["joueur"]["vit_l"]=-1
                    att["joueur"]["vit_c"]=0
                    att["joueur"]["direc"]=0
                    personnage.image = pygame.image.load('left.png')
                    mouv+=1
                    
                    
                if event.key==pygame.K_RIGHT:
                    att["joueur"]["vit_l"]=1
                    att["joueur"]["vit_c"]=0
                    att["joueur"]["direc"]=2
                    personnage.image = pygame.image.load('right.png')
                    mouv+=1
                    
                if event.key==pygame.K_UP:
                    att["joueur"]["vit_l"]=0
                    att["joueur"]["vit_c"]=-1
                    att["joueur"]["direc"]=3
                    personnage.image = pygame.image.load('up.png')
                    mouv+=1
                    
                if event.key==pygame.K_DOWN:
                    att["joueur"]["vit_l"]=0
                    att["joueur"]["vit_c"]=1
                    att["joueur"]["direc"]=1
                    personnage.image = pygame.image.load('down.png')
                    mouv+=1 
                                                      
        surface= pygame.display.set_mode((1280,720))           
        surface.fill((NOIR))
        clock.tick(150)
        
        if caisses_sur_cibles(att)==True:
            if niveau+1==len(GRILLE):
                return 3
            
            else:
                clock.tick(2)
                surface.fill((NOIR))
                titre_police=pygame.font.Font(None,70)
                titre1=titre_police.render("Vous avez réussi ce niveau en "+str(mouv)+" déplacements",True, BLANC)
                surface.blit(titre1,[80,300])
                pygame.display.update()
                clock.tick(0.4)
                return 2
        
        else:
            
            personnage.update(att["joueur"]) 
            caisse.update(att["caisses"])
            dessine(att,surface)

        pygame.display.update()

        #r_entry=pygame.font.Font(None,20)
        #str_r_entry=r_entry.render("Appuyez sur R pour recommencer le niveau, et entrée pour le passer",True, BLANC)
        #surface.blit(str_r_entry,[495,602])
