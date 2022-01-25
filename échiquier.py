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

def Citoe(i):
    return Coordinfotocoordechequiennes(i)

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

def Cetoi(coords):
    return Coordechequiennestocoordinfo(coords)

def casevideinfo(i, echiquier):
    if echiquier[i]==[]:
        return True
    else:
        return False

"""detecte si une case est vide"""

def casevideechiq(coords, echiquier):
    i=Cetoi(coords)
    return casevideinfo(i, echiquier)

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
    return deplacementsendiagonalearrieredroiteinfo(i)


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


def deplacementsendiagonaleavantgaucheechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=deplacementsendiagonaleavantgaucheinfo(i)
    if j=="Erreur":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def davge(coords):
    return deplacementsendiagonaleavantgaucheechiq(coords)


def deplacementsendiagonaleavantdroiteechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=deplacementsendiagonaleavantdroiteinfo(i)
    if j=="Erreur":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def davde(coords):
    return deplacementsendiagonaleavantdroiteechiq(coords)


def deplacementsendiagonalearrieregaucheechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=deplacementsendiagonalearrieregaucheinfo(i)
    if j=="Erreur":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def darge(coords):
    return deplacementsendiagonalearrieregaucheechiq(coords)


def deplacementsendiagonalearrieredroiteechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=deplacementsendiagonalearrieredroiteinfo(i)
    if j=="Erreur":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def darde(coords):
    return deplacementsendiagonalearrieredroiteechiq(coords)

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
        return
    elif direction=="derriere":
        j=recci(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
        return
    elif direction=="gauche":
        j=gauci(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
        return
    elif direction=="droite":
        j=drci(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
        return
    elif direction=="avant gauche":
        j=davgi(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
        return
    elif direction=="avant droite":
        j=davdi(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
        return
    elif direction=="arriere droite":
        j=dardi(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
        return
    elif direction=="arriere gauche":
        j=dargi(i)
        if type(j)!=type(0):
            return "Erreur"
        deplacerpieceinfo(i, j, echiquier)
        return
    else:
        return "Erreur"
    return

"""Deplacer la piece à l'emplacement i dans la direction voulue :
directions possibles :
    -devant
    -derriere
    -gauche
    -droite
    -avant gauche
    -avant droite
    -arriere droite
    -arriere gauche
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
    elif direction=="avg":
        directionbis="avant gauche"
    elif direction=="avd":
        directionbis="avant droite"
    elif direction=="arg":
        directionbis="arriere gauche"
    elif direction=="ard":
        directionbis="arriere droite"
    else:
        directionbis=direction
    return deplacerpiecesdirectioninfo(directionbis, i, echiquier)

"""rajoute les raccourcis :
    -dev = devant
    -der = derriere
    -g = gauche
    -d = droite
    -avg = avant gauche
    -avd = avant droite
    -ard = arriere droite
    -arg = arriere gauche
"""

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

def deplacementpioninfo(i, echiquier):
    tab=echiquier[i]
    dep=[]
    if tab==[]:
        return "Erreur"
    if len(tab)!=2:
        return "Erreur"
    [pieces, couleur]=tab
    if pieces!="P":
        return "Erreur"
    if couleur=="B":
        ja=avci(i)
        if echiquier[ja]==[]:
            dep+=[ja]
        jg=davgi(i)
        if len(jg)==2 and jg[1]=="N":
            dep+=[jg]
        jd=davdi(i)
        if len(jd)==2 and jd[1]=="N":
            dep+=[jd]
    elif couleur=="N":
        ja=recci(i)
        if echiquier[ja]==[]:
            dep+=[ja]
        jg=dargi(i)
        if len(jg)==2 and jg[1]=="B":
            dep+=[jg]
        jd=dardi(i)
        if len(jd)==2 and jd[1]=="B":
            dep+=[jd]
    else:
        return "Erreur"
    return dep

"""Le pion est la seule pièce dont le déplacement dépend de la couleur"""

def deplacementscavalierinfo(i, echiquier):
    dep=[]
    if

