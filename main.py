'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from color import afficher_lab,graph_deplacement_entite, posXY
from menu import menu
from outils import recupLab,recup_pos_file
from logique import check_mur, checkmort, deplacement_entite


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
        posEntXY est une liste a deux dimension contenant :
            - [0] la postiion du glad
            - [1] la position du player
        """
        lab = recupLab(nbLab)
        posEntXY = recup_pos_file(nbLab)
        #affichage du plateau
        afficher_lab(lab)
        for enti in range(2):
            graph_deplacement_entite(lab,enti,posEntXY[enti])

        #Debut de la partie 
        #Initialisation d'une variable pour savoir si on a gagné
        win = False
        while (not(win) and not(checkmort(posEntXY))):

            #Menu pour demander au joueur son mouvement
            dir_dispo = check_mur(lab,posEntXY[1])
            # //WIP// -> Doit sortir "sensJoueur"
            input()
            sensJoueur = 1
            #//WIP//
            
            #On stocke la nouvelle position dans une variable:
            newPosPlayer = deplacement_entite(sensJoueur,posEntXY[1])
            #déplacement visuel 
            graph_deplacement_entite(lab,1,newPosPlayer,posEntXY[1])
            #Update de la position réel 
            posEntXY[1]=newPosPlayer
            if (posEntXY[1][0]>len(lab) or posEntXY[1][1]>len(lab[0])):
                win = True
                break
            




            #For now we just leave :
            input()
            exit("Fin provisoire")

    




