'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from color import afficher_lab
from menu import menu
from outils import recupLab

if __name__ == "__main__":
    #Début du jeu 
    #Ouverture du menu
    nbLab = menu()
    lab = recupLab(nbLab)
    afficher_lab(lab)


