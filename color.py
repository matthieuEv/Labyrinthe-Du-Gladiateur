import colorama

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

'''
Fonction qui affiche le labytinthe
// Cette fonction n'affiche pour l'instant que le lab Vide //
Argument en entré : 
    - tableau  deux dimensions qui contient le lab a afficher 
Retoure :
    - rien 
'''
def afficher_lab (tabLab):
    #Clear la console 
    clear()
    #afficher les contour de la zone de jeu (80x30):
    #D'abord le fond :
    for x in range(40*2):
        for y in range(30):
            posXY(x,y)
            print(colorama.Back.LIGHTBLUE_EX," ",end='')
    #ensuite les contours :
    for x in range(40*2):
        for y in range(30):
            posXY(x,y)
            if ((x == 0 or x == 80-1) or (y == 0 or y == 30-1)):
                print(colorama.Back.BLUE," ",end='')
    #Ensuite le lab en lui même :
    #on set les position de départ pour le centrer dans la zone de jeu
    depXY = [40 - len(tabLab),15 - len(tabLab[1])//2]
    #Ensuite on ballaye la taille du lab
    for x in range(len(tabLab)):
        for y in range(len(tabLab[x])):
            #On position le curseur a la position initiale plus la position dans le lab
            posXY(depXY[0]+(2*x),depXY[1]+y)
            #Si on est sur un mur -> Noir
            if (tabLab[y][x]):
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


    