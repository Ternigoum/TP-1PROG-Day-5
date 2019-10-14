#
from random import randint

#Fonction Cache couleur

def initCache(nbColors=6,nbPawns=4):

    return [randint(1,nbColors) for i in range(nbPawns)]         #Retourne un chiffre aléatoire entre 1 et 6 à chaque fois que 1 apparaît dans les pions

 

#Fonction pour choisir la couleur et les pions

def choose(nbColors=6,nbPawns=4):

    nocorrect = True

    while nocorrect:                             #tant que nocorrect est faux = proposition utilisateur

        nocorrect = False

        selected = input('Input your proposal: ')

        if len(selected) == nbPawns:             #si le nombre de la proposition = nbPawns, la proposition = x

            selected = [int(x) for x in range(selected)]

            for x in selected:                   #pour x dans proposition, si < à 1 ou > à nbColors, alors nocorrect = True

                if (x<1) or (x>nbColors):

                    nocorrect = True

        else:                                   #si le nombre proposition != nbPawns, nocorrect=True

            nocorrect = True

    return selected

 



def evaluation(selected,cache):                #définition de wellput et misplaced

    WellPut = 0

    Misplaced = 0

    copySelected,copyCache = list(selected),list(cache)

    for i in range(len(cache)):                    #pour le nombre de i dans len(cache) et le nombre de j, si copyslected et copycache sont =, Wellput gagne 1 ou Misplaced gagne 1
                                                   #en tous les cas, copyslected et copycache retournent à -1
        if copySelected[i] == copyCache[i]:                

            WellPut += 1

            copySelected[i],copyCache[i] = -1,-1

    for i in range(len(cache)):

     for j in range(len(cache)):

            if (copySelected[i] == copyCache[j]) and (copySelected[i] != -1):

                Misplaced += 1

                copySelected[i],copyCache[j] = -1,-1

    return WellPut,Misplaced

 
#définition affichage

def display(well,bad):

    print(well,"well spot and",bad,"bad ",'\n')

 

#définition affichage cache

def displayCache(cache):

    for x in cache:

        print(x,end='')

 

#défitnition paramètre jeux : nombre couleurs, longueur de séquence et nombre d'essais

def gameParameters():

    nbC = int(input('Input the number of colors: '))

    nbP = int(input(' Enter the length of the sequence to guess: '))

    nbTry = int(input(' Enter the number of trials: '))

    return nbC,nbP,nbTry

 



def master():              #définition win/lost

    nbC,nbP,nbTry = gameParameters()

    cache = initCache(nbC,nbP)

    notFound = True

    tries = 1

    print()

    while notFound and (tries<=nbTry):    #si l'utilisateur a gagné, plus d'essai possible, sinon tries +=1

        print('try',tries)

        well,bad = evaluation(choose(nbC,nbP),cache)

        display(well,bad)

        if well == nbP:

            notFound = False

        else:

            tries += 1

    if tries == nbTry+1:                 #si l'utilisateur a perdu, message d'erreur. S'il a gagné, message de win

        print("lost, we had to find:",end=' ')

        displayCache(cache)

    else:

        print("Congratulations, you have found well:", end=' ')

        displayCache(cache)
