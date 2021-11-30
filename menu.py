from outils import user_input
from color import clear

def menu():
    while(1):
        clear()
        print("\n===== Labyrinthe Du Gladiateur =====\n")
        print("• Choisir le labyrinthe (1)")
        print("• Quitter le jeu (0)\n")
        #run = soit 0, soit 1, pas autre choses
        run=user_input([0,1])
        #si run = 0, on quitte tout
        if run == 0:
            exit()
        elif run == 1:
            clear()
            print("\n===== Labyrinthe Du Gladiateur =====\n")
            print("• Choisissez un labyrinthe entre 1 et 12")
            print("• Quitter le choix du labyrithe (0)\n")
            #choixLaby est compris entre 0 et 12
            choixLaby = user_input([0,1,2,3,4,5,6,7,8,9,10,11,12])
            if choixLaby != 0:
                return choixLaby
            #si choixLaby = 0, retour au menu de base


if __name__ == "__main__":
    print(menu())