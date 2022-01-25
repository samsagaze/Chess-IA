###

"""format typique d'une fonction traduite d'info à echiq :
def fonctionechiq(coords, autresvar):
    i=Coordechequiennestocoordinfo(coords)
    [j, autresvar]=fonctioninfo(i, autresvar)
    coordsbis=Coordinfotocoordechequiennes(j)
    return [coordsbis, autresvar]
"""


##Création d'un échiquier vide et coordonnées

def Creationechiquiervide():
    """ crée un echiquier vide"""
    echiquier=[[] for i in range(64)]
    return echiquier

def Coordinfotocoordechequiennes(i):
    """on donne le numéro d'une case de la matrice represenant l'echiquier et on renvoie une coordonnée de type a6"""
    if i>63 or i<0:
        return "Erreur"
    else:
        alphabet=["a", "b", "c", "d", "e", "f", "g", "h"]
        ligne=i//8+1
        colonne=alphabet[(i%8)]
        return [colonne, ligne]

def Coordechequiennestocoordinfo(coords):
    """fais la même chose dans le sens inverse"""
    [colonne, ligne]=coords
    alphabet=["a", "b", "c", "d", "e", "f", "g", "h"]
    u=-1
    for i in range(8):
        if alphabet[i]==colonne:
            u=i
    if u==-1:
        return "Erreur"
    return (ligne-1)*8+u


##description de l'echiquier

"""L'echiquier est representé sous la forme d'une matrice de tableau, donc les cases sont notées de gauche à droite de bas en haut (voir https://docs.google.com/document/d/1ZkEnX1gmuG94cVONLOJKTuy-SHUzwN2psN2XgxNzptE/edit)

Si la case est vide, alors le tableau est vide, sinon le tableau est un doublet dont le premier element correspond à la piece et le second à la couleur

Valeur des pieces :
    -Pion = "P"
    -Cavalier = "C"
    -Fou = "F"
    -Tour = "T"
    -Dame/Reine = "D"
    -Roi = "R"

Valeur des couleurs :
    - Blanc = "B"
    - Noir = "N"
"""


##deplacements elementaires sur l'echiquier
def avancerunecaseinfo(i):
    if i>55:
        return "Erreur"
    else:
        return i+8

"""renvoie la case devant i"""

def avci(i):
    return avancerunecaseinfo(i)


def reculerunecaseinfo(i):
    if i<8:
        return "Erreur"
    else:
        return i-8

"""renvoie la case derriere i"""

def recci(i):
    return reculerunecaseinfo(i)


def unecasedroiteinfo(i):
    if i%8==7:
        return "Erreur"
    else:
        return i+1

"""renvoie la case à droite de i"""

def drci(i):
    return unecasedroiteinfo(i)


def unecaseagaucheinfo(i):
    if i%8==0:
        return "Erreur"
    else:
        return i-1

"""renvoie la case à gauche de i"""

def gauci(i):
    return unecaseagaucheinfo(i)


def deplacementsendiagonaleavantgaucheinfo(i):
    if i%8==0 or i>55:
        return "Erreur"
    return i+7

"Renvoie la case en haut à gauche de i"

def davgi(i):
    return deplacementsendiagonaleavantgaucheinfo(i)


def deplacementsendiagonaleavantdroiteinfo(i):
    if i%8==7 or i>55:
        return "Erreur"
    return i+9

"Renvoie la case en haut à droite de i"

def davdi(i):
    return deplacementsendiagonaleavantdroiteinfo(i)


def deplacementsendiagonalearrieregaucheinfo(i):
    if i%8==0 or i<8:
        return "Erreur"
    return i-9

"Renvoie la case en bas à gauche de i"

def dargi(i):
    return deplacementsendiagonalearrieregaucheinfo(i)


def deplacementsendiagonalearrieredroiteinfo(i):
    if i%8==7 or i<8:
        return "Erreur"
    return i-7

"Renvoie la case en bas à droite de i"

def dardi(i):
    return deplacementsendiagonalearreiredroiteinfo(i)


def avancerunecaseechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=avancerunecaseinfo(i)
    if j=="Erreur":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def avce(coords):
    return avancerunecaseechiq(coords)


def reculerunecaseechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=reculerunecaseinfo(i)
    if j=="Erreur":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def recce(coords):
    return reculerunecaseechiq(coords)


def unecasedroiteechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=unecasedroiteinfo(i)
    if j=="Erreur":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def drce(coords):
    return unecasedroiteechiq(coords)


def unecaseagaucheechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=unecaseagaucheinfo(i)
    if j=="Erreur":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def gauce(coords):
    return unecaseagaucheechiq(coords)






## deplacement elementaire de pieces sur l'echiquier

def deplacerpieceinfo(i, j, echiquier):
    echiquier[j]=echiquier[i]
    echiquier[i]=[]
    return

"""met la pièce de la case i sur la case j"""

def deplacerpiecesdirectioninfo(direction, i, echiquier):
    if direction=="devant":
        j=avci(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
    elif direction=="derriere":
        j=recci(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
    elif direction=="gauche":
        j=gauci(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
    elif direction=="droite":
        j=drci(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
    return

"""Deplacer la piece à l'emplacement i dans la direction voulue :
directions possibles :
    -devant
    -derriere
    -gauche
    -droite
"""

def ddiri(direction, i, echiquier):
    if direction=="dev":
        directionbis="devant"
    elif direction=="der":
        directionbis="derriere"
    elif direction=="d":
        directionbis="droite"
    elif direction=="g":
        directionbis="gauche"
    else:
        directionbis=direction
    return deplacerpiecesdirectioninfo(directionbis, i, echiquier)

def deplacerpieceechiq(coordsi, coordsj, echiquier):
    i=Coordechequiennestocoordinfo(coordsi)
    j=Coordechequiennestocoordinfo(coordsj)
    deplacerpieceinfo(i, j, echiquier)
    return

def deplacerpiecesdirectionechiq(direction, coords, echiquier):
    i=Coordechequiennestocoordinfo(coords)
    deplacerpiecesdirectioninfo(direction, i, echiquier)
    return

def ddire(direction, coords, echiquier):
    i=Coordechequiennestocoordinfo(coords)
    ddiri(direction, i, echiquier)
    return

###deplacements de pièces





