'''
Le labyrinthe du gladiateur :
@author Matthieu,Elouan
'''

from pygame.display import update
from color import afficher_lab, clear_down,graph_deplacement_entite, graph_mort
from menu import menu, menu_joueur_jeu
from outils import recupLab,recup_pos_file
from logique import check_mur, checkWin, checkmort, choix_dep_glad, deplacement_entite
from time import sleep
from pygameFile import closePygame, eventArrow, eventQuit, fondDecran, getEvent, pgAfficherLab, pgDeplacementEntite, pgGraphEndGame, pgInit, updateScreen

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
        ecran = pgInit()
        fondDecran(ecran)
        pgAfficherLab(ecran,lab)
        for enti in range(2):
            pgDeplacementEntite(ecran,lab,enti,posEntXY[enti])

        #Debut de la partie 
        #Initialisation d'une variable pour savoir si on a gagné
        fin_de_jeu = False
        tour_Joueur = True
        updateScreen()
        while (not(fin_de_jeu)):
            if tour_Joueur:
                #TOUR DU JOUEUR 
                #Verification des mur autour du joueur
                dir_dispo = check_mur(lab,posEntXY[1])
                #Menu pour demander au joueur son mouvement
                sensJoueur=-1
                while sensJoueur ==-1:
                    for event in getEvent():
                        sensJoueur = eventArrow(event,dir_dispo)
                    if sensJoueur!=10:
                        updateScreen()
                #Si le joueur a choisi 0 == Ne pas bouger
                if sensJoueur == 10:
                    fin_de_jeu=True
                elif (sensJoueur in [i for i in range(1,5)]): 
                    #On stocke la nouvelle position dans une variable:
                    newPosPlayer = deplacement_entite(sensJoueur,posEntXY[1])
                    #déplacement visuel 
                    pgDeplacementEntite(ecran,lab,1,newPosPlayer,posEntXY[1])
                    updateScreen()
                    #Update de la position réel 
                    posEntXY[1]=newPosPlayer
                tour_Joueur = False
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
                        pgDeplacementEntite(ecran,lab,0,newPosGlad,posEntXY[0])
                        updateScreen()
                        #Update de la position réel
                        posEntXY[0] = newPosGlad
                tour_Joueur = True
    
            #Si je joueur est en dehors du labyrinthe c'est qu'il a gagner 
            if (checkWin(lab,posEntXY[1])):
                #clear_down()
                fin_de_jeu = True
                #pgGraphEndGame(ecran,lab,posEntXY[1],True)
                print("Win")
                updateScreen
                input("Entre pour continuer")
                closePygame()
            elif checkmort(posEntXY):
                #clear_down()
                fin_de_jeu = True
                #pgGraphEndGame(ecran,lab,posEntXY[1],False)
                print("Loose")  
                updateScreen()
                input("Entre pour continuer")
                closePygame()
            elif not(fin_de_jeu):
                updateScreen()
            #Fin de la Manche                  
        #For now we just leave :
        

    




