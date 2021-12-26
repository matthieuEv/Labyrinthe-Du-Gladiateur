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
    rep = -1
    while (rep!=3):
        #On affiche le menu principal 
        rep = menuPrincipal(screen)
        #Si le joueur veux aller sur le mode arcade 
        if rep == 0:
            r  = menuArcade(screen)
            if (r != 0):
                return(r)
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
    base(screen)
    fo = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)
    txt = ['Mode Arcade','Mode Histoire','Leaderboard','Quitter'] 
    objtxt = [fo.render(txt[i],False,(0,0,0)) for i in range(4)]
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
                closePygame()
                exit()
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

"""
Fonction pour le mode arcade :
@param :
    - screen contenant l'écran
@return : 
    - int aveec le numéro du lab ou 0 si retour
"""
def menuArcade(screen):
    base(screen)
    fo = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)
    t = fo.render("Choisissez un niveau entre 1 et 12",False,(0,0,0))
    screen.blit(t,((LARGEUR//2)-t.get_width()//2,200))

    text = [[str('|'+ str(i)) for i in range(1,7)],[str('|'+ str(i)) for i in range(7,13)]]
    objtxt = [[fo.render(text[0][i],False,(0,0,0)) for i in range(6)],[fo.render(text[1][i],False,(0,0,0)) for i in range(6)]]
    ecart = (1280-60)//7 
    pos = [[[ecart+i*ecart,300+t*200] for i in range(6)] for t in range(2)]
    for ligne in range(2):
        for case in range(6):
            screen.blit(objtxt[ligne][case],(pos[ligne][case][0]-objtxt[ligne][case].get_width()//2,pos[ligne][case][1]))
    screen.blit(fo.render('Retour',False,(0,0,0)),((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width()//2,650))


    rep = True
    place = [0,0]
    oldplace = [-1,-1]
    while(rep):
        if oldplace[0] != -1:
            if oldplace[0]==2:
                pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width()//2-25,650,20,20))
            else:
                pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(pos[oldplace[0]][oldplace[1]][0]-objtxt[oldplace[0]][oldplace[1]].get_width()//2-25,pos[oldplace[0]][oldplace[1]][1],20,20))
        if place[0]==2:
            screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),(((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width()//2-25,650)))
        else:
            screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),(pos[place[0]][place[1]][0]-objtxt[place[0]][place[1]].get_width()//2-25,pos[place[0]][place[1]][1]))
        updateScreen()
        for event in getEvent():
            if event.type == pygame.QUIT:
                closePygame()
                exit()
            elif event.type == pygame.KEYUP:
                if (event.key == ord('z') and place[0]!=0):
                    oldplace = [place[i] for i in range(len(place))]
                    place[0] -= 1 
                elif (event.key == ord('s') and place[0] != 2):
                    oldplace = [place[i] for i in range(len(place))]
                    place[0] += 1
                elif (event.key == ord('q') and place[1] != 0):
                    oldplace = [place[i] for i in range(len(place))]
                    place[1] -= 1
                elif (event.key == ord('d') and place[1] != 5):
                    oldplace = [place[i] for i in range(len(place))]
                    place[1] += 1
                elif (event.key == ord(' ')):
                    rep = False
    return((place[1]+1)+6*place[0] if place[0]!=2 else 0)


'''
fonction qui efface l'ecran et affiche le titre :
@param :
    - screen contenant l'écran 
@return:
    - rien 
'''
def base(screen):
    fondDecran(screen)
    titre = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),50).render('===== Labyrinthe Du Gladiateur =====',False,(0,0,0))
    screen.blit(titre,((LARGEUR//2)-titre.get_width()//2,50))