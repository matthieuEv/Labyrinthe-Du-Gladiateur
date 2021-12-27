import pygame
import os
#import des constantes 
from pygameFile import HAUTEUR,LARGEUR,TAILLE_CARRE,WHITE,LIGHTBLUE,BLUE,GREEN,DARKGREEN,BLACK,RED,YELLOW,PINK,PURPLE
#Import des fonction
from pygameFile import getEvent,fondDecran,updateScreen,closePygame
from outils import write_save_file,read_save_file,recupLeaderboard

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
                return(r,0)
        elif rep == 1:
            r,hist  = menuHistoire(screen)
            if (r != 0):
                return(r,hist)
        elif rep == 2:
            leaderboardPygame(screen)
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

"""
fonction qui permet d'afficher le mode histoire:
@param
    - l'écran dans screen
@return 
    - int aveec le numéro du lab ou 0 si retour
    - le numéro du mode histoire 
"""
def menuHistoire(screen):
    base(screen)
    fo = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)

    rep,action = True,False
    ligne,oldLigne = 0, -1
    while(rep):
        profils = read_save_file("save")
        txt = ['Sauvgarde N°1 - '+str(read_save_file("save")[0][0]),'Sauvgarde N°2 - '+str(read_save_file("save")[0][1]),'Sauvgarde N°3 - '+str(read_save_file("save")[0][2]),'Retour','Play','Supr'] 
        objtxt = [fo.render(txt[i],False,(0,0,0)) for i in range(6)]
        pos = [200,300,400,550]
        for i in range (3):
            screen.blit(objtxt[i],((LARGEUR//2)-objtxt[i].get_width(),pos[i]))
        screen.blit(objtxt[3],((LARGEUR//2)-objtxt[3].get_width()//2,pos[3]))
        if oldLigne!= -1:
            pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2-objtxt[oldLigne].get_width()-25),pos[oldLigne],20,20)))
        screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),((LARGEUR//2-objtxt[ligne].get_width()-25),pos[ligne]))
        updateScreen()
        for event in getEvent():
            if event.type == pygame.QUIT:
                closePygame()
                exit()
            if event.type == pygame.KEYUP:
                if (event.key == ord('z') and ligne!=0):
                    oldLigne = ligne
                    ligne -= 1
                elif (event.key == ord('s') and ligne != 3):
                    oldLigne = ligne
                    ligne += 1
                elif (event.key == ord(' ')):
                    if ligne != 3:
                        action = True
                        case, oldcase = 0,-1
                        screen.blit(objtxt[4],((LARGEUR//2)+40,pos[ligne]))
                        screen.blit(objtxt[5],((LARGEUR//2)+objtxt[4].get_width()+80,pos[ligne]))
                    else:
                        rep =False
        while(action):
            pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2-objtxt[ligne].get_width()-25),pos[ligne],20,20)))
            if oldcase!= -1:
                pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2+15+((objtxt[4].get_width()+40) if case==0 else 0)),pos[ligne],20,20)))
            screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),(LARGEUR//2+15+((objtxt[4].get_width()+40)if case == 1 else 0),pos[ligne]))
            updateScreen()
            for event in getEvent():
                if event.type == pygame.QUIT:
                    closePygame()
                    exit()
                if event.type == pygame.KEYUP:
                    if (event.key == ord('q') and case == 1):
                        oldcase = case
                        case = 0
                    elif (event.key == ord('d') and case == 0):
                        oldcase = case
                        case = 1
                    elif (event.key == ord(' ')):
                        if case:
                            profils[0][ligne]='1'
                            write_save_file("save",profils)
                            action=False
                            base(screen)
                            pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2+15+objtxt[4].get_width()+40,pos[ligne],20,20))))
                        else:
                            rep,action=False,False
    if ligne==3:
        return(0,0)
    else:
        return(int(profils[0][ligne]),ligne)
'''
Fonction qui permet l'affichage du leaderboard 
@param
    - screen comprenant l'écran
@return 
    - rien
'''
def leaderboardPygame(screen):
    base(screen)
    lstLead = recupLeaderboard()
    fo = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)
    text = [[str('|'+ str(i) + ' - '+str('Vide' if lstLead[i-1]=='999' else lstLead[i-1])) for i in range(1,7)],[str('|'+ str(i)+ ' - '+str('Vide' if lstLead[i-1]=='999' else lstLead[i-1])) for i in range(7,13)]]
    objtxt = [[fo.render(text[0][i],False,(0,0,0)) for i in range(6)],[fo.render(text[1][i],False,(0,0,0)) for i in range(6)]]
    ecart = (1280-60)//7 
    pos = [[[ecart+i*ecart,300+t*200] for i in range(6)] for t in range(2)]
    for ligne in range(2):
        for case in range(6):
            screen.blit(objtxt[ligne][case],(pos[ligne][case][0]-objtxt[ligne][case].get_width()//2,pos[ligne][case][1]))
    screen.blit(fo.render('Retour',False,(0,0,0)),((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width()//2,650))
    screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width(),650))
    updateScreen()

    rep = True
    while(rep):
        for event in getEvent():
                if event.type == pygame.QUIT:
                    closePygame()
                    exit()
                elif event.type == pygame.KEYUP:
                    if (event.key == ord(' ')):
                        rep = False

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