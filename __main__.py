import pygame
from couleur import NOIR, BLANC
import presentation
import scenario
from pygame.locals import *



def main():
    '''Fonction principale du jeu.
    None -> None
    '''
    essais=0
    pygame.init() # Initialise Pygame
    clock= pygame.time.Clock()
    surface= pygame.display.set_mode((1200,670)) # Definit la taille de la fenetre
    pygame.display.set_caption("Sokoban") # Ajouter un nom a la fenetre

    surface.fill(BLANC)   
    continuer=presentation.execute(surface)
    terminer=False
    if not continuer:
        pygame.quit()
        terminer=True
    elif continuer==True:
        niveau=0
        while not terminer:
            att=scenario.init(niveau)
            execute=scenario.execute(att,niveau)
            if execute==0:
                pygame.quit()
                terminer=True
            elif execute==1:
                att=scenario.init(niveau)
                pygame.display.update()  
            elif execute==2:
                niveau+=1
            elif execute==3:
                clock.tick(2)
                surface.fill((NOIR))
                titre_police=pygame.font.Font(None,70)
                titre1=titre_police.render("Bravo, vous avez fini le dernier niveau !",True, BLANC)
                surface.blit(titre1,[200,350])
                pygame.display.update()
                clock.tick(0.4)
                pygame.quit()
                terminer=True

    
    
# Commande qui permet de lancer automatiquement le programme               
if __name__ == '__main__':
    main()
