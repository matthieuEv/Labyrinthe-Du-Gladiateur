'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from color import afficher_lab
from menu import menu
from outils import recupLab

if __name__ == "__main__":
    #Début du jeu 
    #Intialisation du Jeu
    #Initialisation des variable:
    gladXY = [None for i in range(2)]
    playerXY = [None for i in range(2)]
    #Ouverture du menu
    nbLab = menu()
    lab = recupLab(nbLab)
    afficher_lab(lab)
    
    




