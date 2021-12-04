from outils import user_input
from color import clear,posXY,init,clear_down
from colorama import Fore, Back

def menu():
    init()
    while(1):
        #clear()
        posXY(0,10)
        print(Fore.GREEN,"▬▬▬▬▬",Fore.RESET,Back.RESET,"Labyrinthe Du Gladiateur",Fore.GREEN,"▬▬▬▬▬",Fore.RESET,Back.RESET,"\n")
        print("• Choisir le labyrinthe ",Fore.BLACK,Back.RED,"(1)",Fore.RESET,Back.RESET,sep="")
        print("• Quitter le jeu ",Fore.BLACK,Back.RED,"(0)",Fore.RESET,Back.RESET,"\n",sep="")
        #run = soit 0, soit 1, pas autre choses
        run=user_input([0,1])
        #si run = 0, on quitte tout
        if run == 0:
            exit()
        elif run == 1:
            clear()
            posXY(0,10)
            print(Fore.GREEN,"▬▬▬▬▬",Fore.RESET,Back.RESET,"Labyrinthe Du Gladiateur",Fore.GREEN,"▬▬▬▬▬",Fore.RESET,Back.RESET,"\n")
            print("• Choisissez un labyrinthe entre ",Fore.BLACK,Back.RED,"1 et 12",Fore.RESET,Back.RESET,sep="")
            print("• Quitter le choix du labyrithe ",Fore.BLACK,Back.RED,"(0)",Fore.RESET,Back.RESET,"\n",sep="")
            #choixLaby est compris entre 0 et 12
            choixLaby = user_input([0,1,2,3,4,5,6,7,8,9,10,11,12])
            if choixLaby != 0:
                return choixLaby
            #si choixLaby = 0, retour au menu de base


def menu_joueur_jeu(dir_possible):
    nomDir = ["Est","Ouest","Nord","Sud"]
    possibility = [0]
    clear_down()
    posXY(0,31)
    print("Quel direction voulez vous ?")
    print("(0) - Ne pas bouger")
    for i in range(len(dir_possible)):
        if (dir_possible[i]):
            print("(%d) - %s"%(i+1,nomDir[i]))
            possibility.append(i+1)
    return(user_input(possibility))
    

if __name__ == "__main__":
    print(menu())