import colorama
from outils import user_input
from color import clear,posXY,init
from colorama import Fore, Back


TAILLE_PLATEAU_X = 80
TAILLE_PLATEAU_Y = 30

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


def menu():
    init()
    while(1):
        clear()
        background()
        posXY(20,11)
        print(Back.LIGHTBLUE_EX,Fore.BLACK,"▬▬▬▬▬ Labyrinthe Du Gladiateur ▬▬▬▬▬")
        posXY(23,13)
        print("• Choisir le labyrinthe (1)")
        posXY(23,14)
        print("• Quitter le jeu (0)")
        posXY(23,17)
        #run = soit 0, soit 1, pas autre choses)
        run=user_input([0,1])
        #si run = 0, on quitte tout
        if run == 0:
            print(colorama.Style.RESET_ALL)
            clear()
            exit()

        elif run == 1:
            print(colorama.Style.RESET_ALL)
            clear()
            background()

            posXY(20,11)
            print(Back.LIGHTBLUE_EX,Fore.BLACK,"▬▬▬▬▬ Labyrinthe Du Gladiateur ▬▬▬▬▬")

            posXY(23,13)
            print("• Choisissez un labyrinthe entre 1 et 12")

            posXY(23,14)
            print("• Quitter le choix du labyrithe (0)")
            #choixLaby est compris entre 0 et 12

            posXY(23,17)
            choixLaby = user_input([0,1,2,3,4,5,6,7,8,9,10,11,12])
            print(colorama.Style.RESET_ALL)
            if choixLaby != 0:
                clear()
                return choixLaby
            #si choixLaby = 0, retour au menu de base

if __name__ == "__main__":
    print(menu())