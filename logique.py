'''
Fichier contenant les fonctions qui servirons a la logique et au déroulement du jeu
'''

'''
Fonction permettant d'éffectuer un déplacement d'une entité
//La vérification de si le déplacement est possible doit être fait avant//
Arguments : 
    - Le choix du sens de déplacement int()
    - La liste à 2 dim avec la position du joueur :
            - [0] = position sur X 
            - [1] = position sur y
retourne :
    - la liste à 2 dim de la position du joueur mis à jour
'''

def deplacement_entite(sens,poXY):
    new_pos = [None for i in range (2)]
    if (sens == 1 ):
        new_pos[0] = poXY[0]+2
    elif(sens == 2):
        new_pos[0] = poXY[0]-2
    elif(sens == 3):
        new_pos[1] = poXY[1]+2
    else:
        new_pos[1] = poXY[1]-2
    return(new_pos)

"""
Fonction de test de mort du joueur 
arguments : 
    - liste a Deux dim contenant les position du glad et du joueur 
retourne :
    - True si le joueur et le glad sont sur la même case sinon False
"""
def checkmort (posEntiteXY):
    return((posEntiteXY[0][0]==posEntiteXY[1][0]) and (posEntiteXY[0][1]==posEntiteXY[1][1]))