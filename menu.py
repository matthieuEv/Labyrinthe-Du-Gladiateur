import colorama
from outils import user_input
from color import clear,posXY,init,clear_down,background
from colorama import Fore, Back


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


def menu_joueur_jeu(dir_possible):
    nomDir = ["Est","Ouest","Nord","Sud"]
    possibility = [10,0]
    clear_down()
    posXY(0,31)
    print("Quel direction voulez vous ?")
    print("(0) - Ne pas bouger")
    for i in range(len(dir_possible)):
        if (dir_possible[i]):
            print("(%d) - %s"%(i+1,nomDir[i]))
            possibility.append(i+1)
    print("(10) - Quitter")
    return(user_input(possibility,"int",True,[0,34+len(dir_possible)]))
    

if __name__ == "__main__":
    print(menu())