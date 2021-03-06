'''
Fichier contenant les fonctions qui servirons a la logique et au déroulement du jeu
'''

'''
Fonction permettant d'éffectuer un déplacement d'une entité
//La vérification de si le déplacement est possible doit être fait avant//
@params : 
    - Le choix du sens de déplacement int()
        - 0 = ne bouge pas 
        - 1 = est 
        - 2 = Ouest
        - 3 = Nord
        - 3 = sud
    - La liste à 2 dim avec la position du joueur :
            - [0] = position sur X 
            - [1] = position sur y
@return :
    - la liste à contenant la position du joueur mis à jour
@author Elouan
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
Fonction de test de mort du joueur 
@params : 
    - liste a Deux dim contenant les position du glad et du joueur 
@return :
    - True si le joueur et le glad sont sur la même case sinon False
@author Elouan
"""
def checkmort (posEntiteXY):
    return((posEntiteXY[0][0]==posEntiteXY[1][0]) and (posEntiteXY[0][1]==posEntiteXY[1][1]))
"""
Fonction de test de mort du joueur 
@params : 
    - liste a Deux dim contenant le labyrinthe
    - une liste contenant la position du joueur
@return :
    - True si le joueur et le glad sont sur la même case sinon False
@author Elouan
"""
def checkWin (tabLab,posXY):
    return(posXY[0]>=len(tabLab[0]) or posXY[1]>=len(tabLab) or posXY[0]<=0 or posXY[1]<=0)

'''
Fonction qui vérifie la présence de mur 
@param :
    - liste a deux dim contenant le labyrinthe 
    - liste XY contenant la position de l'entite a tester
@return :
    - liste des sens de deplacemnt possible True and False
        - [0] = est 
        - [1] = Ouest
        - [2] = Nord
        - [3] = sud 
@author Elouan
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

'''
Fonction de choix de direction pour le glad
@param : 
    - liste de taille 4 avec les déplacement possible
    - liste deux dim avec les position du glad [0] et du joueur [1]
@return :
    - un entier avec la direction que doit prendre le glad 
        - 0 = ne bouge pas 
        - 1 = est 
        - 2 = Ouest
        - 3 = Nord
        - 4 = sud
@author Elouan
'''
def choix_dep_glad(dir_possible,posEntiXY):
    #On crée une variable pour le sens a renvoyer 
    sens = 0
    #et un compteur 
    cpt = 0
    #On vérifie d'abord selon Est-Ouest puis Nord-Sud
    while (cpt<2 and not(sens)):
        #si il est plus a 1 - est 2- nord on idique le sens qui va avec 
        if (posEntiXY[1][cpt]>posEntiXY[0][cpt] and dir_possible[cpt*3]):
            sens = 1+(cpt*3)
        #Sinon si l'autre coté 
        elif(posEntiXY[1][cpt]<posEntiXY[0][cpt] and dir_possible[1+(cpt*1)]):
            sens = 2 +(cpt*1) 
        cpt+=1
    #Si il est ni l'un ni l'autre on ne bouge pas
    return(sens)