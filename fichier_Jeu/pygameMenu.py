from typing import Text
import pygame
import os
#import des constantes 
from pygameFile import HAUTEUR,LARGEUR,TAILLE_CARRE,WHITE,LIGHTBLUE,BLUE,GREEN,DARKGREEN,BLACK,RED,YELLOW,PINK,PURPLE
#Import des fonction
from pygameFile import getEvent,fondDecran,updateScreen,closePygame

'''
fonction Principale des menus
@param :
    - screen
@return :
    - nblab à jouer
'''
def menuPygame(screen):

    fondDecran(screen)
    titre = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),50).render('===== Labyrinthe Du Gladiateur =====',False,(0,0,0))
    screen.blit(titre,((LARGEUR//2)-titre.get_width()//2,50))

    rep = -1
    while (rep!=3):
        #On affiche le menu principal 
        rep = menuPrincipal(screen)
        #Si le joueur veux aller sur le mode arcade 
        if rep == 0:
            pass
        elif rep == 1:
            pass
        elif rep == 2:
            pass
    #Quitter le jeuÒ
    if rep == 3:
        closePygame()
        exit()

"""
Fonction de gestion du menu principal 
@param
    - screen contient l'écran
@return 
    - int contenant le choix du joueur 
        - 0 mode arcade 
        - 1 mode histoire
        - 2 Leaderboard 
        - 3 Quitter 
"""
def menuPrincipal (screen):
    f = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)
    txt = ['Mode Arcade','Mode Histoire','Leaderboard','Quitter'] 
    objtxt = [f.render(txt[i],False,(0,0,0)) for i in range(4)]
    pos = [200,300,400,550]
    for i in range (4):
        screen.blit(objtxt[i],((LARGEUR//2)-objtxt[i].get_width()//2,pos[i]))

    rep = True
    ligne = 0
    oldLigne = -1
    while(rep):
        if oldLigne!= -1:
            pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2-objtxt[oldLigne].get_width()//2-25),pos[oldLigne],20,20)))
        screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),((LARGEUR//2-objtxt[ligne].get_width()//2-25),pos[ligne]))
        updateScreen()
        for event in getEvent():
            if event.type == pygame.QUIT:
                return(0)
            elif event.type == pygame.KEYUP:
                if (event.key == ord('z') and ligne!=0):
                    oldLigne = ligne
                    ligne -= 1
                elif (event.key == ord('s') and ligne != 3):
                    oldLigne = ligne
                    ligne += 1
                elif (event.key == ord(' ')):
                    rep = False
    return(ligne)
