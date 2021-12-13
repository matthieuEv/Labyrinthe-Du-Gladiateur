'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from color import afficher_lab, clear_down,graph_deplacement_entite, graph_mort
from menu import menu, menu_joueur_jeu
from outils import addLab, newBest, recupLab,recup_pos_file, updatePos
from logique import check_mur, checkWin, checkmort, choix_dep_glad, deplacement_entite
from time import sleep

histoire=0
if __name__ == "__main__":
    #tant que le joueur ne choisi pas de sortir depuis le menu 
    while (True):
        if not(histoire):
            #Ouverture du menu et récupération du choi du joueur 
            nbLab,histoire = menu()

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
        find_de_jeu = False
        tour_Joueur = True
        #Nombre de tour fait par le joueur 
        nb_tour = 0
        while (not(find_de_jeu)):
            updatePos(posEntXY,histoire)
            if tour_Joueur:
                #TOUR DU JOUEUR 
                #Verification des mur autour du joueur
                dir_dispo = check_mur(lab,posEntXY[1])
                #Menu pour demander au joueur son mouvement
                sensJoueur = menu_joueur_jeu(dir_dispo)
                #Si le joueur a choisi 0 == Ne pas bouger
                if sensJoueur == 10:
                    histoire=0
                    find_de_jeu=True
                elif (sensJoueur!=0): 
                    #On stocke la nouvelle position dans une variable:
                    newPosPlayer = deplacement_entite(sensJoueur,posEntXY[1])
                    #déplacement visuel 
                    graph_deplacement_entite(lab,1,newPosPlayer,posEntXY[1])
                    #Update de la position réel 
                    posEntXY[1]=newPosPlayer
                tour_Joueur = False
                #On icremente le nombre de tour 
                nb_tour+=1
            else:
                #TOUR DU GLADIATEUR 
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
                tour_Joueur = True
    
            #Si je joueur est en dehors du labyrinthe c'est qu'il a gagner 
            if (checkWin(lab,posEntXY[1])):
                clear_down()
                #On update la variable pour pouvoir sortir de la partie
                find_de_jeu = True
                graph_mort(lab,posEntXY[1],True)
                print("Win")
                print(newBest(nbLab,nb_tour))
                if histoire:
                    addLab(histoire)
                    #si est pas en mode histoire on aura besoin du lab suivant
                    nbLab=(nbLab+1 if nbLab<12 else nbLab)
                input("Entre pour continuer")
            #Si le joueur a la même pos que le glad c'est qu'il est mort
            if checkmort(posEntXY):
                clear_down()
                find_de_jeu = True
                graph_mort(lab,posEntXY[1],False)
                print("Loose")  
                input("Entre pour continuer")
            #Fin de la Manche
        

    




