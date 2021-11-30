"""
Fonction pour gérer les entrées utilisateur
- prend en argument:
        le type attendu : "String" pour une str()
                          "int" pour un int()
        une liste avec toute les possibilités
- Renvoie : la valeur attendu en int ou str 
    //ATTENTION on peut pas attendre "" ou -1//
"""
def user_input(typeIn,possibillity):
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
                print("valeur incorect")
