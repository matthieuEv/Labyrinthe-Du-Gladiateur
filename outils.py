from PIL import Image
from numpy import*

from color import posXY

"""
Fonction pour gérer les entrées utilisateur
- prend en argument:
        possibillity = une liste avec toute les possibilités
        typeIn = le type attendu : "String" pour une str()
                                    "int" pour un int() -- par defaut 
        isPos = si il y a une position False -- par defaut 
        pos = position ou afficher [0,0] -- par defaut 
- Renvoie : la valeur attendu en int ou str 
    //ATTENTION on peut pas attendre "" ou -1//
"""
def user_input(possibillity,isPos=False,pos=[0,0]):
    #tant que l'on est pas sortie 
    while(1):
        try:
            if isPos :
                posXY(pos[0],pos[1])
                print("                    ",end='')
                posXY(pos[0],pos[1])
            print("--> ",end='')
            inp = int(input())
            #Si la réponse est au bon format et est dans la liste on la retourne
            if inp in possibillity :
                return(inp)
            else:
                pass
        except: 
            pass
"""
Fonction pour gérer les entrées utilisateur
- prend en argument:
        pos = position ou afficher [0,0] -- par defaut 
- Renvoie : la valeur attendu en str 
    //ATTENTION on peut pas attendre "" ou -1//
"""
def user_input_str(pos):
    while(1):
        posXY(pos[0],pos[1])
        print("                    ",end='')
        posXY(pos[0],pos[1])
        print("--> ",end='')
        inp = str(input())
        #Si la réponse est au bon format et est dans la liste on la retourne
        return(inp)


"""
Outils pour récupérer le labyrinthe a partir du fichier bitmap
arguments :
    - Le numéro du labyrinthe a charger sur un entier 
retourne :
    - Une liste a deux dim contenant les mur et passages du labyrinthe

"""
def recupLab(nb):
    temp=Image.open("labs/"+str(nb)+".bmp")
    # Crée une liste a partir de l'image, blanc=True et Noir==False
    arrayBmp = array(temp)
    #Nouvelle liste de la même taille que A
    arraylab=[[None for t in range(len(arrayBmp[i]))]for i in range(len(arrayBmp))]
    #Convertir les True en 1 et les False en 0
    #Peut-être ammener a changer 
    for i in range(len(arrayBmp)):
        for j in range(len(arrayBmp[i])):
            if arrayBmp[i][j]==True:
                arraylab[i][j]=1
            else:
                arraylab[i][j]=0
    #On retourne la nouvelle liste
    return(arraylab)

"""
Outils pour récupérer la position initiale du joueur et du gladiateur dans le lab:
argument : 
    - un entier avec le numéro du labyrinthe a charger 
retourne :
    - une liste a deux dimensions contenant les position X-Y du glad puis du joueur 
"""
def recup_pos_file(nb):
    #Ouvrir le fichier contenant les position
    file = open("labs/"+str(nb)+'.txt', 'r')
    #Crée une liste contenant les position separer du gald et du player
    lstPos = file.readlines()[0].split(',')
    #Crée une liste vide de deux fois deux
    posXY = [[None for i in range(2)] for t in range(2)]
    #balayer toute la liste juste crée
    for entity in range(len(posXY)):
        for pos in range(len(posXY[entity])):
            #Chaque valeur de la liste prend la valeur de position qui lui correspond et la mettre en int
            posXY[entity][pos]=int(lstPos[entity].split('-')[pos+1])
    #Retourner les bonne valeur pour chaque entité
    return(posXY)

"""
Outils pour le fichier save:
argument : 
    - le nom du fichier a lire 
retourne :
    - une liste avec le nom de la save et son emplacement
"""
def read_save_file(fichier):
    with open(fichier,"r") as file:
        f = file.read()
        lst = f.split(';')
        lst2 = []
        print(f.split(";"))
        for prof in lst:
            lst2.append(prof.split(','))
        for i in range(len(lst2)):
            lst2[i][1] = int(lst2[i][1])
        return(lst2)

if __name__ == "__main__":
    print(user_input_str([10,10]))