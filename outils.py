from PIL import Image
from numpy import*

"""
Fonction pour gérer les entrées utilisateur
- prend en argument:
        typeIn = le type attendu : "String" pour une str()
                                    "int" pour un int()
        possibillity = une liste avec toute les possibilités
- Renvoie : la valeur attendu en int ou str 
    //ATTENTION on peut pas attendre "" ou -1//
"""
def user_input(possibillity,typeIn="int"):
    #Crée la variable de récepetion en fonction des besoin
    inp = "" if typeIn == "string" else (-1)
    #tant que l'on est pas sortie 
    while(1):
        #Si on attend une str
        if (typeIn == "string") : 
            try:
                inp = str(input("--> "))
                #Si la réponse est au bon format et est dans la liste on la retourne
                if inp in possibillity :
                    return(inp)
                else:
                    pass
            except: 
                pass
        #Sinon on est dans int
        else:
            try:
                inp = int(input("--> "))
                #Si la réponse est au bon format et est dans la liste on la retourne
                if inp in possibillity :
                    return(inp)
                else:
                    pass
            except: 
                pass


"""
Outils pour récupérer le labyrinthe a partir du fichier bitmap

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
                arraylab[i][j]=0
            else:
                arraylab[i][j]=1
    #On retourne la nouvelle liste
    return(arraylab)