'''
Fichier contenant les fonctions qui servirons a la logique et au déroulement du jeu
'''

'''
Fonction permettant d'éffectuer un déplacement d'une entité
//La vérification de si le déplacement est possible doit être fait avant//
Arguments : 
    - Le choix du sens de déplacement int()
        - 0 = ne bouge pas 
        - 1 = est 
        - 2 = Ouest
        - 3 = Nord
        - 3 = sud
    - La liste à 2 dim avec la position du joueur :
            - [0] = position sur X 
            - [1] = position sur y
retourne :
    - la liste à contenant la position du joueur mis à jour
'''
def deplacement_entite(sens,poXY):
    #On gère le cas de chaque sens 
    new_pos = [poXY[i]for i in range(len(poXY))]
    if (sens == 1 ):
        new_pos[0] = poXY[0]+2
    elif(sens == 2):
        new_pos[0] = poXY[0]-2
    elif(sens == 3):
        new_pos[1] = poXY[1]-2
    else:
        new_pos[1] = poXY[1]+2
    return(new_pos)

"""
Fonction de test victoire du joueur 
arguments : 
    - liste a Deux dim contenant le labyrinthe
    - une liste contenant la position du joueur
retourne :
    - True si le joueur et le glad sont sur la même case sinon False
"""
def checkWin (tabLab,posXY):
    return(posXY[0]>=len(tabLab[0]) or posXY[1]>=len(tabLab) or posXY[0]<=0 or posXY[1]<=0)

'''
Fonction qui vérifie la présence de mur 
argument :
    - liste a deux dim contenant le labyrinthe 
    - liste XY contenant la position de l'entite a tester
retourne :
    - liste des sens de deplacemnt possible True and False
        - [0] = est 
        - [1] = Ouest
        - [2] = Nord
        - [3] = sud 
'''
def check_mur (tabLab,posEnti):
    #On crée la variable de reception 
    sens_dispo = [False for i in range(4)]
    #On vériie un par un chaque cas 
    if not(tabLab[posEnti[1]][posEnti[0]+1]):
        sens_dispo[0] = True
    if not(tabLab[posEnti[1]][posEnti[0]-1]):
        sens_dispo[1] = True
    if not(tabLab[posEnti[1]-1][posEnti[0]]):
        sens_dispo[2] = True
    if not(tabLab[posEnti[1]+1][posEnti[0]]):
        sens_dispo[3] = True
    return(sens_dispo)