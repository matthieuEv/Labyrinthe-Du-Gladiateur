from os import sep
import colorama
from colorama.ansi import Back

TAILLE_PLATEAU_X = 80
TAILLE_PLATEAU_Y = 30

#Fonction qui initialise colorama
def init():
    colorama.init()
    clear()

#Fonction qui efface tout l'ecran
def clear():
    print("\x1b[2J\x1b[H",end="")

#Fonction qui simule l'effacement d'une ligne a partir d'un point 
def effaceLigne (x,y):
    print(colorama.Style.RESET_ALL)
    for i in range (150):
        posXY(x+i,y)
        print(' ')

#Fonction pour placer le curseur d'ecriture
def posXY(x,y):
    print("\x1b[%d;%dH"%(y,x),end="")

#Fonction pour clear le dessous du plateau
def clear_down ():
    posXY(0,31)
    for i in range (8):
        for i in range(30):
            print(' ',end='')
        print('\n',end='')
"""
Fonction pour changer le personnage a la fin du jeu
@param: 
    - liste a deux dim contenant le tableau 
    - liste avec les position pour afficher l'emoji
    - Un boolean a True si victoire
@return :
    - rien 
@author Elouan
"""
def graph_mort(tabLab,posafficher,vict):
    depXY = [TAILLE_PLATEAU_X//2 - len(tabLab[0]),TAILLE_PLATEAU_Y//2 - len(tabLab)//2]
    posXY(depXY[0]+(2*posafficher[0]),depXY[1]+posafficher[1])
    #Si c'est en cas de victoire 
    if vict :
        print(colorama.Back.LIGHTBLUE_EX,"\U0001f601",end='',sep='')
    else :
        print(colorama.Back.LIGHTGREEN_EX,"\U0001f480",end='',sep='')
    print(colorama.Style.RESET_ALL)
    posXY(0,31)

'''
Fonction qui affiche le labytinthe
// Cette fonction n'affiche que le lab Vide //
@param en entré : 
    - tableau  deux dimensions qui contient le lab a afficher 
@return :
    - rien 
@author Elouan
'''
def afficher_lab (tabLab):
    #Clear la console 
    clear()
    #afficher les contour de la zone de jeu (80x30):
    #D'abord le fond :
    for x in range(TAILLE_PLATEAU_X):
        for y in range(TAILLE_PLATEAU_Y):
            posXY(x,y)
            print(colorama.Back.LIGHTBLUE_EX," ",end='')
    #ensuite les contours :
    for x in range(TAILLE_PLATEAU_X):
        for y in range(TAILLE_PLATEAU_Y):
            posXY(x,y)
            if ((x == 0 or x == 80-1) or (y == 0 or y == 30-1)):
                print(colorama.Back.BLUE," ",end='')
    #Ensuite le lab en lui même :
    #on set les position de départ pour le centrer dans la zone de jeu
    depXY = [TAILLE_PLATEAU_X//2 - len(tabLab[0]),TAILLE_PLATEAU_Y//2 - len(tabLab)//2]
    #Ensuite on ballaye la taille du lab
    for x in range(len(tabLab)):
        for y in range(len(tabLab[x])):
            #On position le curseur a la position initiale plus la position dans le lab
            posXY(depXY[0]+(2*y),depXY[1]+x)
            #Si on est sur un mur -> Noir
            if (tabLab[x][y]):
                print(colorama.Back.BLACK,end='')
            #Sinon si on est sur une case inaccessible -> vert Foncé
            elif (not(x%2) or not(y%2)):
                print(colorama.Back.GREEN,end='')
            #Sinon -> Vert
            else:
                print(colorama.Back.LIGHTGREEN_EX,end='')
            #On affiche le double escpace pour faire une case pleine
            print("  ",end='')
    #Cette ligne permet d'être que l'on ne réérira pas sur le plateau de jeu
    posXY(0,31)
    #On reset les styles pour la suite
    print(colorama.Style.RESET_ALL)

'''
Fonction qui gère l'affichage d'un déplacement d'entité
@params:
    - La liste a deux dim contenant le tableau du lab
    - un entier contenant l'entite a afficher :
        - 0 = gladiateur
        - 1 = player
    - position de d'arrive = liste a deux dim X-Y 
    - position de départ = liste a deux dim X-Y 
        //Par defaut a -1 si pas de valeur de départ//
@return :
    rien 
@author Elouan
'''
def graph_deplacement_entite(tabLab,entite,posArr,posDep=[-1,-1]):
    depXY = [TAILLE_PLATEAU_X//2 - len(tabLab[0]),TAILLE_PLATEAU_Y//2 - len(tabLab)//2]
    if not(posDep[0]==-1):
        posXY(depXY[0]+(2*posDep[0]),depXY[1]+posDep[1])
        print(colorama.Back.LIGHTGREEN_EX,"  ",end='',sep='')
    if (posArr[0]>len(tabLab[0])-1 or posArr[1]>len(tabLab)-1):
        print(colorama.Back.LIGHTBLUE_EX,end='')
    else :
        print(colorama.Back.LIGHTGREEN_EX,end='')
    posXY(depXY[0]+(2*posArr[0]),depXY[1]+posArr[1])
    if entite :
        print("\U0001f628",end='',sep='')
    else:
        print("\U0001f608",end='',sep='')
    posXY(0,31)
    print(colorama.Style.RESET_ALL)


"""
Créée le fond d'écran du menu
@params:
    - None
@return:
    - None
@author Matthieu
"""
def background():
    for x in range(TAILLE_PLATEAU_X):
        for y in range(TAILLE_PLATEAU_Y):
            posXY(x,y)
            print(Back.LIGHTBLUE_EX," ",end='')
    #ensuite les contours :
    for x in range(TAILLE_PLATEAU_X):
        for y in range(TAILLE_PLATEAU_Y):
            posXY(x,y)
            if ((x == 0 or x == 80-1) or (y == 0 or y == 30-1)):
                print(Back.BLUE," ",end='')
    print(colorama.Style.RESET_ALL)


