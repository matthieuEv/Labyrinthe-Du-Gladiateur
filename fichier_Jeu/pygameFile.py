import pygame
from pygame.constants import  K_DOWN, K_RETURN, K_SPACE, K_UP, K_RIGHT, K_LEFT, K_m, K_r, K_s, K_z, K_q, K_d, K_m
import os

#Taille
HAUTEUR = 720
LARGEUR = 1280
TAILLE_CARRE = 20
#Couleurs
WHITE = (255,255,255)
LIGHTBLUE = (114,159,207)
BLUE = (52,101,164)
GREEN = (0,255,0)
DARKGREEN = (78,154,6)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
PINK = (168,50,117)
PURPLE = (119,50,168)

"""
Fonction pour crée la fenêtre 
Argument :
    - rien 
Retourne :
    - un object fenêtre
"""
def pgInit():
    pygame.init()
    return(pygame.display.set_mode((LARGEUR,HAUTEUR)))

"""
Fonction pour recuperer les event
argument :
    - rien 
retourne :
    - les events
"""
def getEvent():
    return(pygame.event.get())

"""
Fonction pour mettre à jour l'ecran 
argument : 
    -rien 
retourne :
    - rien 
"""
def updateScreen():
    pygame.display.flip()

"""
Fonction pour afficher le fond d'ecran
argument:
    - une fenêtre 
retourne :
    - rien
"""
def fondDecran(screen):
    screen.fill(BLUE)
    pygame.draw.rect(screen,LIGHTBLUE,pygame.Rect(30,30,(LARGEUR-60),(HAUTEUR-60)))

"""
Fonction qui affiche un lab 
argument:
    - une fenêtre 
    - un lab (tableau a deux dim)
retourne :
    - rien 
"""
def pgAfficherLab(screen,lab):
    dep = [LARGEUR//2 - (len(lab[0])//2)*TAILLE_CARRE,HAUTEUR//2 - (len(lab)//2)*TAILLE_CARRE]
    for x in range(len(lab[0])) :
        for y in range(len(lab)):
            if lab[y][x]:
                pygame.draw.rect(screen,BLACK,pygame.Rect(dep[0],dep[1],TAILLE_CARRE,TAILLE_CARRE))
            elif (x%2==0 or y%2==0):
                pygame.draw.rect(screen,DARKGREEN,pygame.Rect(dep[0],dep[1],TAILLE_CARRE,TAILLE_CARRE))
            else:
                pygame.draw.rect(screen,GREEN,pygame.Rect(dep[0],dep[1],TAILLE_CARRE,TAILLE_CARRE))

            dep[1] = dep[1]+TAILLE_CARRE
        dep = [dep[0]+TAILLE_CARRE,HAUTEUR//2 - (len(lab)//2)*TAILLE_CARRE]


"""
Fonction pour gérer le déplacement d'une entité sur le plalteau 
Arguments:
    - un objet screen
    - La liste a deux dim contenant le tableau du lab
    - un entier contenant l'entite a afficher :
        - 0 = gladiateur
        - 1 = player
    - position de d'arrive = liste a deux dim X-Y 
    - position de départ = liste a deux dim X-Y 
        //Par defaut a -1 si pas de valeur de départ//
retourne :
    rien 
"""
def pgDeplacementEntite(screen,tabLab,entite,posArr,posDep=[-1,-1]):
    dep = [LARGEUR//2 - (len(tabLab[0])//2)*TAILLE_CARRE,HAUTEUR//2 - (len(tabLab)//2)*TAILLE_CARRE]
    base_path = os.path.dirname(__file__)
    if (posDep[0]!=-1):
        pygame.draw.rect(screen,GREEN,pygame.Rect(dep[0]+TAILLE_CARRE*posDep[0],dep[1]+TAILLE_CARRE*posDep[1],TAILLE_CARRE,TAILLE_CARRE))
    if entite :
        #pygame.draw.rect(screen,YELLOW,pygame.Rect(dep[0]+TAILLE_CARRE*posArr[0],dep[1]+TAILLE_CARRE*posArr[1],TAILLE_CARRE,TAILLE_CARRE))
        screen.blit(pygame.image.load(os.path.join(base_path,"resources/player.png")),(dep[0]+TAILLE_CARRE*posArr[0],dep[1]+TAILLE_CARRE*posArr[1]))
    else:
        #pygame.draw.rect(screen,RED,pygame.Rect(dep[0]+TAILLE_CARRE*posArr[0],dep[1]+TAILLE_CARRE*posArr[1],TAILLE_CARRE,TAILLE_CARRE))
        screen.blit(pygame.image.load(os.path.join(base_path,"resources/glad.png")),(dep[0]+TAILLE_CARRE*posArr[0],dep[1]+TAILLE_CARRE*posArr[1]))

"""
check if EXIT is clicked
argument:
    - int contenant l'event
return :
    - True si c'est un event exit False sinon
"""
def eventQuit(a):
    return(a == pygame.QUIT)


"""
Fonction qui permet de récupérer le sens de déplacement en fonction des imput clavier
Argument :
    - l'event 
    - les diréction disponible
retourne : 
    - le numéro de la direction choisi 
"""
def eventArrow(e,dir):
    if e.type == pygame.QUIT:
        closePygame()
        return(10)
    if e.type == pygame.KEYUP:
        if ((e.key in [K_d,K_RIGHT]) and dir[0]):
            return(1)
        elif ((e.key in [K_q,K_LEFT]) and dir[1]):
            return(2)
        elif ((e.key in [K_z,K_UP]) and dir[2]):
            return(3)
        elif ((e.key in [K_s,K_DOWN]) and dir[3]):
            return(4)
        elif ((e.key in [K_SPACE,K_RETURN])):
            return(0)
        elif (e.key == K_m):
            return(10)
    return(-1)

"""
Fonction pour fermer l'ecran pygame
Agument :
    - rien 
Retourne :
    - rien 
"""
def closePygame():
    pygame.display.quit()
    pygame.quit()

"""
Fonction pour changer le personnage a la fin du jeu
argument: 
    - un object screen
    - liste a deux dim contenant le tableau 
    - Un boolean a True si victoire
retourne :
    - rien 
"""
def  pgGraphEndGame(screen,vict,best=False):
    pygame.font.init()
    myfont = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),50)
    myfont2 = pygame.font.SysFont(os.path.join('resources/fonts/Roboto-Medium.ttf'),30)
    if vict : 
        textsurface = myfont.render('WIN', False, (0, 0, 0))
        textsurface2 = myfont2.render('Appuyer sur Entre pour continer',False,(0,0,0))
            
    else:
        textsurface = myfont.render('LOOSE', False, (0, 0, 0))
        textsurface2 = myfont2.render('Appuyer sur Entre pour continer et R pour recommencer',False,(0,0,0))
    screen.blit(textsurface,(575,50))
    
    if best:
        screen.blit(myfont.render('Nouveau meilleur',False,(0,0,0)),(575,670))
    screen.blit(textsurface2,(LARGEUR-textsurface2.get_width()-30,700))
    updateScreen()
    rep = True
    while(rep):
        for event in getEvent():
            if event.type == pygame.QUIT:
                closePygame()
                exit()
            elif event.type == pygame.KEYUP:
                if (event.key in [K_SPACE,K_RETURN]):
                    return(False)
                elif (event.key == K_r and not(vict)):
                    return(True)