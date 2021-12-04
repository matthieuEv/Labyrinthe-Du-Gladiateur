'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from color import afficher_lab,graph_deplacement_entite, posXY
from menu import menu
from outils import recupLab,recup_pos_file
from logique import check_mur, checkmort, choix_dep_glad, deplacement_entite
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
        for enti in range(2):
            graph_deplacement_entite(lab,enti,posEntXY[enti])

        #Debut de la partie 
        #Initialisation d'une variable pour savoir si on a gagné
        win = False
        while (not(win) and not(checkmort(posEntXY))):

            #TOUR DU JOUEUR 

            #Menu pour demander au joueur son mouvement
            dir_dispo = check_mur(lab,posEntXY[1])

            # //WIP// -> Doit sortir "sensJoueur" un entier entre 0 pas
            input()
            sensJoueur = 1
            #//WIP//
            
            #On stocke la nouvelle position dans une variable:
            newPosPlayer = deplacement_entite(sensJoueur,posEntXY[1])
            #déplacement visuel 
            graph_deplacement_entite(lab,1,newPosPlayer,posEntXY[1])
            #Update de la position réel 
            posEntXY[1]=newPosPlayer

            input()
            #TOUR DU GLADIATEUR 

            #Si je joueur est en dehors du labyrinthe c'est qu'il a gagner 
            if (posEntXY[1][0]>len(lab) or posEntXY[1][1]>len(lab[0])):
                win = True
            #ça signifie que je joueur est encore dans le lab et que le gladiateur doit bouger
            else:
                for i in range(2):
                    sleep(0.5)
                    #On met a jour la variable dir_dispo avec les valeurs pour le glad
                    dir_dispo = check_mur(lab,posEntXY[0])
                    #on regarde dans quel sens le glad doit aller
                    sens_glad = choix_dep_glad(dir_dispo,posEntXY)
                    #Si on décide de bouger
                    if (sens_glad):
                        #On stocke la nouvelle position dans une variable:
                        newPosGlad = deplacement_entite(sens_glad,posEntXY[0])
                        #déplacement visuel 
                        graph_deplacement_entite(lab,0,newPosGlad,posEntXY[0])
                        #Update de la position réel
                        posEntXY[0] = newPosGlad
            #Fin de la Manche

            #For now we just leave :
            input()
            exit("Fin provisoire")

    




