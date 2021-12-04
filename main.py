'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from color import afficher_lab
from menu import menu
from outils import recupLab

if __name__ == "__main__":
    #tant que le joueur ne choisi pas de sortir depuis le menu 
    while (True):
        #Ouverture du menu et récupération du choi du joueur 
        nbLab = menu()
        #Début du jeu 
        #Intialisation du Jeu
        #Initialisation des variable:
        gladXY = [None for i in range(2)]
        playerXY = [None for i in range(2)]
        lab = recupLab(nbLab)
        #affichage du plateau
        afficher_lab(lab)
    
    




