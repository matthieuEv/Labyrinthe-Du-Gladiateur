import colorama
from colorama.initialise import reset_all
from outils import read_save_file, user_input, user_input_str,testSaveExist, write_save_file
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
        print("• Choisir le mode Arcade (1)")
        posXY(23,14)
        print("• Choisir le mode Histoire (2)")
        posXY(23,15)
        print("• Quitter le jeu (0)")
        #run = soit 0, soit 1, pas autre choses)
        run=user_input([0,1,2],isPos=True,pos=[23,18])

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
            choixLaby = user_input([0,1,2,3,4,5,6,7,8,9,10,11,12],isPos=True,pos=[23,17])
            print(colorama.Style.RESET_ALL)
            if choixLaby != 0:
                clear()
                return choixLaby
            #si choixLaby = 0, retour au menu de base

        elif run == 2:
            print(colorama.Style.RESET_ALL)
            clear()
            background()
            posXY(20,11)
            print(Back.LIGHTBLUE_EX,Fore.BLACK,"▬▬▬▬▬ Labyrinthe Du Gladiateur ▬▬▬▬▬")
            profils = read_save_file("save")
            posXY(23,13)
            print("• Choisir une sauvegarde (1)")
            posXY(23,14)
            # print("• Créer une sauvegarde (2)")
            # posXY(23,15)
            print("• Quitter menu (0)")
            #run = soit 0, soit 1, pas autre choses)
            choose=user_input([0,1],isPos=True,pos=[23,18])
            print(colorama.Style.RESET_ALL)


            if choose == 1: #choisir la sauvegarde
                print(colorama.Style.RESET_ALL)
                clear()
                background()

                currentLvl1=read_save_file("save")[0][0]
                currentLvl2=read_save_file("save")[0][1]
                currentLvl3=read_save_file("save")[0][2]

                posXY(20,11)
                print(Back.LIGHTBLUE_EX,Fore.BLACK,"▬▬▬▬▬ Labyrinthe Du Gladiateur ▬▬▬▬▬")

                posXY(23,13)
                print("• Jouer sur la sauvegarde 1 (1)")
                posXY(27,14)
                print("Niveau actuel: ", currentLvl1)

                posXY(23,16)
                print("• Jouer sur la sauvegarde 2 (2)")
                posXY(27,17)
                print("Niveau actuel: ", currentLvl2)


                posXY(23,19)
                print("• Jouer sur la sauvegarde 3 (3)")
                posXY(27,20)
                print("Niveau actuel: ", currentLvl3)


                posXY(23,22)
                print("• Quitter menu (0)")

                choose=user_input([0,1,2,3],isPos=True,pos=[23,24])
                return choose


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
    return(user_input(possibility,True,[0,34+len(dir_possible)]))
    

if __name__ == "__main__":
    print(menu())