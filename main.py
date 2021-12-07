'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from color import afficher_lab, clear_down,graph_deplacement_entite, graph_mort, posXY
from menu import menu, menu_joueur_jeu
from outils import recupLab,recup_pos_file
from logique import check_mur, checkWin, deplacement_entite
from time import sleep

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
        graph_deplacement_entite(lab,1,posEntXY[1])

        #Debut de la partie 
        #Initialisation d'une variable pour savoir si on a gagné
        find_de_jeu = False
        tour_Joueur = True
        while (not(find_de_jeu)):
            if tour_Joueur:
                #TOUR DU JOUEUR 
                #Verification des mur autour du joueur
                dir_dispo = check_mur(lab,posEntXY[1])
                #Menu pour demander au joueur son mouvement
                sensJoueur = menu_joueur_jeu(dir_dispo)
                #Si le joueur a choisi 0 == Ne pas bouger 
                if sensJoueur == 10:
                    break
                elif (sensJoueur!=0): 
                    #On stocke la nouvelle position dans une variable:
                    newPosPlayer = deplacement_entite(sensJoueur,posEntXY[1])
                    #déplacement visuel 
                    graph_deplacement_entite(lab,1,newPosPlayer,posEntXY[1])
                    #Update de la position réel 
                    posEntXY[1]=newPosPlayer
    
            #Si je joueur est en dehors du labyrinthe c'est qu'il a gagner 
            if (checkWin(lab,posEntXY[1])):
                clear_down()
                find_de_jeu = True
                graph_mort(lab,posEntXY[1],True)
                print("Win")
                input("Entre pour continuer")
            #Fin de la Manche                  
        #For now we just leave :
        

    




