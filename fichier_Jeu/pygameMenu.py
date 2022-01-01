import pygame
import os

from pygame.constants import  K_DOWN, K_RETURN, K_SPACE, K_UP, K_RIGHT, K_LEFT, K_s, K_z, K_q, K_d
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
            #Si on sort de la fonction avec autre chose que retour on renvoie le lab choisi
            if (r != 0):
                return(r,0)
        #Si le joueur veut aller en mode histoire
        elif rep == 1:
            r,hist  = menuHistoire(screen)
            #Si on sort de la fonction avec autre chose que retour, on revoie la save et le lab ou elle est rendu
            if (r != 0):
                return(r,hist+1)
        #Si le joeur veut voir le leaderboard
        elif rep == 2:
            leaderboardPygame(screen)
    #Quitter le jeu
    if rep == 3:
        #fermer la fenêtre puis le programme 
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
    #On efface la fenêtre et on remet le titre 
    base(screen)
    #On crée la police d'écriture (j'aurai aimer la définir en constante, cependant elle nessessite que l'outils soit initialiser pour être crée)
    fo = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)
    #On crée la liste des textes a afficher 
    txt = ['Mode Arcade','Mode Histoire','Leaderboard','Quitter'] 
    #On crée le rendu des objets texte
    objtxt = [fo.render(txt[i],False,(0,0,0)) for i in range(4)]
    #On donne leurs position 
    pos = [200,300,400,550]
    #On les ajoute a l'affichage 
    for i in range (4):
        screen.blit(objtxt[i],((LARGEUR//2)-objtxt[i].get_width()//2,pos[i]))

    rep = True
    ligne = 0
    oldLigne = -1
    #Tant que le joueur n'as pas répondu
    while(rep):
        #Element permettant d'effacer la flèche lors d'un mouvement 
        if oldLigne!= -1:
            pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2-objtxt[oldLigne].get_width()//2-25),pos[oldLigne],20,20)))
        #Affichage de la flèche
        screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),((LARGEUR//2-objtxt[ligne].get_width()//2-25),pos[ligne]))
        #On met a jour l'écran
        updateScreen()

        #Gestion des évènements 
        for event in getEvent():
            #Si on ferme la fenêtre 
            if event.type == pygame.QUIT:
                #fermer la fenêtre puis le programme 
                closePygame()
                exit()
            #Si une touche est levé (on prend levé pour éviter les repétition)
            elif event.type == pygame.KEYUP:
                #Si la touche en question est z ou la flèche du haut et si on est pas encore au maximum
                if ((event.key in [K_z,K_UP]) and ligne!=0):
                    oldLigne = ligne
                    ligne -= 1
                elif ((event.key in [K_s,K_DOWN]) and ligne != 3):
                    oldLigne = ligne
                    ligne += 1
                #Si c'est expace ou entré on valide
                elif (event.key in [K_SPACE,K_RETURN]):
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
    #On efface la fenêtre et on remet le titre 
    base(screen)
    #On crée la police d'écriture
    fo = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)
    #On fait le rendu et le l'affichage du sous-titre
    t = fo.render("Choisissez un niveau entre 1 et 12",False,(0,0,0))
    screen.blit(t,((LARGEUR//2)-t.get_width()//2,200))

    #On génère les textes à afficher, on les rend, on indique ensuitre leurs position puis on les affiches 
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
    #On gère les entré utilisateur
    while(rep):
        #Option pour effacer les flèches lors de mouvment 
        if oldplace[0] != -1:
            if oldplace[0]==2:
                pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width()//2-25,650,20,20))
            else:
                pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(pos[oldplace[0]][oldplace[1]][0]-objtxt[oldplace[0]][oldplace[1]].get_width()//2-25,pos[oldplace[0]][oldplace[1]][1],20,20))
        #Affichages des flèche des selection.
        if place[0]==2:
            screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),(((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width()//2-25,650)))
        else:
            screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),(pos[place[0]][place[1]][0]-objtxt[place[0]][place[1]].get_width()//2-25,pos[place[0]][place[1]][1]))
        updateScreen()

        #Gestion des évènements
        for event in getEvent():
            #Si on ferme la fenêtre
            if event.type == pygame.QUIT:
                #fermer la fenêtre puis le programme 
                closePygame()
                exit()
            #Si une touche est levé (on prend levé pour éviter les repétition)
            elif event.type == pygame.KEYUP:
                #On gère ensuite les différentes touches 
                if ((event.key in [K_z,K_UP]) and place[0]!=0):
                    oldplace = [place[i] for i in range(len(place))]
                    place[0] -= 1 
                elif ((event.key in [K_s,K_DOWN]) and place[0] != 2):
                    oldplace = [place[i] for i in range(len(place))]
                    place[0] += 1
                elif ((event.key in [K_q,K_LEFT]) and place[1] != 0):
                    oldplace = [place[i] for i in range(len(place))]
                    place[1] -= 1
                elif ((event.key in [K_d,K_RIGHT]) and place[1] != 5):
                    oldplace = [place[i] for i in range(len(place))]
                    place[1] += 1
                elif (event.key in [K_SPACE,K_RETURN]):
                    rep = False
    #On retourne le labyrinthe choisi 
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
    #On efface la fenêtre et on remet le titre 
    base(screen)
    #On crée la police d'écriture
    fo = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)

    #Dans cette fonction la quasi-totalité est dans une boucle car les action du joueur peuvent faire varier l'affichage

    rep,action = True,False
    ligne,oldLigne = 0, -1
    #tant que le joueur n'as pas choisi 
    while(rep):
        #On lis le fichier de save dans une liste
        profils = read_save_file("save")
        #On crée les texte a affciher avec les numéro de lab associer a chaque save
        txt = ['Sauvgarde N°1 - '+str(read_save_file("save")[0][0]),'Sauvgarde N°2 - '+str(read_save_file("save")[0][1]),'Sauvgarde N°3 - '+str(read_save_file("save")[0][2]),'Retour','Play','Supr'] 
        #on fait le rendu de chaque texte
        objtxt = [fo.render(txt[i],False,(0,0,0)) for i in range(6)]
        #on donne leurs position 
        pos = [200,300,400,550]
        #on affiche chaque texte sur l'écran
        for i in range (3):
            screen.blit(objtxt[i],((LARGEUR//2)-objtxt[i].get_width(),pos[i]))
        #On affiche retour
        screen.blit(objtxt[3],((LARGEUR//2)-objtxt[3].get_width()//2,pos[3]))

        #Gestion de la flèche de selection
        if oldLigne!= -1:
            pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2-objtxt[oldLigne].get_width()-25),pos[oldLigne],20,20)))
        screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),((LARGEUR//2-objtxt[ligne].get_width()-25),pos[ligne]))
        updateScreen()

        #première gestion des événement pour le choix de la save
        for event in getEvent():
            #Si on ferme la fenêtre
            if event.type == pygame.QUIT:
                #fermer la fenêtre puis le programme 
                closePygame()
                exit()
            #Si une touche est levé (on prend levé pour éviter les repétition)
            if event.type == pygame.KEYUP:
                if ((event.key in [K_z,K_UP]) and ligne!=0):
                    oldLigne = ligne
                    ligne -= 1
                elif ((event.key in [K_s,K_DOWN]) and ligne != 3):
                    oldLigne = ligne
                    ligne += 1
                elif (event.key in [K_SPACE,K_RETURN]):
                    #Si le joueur valide une save on affiche les option qu'il a avec cette save sauf si c'est retour auquel cas on sort simplement
                    if ligne != 3:
                        action = True
                        case, oldcase = 0,-1
                        screen.blit(objtxt[4],((LARGEUR//2)+40,pos[ligne]))
                        screen.blit(objtxt[5],((LARGEUR//2)+objtxt[4].get_width()+80,pos[ligne]))
                    else:
                        rep =False
        
        #Quand le joueur a choisi une save il peut alors la jouer ou l'effacer
        while(action):
            #On affiche les choix 
            pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2-objtxt[ligne].get_width()-25),pos[ligne],20,20)))
            #Gestion de la flèche
            if oldcase!= -1:
                pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(((LARGEUR//2+15+((objtxt[4].get_width()+40) if case==0 else 0)),pos[ligne],20,20)))
            screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),(LARGEUR//2+15+((objtxt[4].get_width()+40)if case == 1 else 0),pos[ligne]))
            updateScreen()

            #Gestion des évènements pour le choix de l'action 
            for event in getEvent():
                #Si on ferme la fenêtre
                if event.type == pygame.QUIT:
                    #fermer la fenêtre puis le programme 
                    closePygame()
                    exit()
                #Si une touche est levé (on prend levé pour éviter les repétition)
                if event.type == pygame.KEYUP:
                    if ((event.key in [K_q,K_LEFT]) and case == 1):
                        oldcase = case
                        case = 0
                    elif ((event.key in [K_d,K_RIGHT]) and case == 0):
                        oldcase = case
                        case = 1
                    elif (event.key in [K_SPACE,K_RETURN]):
                        #Si le joueur choisi de suprimer alors on remet a 0 la save en question
                        if case:
                            profils[0][ligne]='1'
                            write_save_file("save",profils)
                            action=False
                            #On efface la fenêtre et on remet le titre puis on réaffiche les save avec chaque niveau a jour
                            base(screen)
                        else:
                            #Sinon on sort des deux boucles
                            rep,action=False,False
    #Si on a choisi retour on sort 0 
    if ligne==3:
        return(0,0)
    else:
        #Sinon on retourne la save et le niveau auquel on est rendu
        return(int(profils[0][ligne]),ligne)


'''
Fonction qui permet l'affichage du leaderboard 
@param
    - screen comprenant l'écran
@return 
    - rien
'''
def leaderboardPygame(screen):
    #On efface la fenêtre et on remet le titre 
    base(screen)
    lstLead = recupLeaderboard()
    #On crée la police d'écriture
    fo = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)
    #On crée les textes à afficher avec les meilleurs scores
    text = [[str('|'+ str(i) + ' - '+str('Vide' if lstLead[i-1]=='999' else lstLead[i-1])) for i in range(1,7)],[str('|'+ str(i)+ ' - '+str('Vide' if lstLead[i-1]=='999' else lstLead[i-1])) for i in range(7,13)]]
    #On fait le rendu de chaque objets
    objtxt = [[fo.render(text[0][i],False,(0,0,0)) for i in range(6)],[fo.render(text[1][i],False,(0,0,0)) for i in range(6)]]
    #On calcul l'écart entre chaque score
    ecart = (1280-60)//7 
    #On utilise ça pour enregistre chaque position 
    pos = [[[ecart+i*ecart,300+t*200] for i in range(6)] for t in range(2)]

    #on fait affiche chaque score
    for ligne in range(2):
        for case in range(6):
            screen.blit(objtxt[ligne][case],(pos[ligne][case][0]-objtxt[ligne][case].get_width()//2,pos[ligne][case][1]))
    
    #On affiche le bouton retour et la flèche devant 
    screen.blit(fo.render('Retour',False,(0,0,0)),((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width()//2,650))
    screen.blit(pygame.image.load(os.path.join('resources/arrow.png')),((LARGEUR//2)-fo.render('Retour',False,(0,0,0)).get_width(),650))
    updateScreen()

    rep = True
    while(rep):
        for event in getEvent():
            #Si on ferme la fenêtre
                if event.type == pygame.QUIT:
                    #fermer la fenêtre puis le programme 
                    closePygame()
                    exit()
                #Si une touche est levé (on prend levé pour éviter les repétition)
                elif event.type == pygame.KEYUP:
                    #Si on valide on sort simplement de la fonction
                    if (event.key in [K_SPACE,K_RETURN]):
                        rep = False

'''
fonction qui efface l'ecran et affiche le titre :
@param :
    - screen contenant l'écran 
@return:
    - rien 
'''
def base(screen):
    #On affiche le fond d'écran
    fondDecran(screen)
    #On crée et on affiche le titre
    titre = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),50).render('===== Labyrinthe Du Gladiateur =====',False,(0,0,0))
    screen.blit(titre,((LARGEUR//2)-titre.get_width()//2,50))