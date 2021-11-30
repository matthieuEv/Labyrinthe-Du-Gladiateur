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