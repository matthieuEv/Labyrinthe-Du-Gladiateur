from PIL import Image
from numpy import*

"""
Outils pour récupérer le labyrinthe a partir du fichier bitmap
@params :
    - Le numéro du labyrinthe a charger sur un entier
@return :
    - Une liste a deux dim contenant les mur et passages du labyrinthe
@author Elouan
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
@param :
    - un entier avec le numéro du labyrinthe a charger
@return :
    - une liste a deux dimensions contenant les position X-Y du glad puis du joueur
@author Elouan
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
@param :
    - le nom du fichier a lire
@return :
    - 3 liste avec le labyrinthe en cours, la position en cours du gladiateur
      et la position en cours du joueur
@author Matthieu
"""
def read_save_file(fichier):
    with open(fichier,"r") as file:
        f = file.read()
        lst = f.split(';')
        lst2,lst3 = [],[]
        for prof in lst:
            lst2.append(prof.split('-'))
        for i in range(3):
            lst3.append(lst2[i][0].split(':'))
        currentLab = [lst3[0][1],lst3[1][1],lst3[2][1]]
        posLabGlad = [lst2[0][1],lst2[1][1],lst2[2][1]]
        posLabPlay = [lst2[0][2],lst2[1][2],lst2[2][2]]

        return currentLab,posLabGlad,posLabPlay

"""
@author Matthieu
"""
def testSaveExist(fichier,saveName):
    lst = read_save_file(fichier)
    for i in range(len(lst)):
        if (lst[i][0]).lower() == saveName.lower():
            return True
    return False

"""
@author Matthieu
"""
def write_save_file(fichier,listn):
    f = open(fichier, "w")
    f.write("S1:"+listn[0][0]+"-"+listn[1][0]+"-"+listn[2][0]+";"+"S2:"+listn[0][1]+"-"+listn[1][1]+"-"+listn[2][1]+";"+"S3:"+listn[0][2]+"-"+listn[1][2]+"-"+listn[2][2]+";")

"""
@author Matthieu
"""
def addLab(currentSave):
    profils = read_save_file("save")
    profils[0][currentSave-1]=str((int(profils[0][currentSave-1])+1))
    write_save_file("save",profils)


"""
Fonction qui permet de récupérer les meilleurs score:
@param :
    - rien 
@return :
    - une liste avec les meilleurs scores
@author Elouan
"""
def recupLeaderboard():
    return (open('leaderboard','r').readlines()[0].split(','))

"""
Fonction qui écrit le score si il est meilleur que l'ancien
@param: 
    - le numéro du lab
    - le Nombre de tour 
@return:
    - un texte si le score est un nouveau meilleur 
@author Elouan
"""
def newBest(nbLab,nbTour):
    #on récupère le leaderboard dans une liste 
    ldb = recupLeaderboard()
    #Si on a fait un nouveau meilleur score
    if (nbTour<int(ldb[nbLab-1])):
        #On met la valeur dans la liste
        ldb[nbLab-1]=str(nbTour)
        #On ouvre le fichier
        file = open('leaderboard','w')
        #On écrit la liste mis a jour dans le fichier
        for i in range(len(ldb)):
            file.write((","+ldb[i])if i!=0 else(ldb[i]))
        #On retourne un texte à afficher
        return("Nouveau meilleur !")
    else:
        #Si on as pas de record on renvoie un texte vide
        return('')
