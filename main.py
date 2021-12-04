'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from color import afficher_lab,graph_deplacement_entite, posXY
from menu import menu
from outils import recupLab,recup_pos_file
from logique import deplacement_entite


if __name__ == "__main__":
    #tant que le joueur ne choisi pas de sortir depuis le menu 
    while (True):
        #Ouverture du menu et récupération du choi du joueur 
        nbLab = menu()
                #Début du jeu 
        #Intialisation du Jeu
        #Initialisation des variable
        """
        lab est une liste a deux dim contenant les mur et case d'air du lab
        posXY est une liste a deux dimension contenant :
            - [0] la postiion du glad
            - [1] la position du player
        """
        lab = recupLab(nbLab)
        posXY = recup_pos_file(nbLab)
        print(posXY)
        #affichage du plateau
        afficher_lab(lab)
        for enti in range(2):
            graph_deplacement_entite(lab,enti,posXY[enti])

        #For now we just leave :
        input()
        exit("Fin provisoire")

    




