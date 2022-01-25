##Création d'un échiquier vide et coordonnées

def Creationechiquiervide():
    """ crée un echiquier vide"""
    echiquier=[[] for i in range(64)]
    return echiquier

def Coordinfotocoordechequiennes(i):
    """on donne le numéro d'une case de la matrice represenant l'echiquier et on renvoie une coordonnée de type a6"""
    if i>63 | i<0:
        return "Pas dans l'echiquier"
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
        return "Pas dans l'echiquier"
    return (ligne-1)*8+u



##deplacements elementaires sur l'echiquier
def avancerunecaseinfo(i):
    if i>55:
        return "sur la derniere rangee"
    else:
        return i+8

def avci(i):
    return avancerunecaseinfo(i)

def reculerunecaseinfo(i):
    if i<8:
        return "sur la premiere rangee"
    else:
        return i-8

def recci(i):
    return reculerunecaseinfo(i)

def unecasedroiteinfo(i):
    if i%8==7:
        return "sur la derniere colonne"
    else:
        return i+1

def drci(i):
    return unecasedroiteinfo(i)

def unecaseagaucheinfo(i):
    if i%8==0:
        return "sur la premiere colonne"
    else:
        return i-1

def gauci(i):
    return unecaseagaucheinfo(i)

def avancerunecaseechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=avancerunecaseinfo(i)
    if j=="sur la derniere rangee":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def avce(coords):
    return avancerunecaseechiq(coords)

def reculerunecaseechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=reculerunecaseinfo(i)
    if j=="sur la premiere rangee":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def recce(coords):
    return reculerunecaseechiq(coords)

def unecasedroiteechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=unecasedroiteinfo(i)
    if j=="sur la derniere colonne":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def drce(coords):
    return unecasedroiteechiq(coords)

def unecaseagaucheechiq(coords):
    i=Coordechequiennestocoordinfo(coords)
    j=unecaseagaucheinfo(i)
    if j=="sur la premiere colonne":
        return j
    else:
        return Coordinfotocoordechequiennes(j)

def gauce(coords):
    return unecaseagaucheechiq(coords)

## deplacement elementaire de pieces sur l'echiquier




