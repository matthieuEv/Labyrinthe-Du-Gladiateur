import colorama
from colorama.ansi import Style
from outils import recupLeaderboard, user_input
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
        print("• Leaderboard (2)")
        posXY(23,15)
        print("• Quitter le jeu (0)")
        #run = soit 0, soit 1, pas autre choses)
        run=user_input([0,1,2],isPos=True,pos=[23,17])
        #si run = 0, on quitte tout
        print(colorama.Style.RESET_ALL)
        if run == 0:
            print(colorama.Style.RESET_ALL)
            clear()
            exit()

        if run == 2:
            leaderboard()

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

'''
Cette fonction permet de propser au joueur les mouvement qui lui sont disponible
argument :
    - Liste contenant les direction possible
retourne :
    - le sens choisi par le joueur
'''

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

'''
Fonctoin qui affiche le leaderBoard 
argument :
    - rien 
retourne :
    - rien 

'''
def leaderboard():
    clear()
    background()
    posXY(20,11)
    print(Back.LIGHTBLUE_EX,Fore.BLACK,"▬▬▬▬▬ Labyrinthe Du Gladiateur ▬▬▬▬▬")
    posXY(30,13)
    print("-- Leaderboard --")
    ldb = recupLeaderboard()
    for l in range(len(ldb)//6):
        for h in range(6):
            posXY(25+l*13,15+h)
            print("|Lab%d : %s"%((6*l+h)+1,ldb[(6*l+h)] if ldb[(6*l+h)]!='999' else 'Vide'))
    posXY(22,23)
    print("Entrer pour retourner au menu principal")
    print(colorama.Style.RESET_ALL)
    input()



if __name__ == "__main__":
    print(menu())