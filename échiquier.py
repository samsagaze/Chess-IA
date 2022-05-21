###

"""format typique d'une fonction traduite d'info à echiq :
def fonctionechiq(coords, autresvar):
    i=Coordechequiennestocoordinfo(coords)
    [j, autresvar]=fonctioninfo(i, autresvar)
    coordsbis=Coordinfotocoordechequiennes(j)
    return [coordsbis, autresvar]

coords=[colonne, ligne], avec colonne type string et ligne type int
"""
"""Variables utiles : """

pieces = ["P", "C", "F", "T", "R", "D"]

##Création d'un échiquier vide et coordonnées

def Creationechiquiervide():
    """ crée un echiquier vide"""
    echiquier=[[] for i in range(64)]
    return echiquier

"""signature : null -> tableau"""

def Cev():
    return Creationechiquiervide()
"""alias de creationechiquiervide, même signature"""

def Coordinfotocoordechequiennes(i):
    """on donne le numéro d'une case de la matrice represenant l'echiquier et on renvoie une coordonnée de type a6"""
    if i>63 or i<0:
        return "Erreur"
    else:
        alphabet=["a", "b", "c", "d", "e", "f", "g", "h"]
        ligne=i//8+1
        colonne=alphabet[(i%8)]
        return [colonne, ligne]
"""signature : int -> [string, int]"""

def Citoe(i):
    return Coordinfotocoordechequiennes(i)
"""alias de coordinfotocoordechequiennes, même signature"""

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
"""signature : [string, int]-> int"""


def Cetoi(coords):
    return Coordechequiennestocoordinfo(coords)
"""alias de coordechequiennestocoordinfo, même signature"""

def casevideinfo(i, echiquier):
    if echiquier[i]==[]:
        return True
    else:
        return False

"""detecte si une case est vide
signature : [int, tableau]-> booleen"""

def casevideechiq(coords, echiquier):
    i=Cetoi(coords)
    return casevideinfo(i, echiquier)

def ajoutpiecei(x, c, i, echiquier):
    echiquier[i]=[x, c]
    return

"""ajoute la pièce x (type string) de la couleur c (type String) à l'emplacement i (type int) à l'échiquier"""

def ajoutpiecece(x, c, coords, echiquier):
    i=Cetoi(coords)
    ajoutpiecei(x, c, i ,echiquier)

def Creationechequierplein():
    echiquier=Creationechiquiervide()
    couleur="B"
    for i in range(8):
        echiquier[i+8]=["P", couleur]
    echiquier[0]=["T", couleur]
    echiquier[7]=["T", couleur]
    echiquier[1]=["C", couleur]
    echiquier[6]=["C", couleur]
    echiquier[2]=["F", couleur]
    echiquier[5]=["F", couleur]
    echiquier[3]=["D", couleur]
    echiquier[4]=["R", couleur]
    couleur="N"
    for i in range(8):
        echiquier[i+48]=["P", couleur]
    echiquier[56]=["T", couleur]
    echiquier[63]=["T", couleur]
    echiquier[57]=["C", couleur]
    echiquier[62]=["C", couleur]
    echiquier[58]=["F", couleur]
    echiquier[61]=["F", couleur]
    echiquier[59]=["D", couleur]
    echiquier[60]=["R", couleur]
    return echiquier

"""crée un echiquier avec les pièces de départ dessus
signature : null-> tableau"""

def victoire(echiquier):
    couleur=""
    for case in echiquier:
        if case!=[]:
            if couleur=="":
                couleur=case[1]
            else:
                if couleur!=case[1]:
                    return [False, ""]
    if couleur=="":
        return [False, ""]
    return [True, couleur]

"""si il y a un vainqueur dans la position donnée, alors victoire renvoie le doublet [True, couleur du vainqueur], sinon la fonction renvoie [False, ""]
signature : tableau -> [bool, String]"""

def identifiant(echiquier):
    id=0
    for i in range(64):
        case=echiquier[i]
        if case!=[]:
            for j in range(6):
                if case[0]==pieces[j]:
                    if case[1]=="B":
                        id+=j*(6**(2*i))
                    else:
                        id+=j*(6**(2*i+1))
    return id

def stringtotab(str):
    tab=[]
    for i in str:
        tab+=[i]
    tab[1]=int(tab[1])
    return tab

"""convertit un double de type "xn", avec x une lettre et n un chiffre, en tableau [x, n]"""


"""signature : tableau ->int
attribue un identifiant unique (demontrable facilement) à chaque position possible
essentielle pour le hash"""

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
"""toute les fonctions info auront pour signature :
int -> int
toutes les fonctions coordonnées echquiennes auront pour signature
coords -> coords"""


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
"""signature : int, int, tableau -> null"""

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
signature : string, int, tableau -> null
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
signature : string, int, tableau -> null
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

"""Les fonctions suivantes donnent les deplacements possibles d'une pièce à l'emplacement i en fonction de l'echiquier
Cependant rien ne dit qu'à la case i il se trouve bien ce type de pièce; si ce n'est pas le cas les fonctions vont souvent retourner erreur
signature des fonctions : int, tableau -> tableau"""

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
        if jg!="Erreur" and len(echiquier[jg])==2 and echiquier[jg][1]=="N":
            dep+=[jg]
        jd=davdi(i)
        if jd!="Erreur" and len(echiquier[jd])==2 and echiquier[jd][1]=="N":
            dep+=[jd]
    elif couleur=="N":
        ja=recci(i)
        if echiquier[ja]==[]:
            dep+=[ja]
        jg=dargi(i)
        if jg!="Erreur" and len(echiquier[jg])==2 and echiquier[jg][1]=="B":
            dep+=[jg]
        jd=dardi(i)
        if jd!="Erreur" and len(echiquier[jd])==2 and echiquier[jd][1]=="B":
            dep+=[jd]
    else:
        return "Erreur"
    return dep

"""Le pion est la seule pièce dont le déplacement dépend de la couleur"""

def deplacementscavalierinfo(i, echiquier):
    dep=[]
    if len(echiquier[i])!=2:
        return erreur
    couleur=echiquier[i][1]
    if i<48:
        if i%8!=7:
            c=echiquier[i+17]
            if c!=[]:
                if len(c)!=2:
                    return "Erreur"
                else:
                    if c[1]!=couleur:
                        dep+=[i+17]
            else:
                dep+=[i+17]
        if i%8!=0:
            c=echiquier[i+15]
            if c!=[]:
                if len(c)!=2:
                    return "Erreur"
                else:
                    if c[1]!=couleur:
                        dep+=[i+15]
            else:
                dep+=[i+15]
    if i>15:
        if i%8!=7:
            c=echiquier[i-15]
            if c!=[]:
                if len(c)!=2:
                    return "Erreur"
                else:
                    if c[1]!=couleur:
                        dep+=[i-15]
            else:
                dep+=[i-15]
        if i%8!=0:
            c=echiquier[i-17]
            if c!=[]:
                if len(c)!=2:
                    return "Erreur"
                else:
                    if c[1]!=couleur:
                        dep+=[i-17]
            else:
                dep+=[i-17]
    if i%8>1:
        if i<56:
            c=echiquier[i+6]
            if c!=[]:
                if len(c)!=2:
                    return "Erreur"
                else:
                    if c[1]!=couleur:
                        dep+=[i+6]
            else:
                dep+=[i+6]
        if i>7:
            c=echiquier[i-10]
            if c!=[]:
                if len(c)!=2:
                    return "Erreur"
                else:
                    if c[1]!=couleur:
                        dep+=[i-10]
            else:
                dep+=[i-10]
    if i%8<6:
        if i<56:
            c=echiquier[i+10]
            if c!=[]:
                if len(c)!=2:
                    return "Erreur"
                else:
                    if c[1]!=couleur:
                        dep+=[i+10]
            else:
                dep+=[i+10]
        if i>7:
            c=echiquier[i-6]
            if c!=[]:
                if len(c)!=2:
                    return "Erreur"
                else:
                    if c[1]!=couleur:
                        dep+=[i-6]
            else:
                dep+=[i-6]
    return dep

"""le cavalier se déplacant en L, il faut faire attention aux dépassements des bordures"""


def deplacementsfoudevantgaucheinfo(i, echiquier):
    dep=[]
    jhg=i
    couleur=echiquier[i][1]
    boolhg=True
    """deplacements en diagonal haut gauche"""
    while boolhg:
        jhg=davgi(jhg)
        if jhg=="Erreur":
            return dep
        casejhg=echiquier[jhg]
        if casejhg!=[]:
            if couleur==casejhg[1]:
                return dep
            else:
                return dep+[jhg]
        dep+=[jhg]
    return dep

def deplacementsfoudevantdroiteinfo(i, echiquier):
    dep=[]
    jhd=i
    couleur=echiquier[i][1]
    boolhd=True
    """deplacements en diagonal haut droite"""
    while boolhd:
        jhd=davdi(jhd)
        if jhd=="Erreur":
            return dep
        casejhd=echiquier[jhd]
        if casejhd!=[]:
            if couleur==casejhd[1]:
                return dep
            else:
                return dep+[jhd]
        dep+=[jhd]
    return dep


def deplacementsfouarrieredroiteinfo(i, echiquier):
    dep=[]
    jbd=i
    couleur=echiquier[i][1]
    boolbd=True
    """deplacements en diagonal bas droite"""
    while boolbd:
        jbd=dardi(jbd)
        if jbd=="Erreur":
            return dep
        casejbd=echiquier[jbd]
        if casejbd!=[]:
            if couleur==casejbd[1]:
                return dep
            else:
                return dep+[jbd]
        dep+=[jbd]
    return dep

def deplacementsfouarrieregaucheinfo(i, echiquier):
    dep=[]
    jbg=i
    couleur=echiquier[i][1]
    boolbg=True
    """deplacements en diagonal bas gauche"""
    while boolbg:
        jbg=dargi(jbg)
        if jbg=="Erreur":
            return dep
        casejbg=echiquier[jbg]
        if casejbg!=[]:
            if couleur==casejbg[1]:
                return dep
            else:
                return dep+[jbg]
        dep+=[jbg]
    return dep

def deplacementsfouinfo(i, echiquier):
    dep=[]
    depfad=deplacementsfouarrieredroiteinfo(i, echiquier)
    depfavd=deplacementsfoudevantdroiteinfo(i, echiquier)
    depfag=deplacementsfouarrieregaucheinfo(i, echiquier)
    depfavg=deplacementsfoudevantgaucheinfo(i, echiquier)
    if depfad=="Erreur":
        return "Erreur"
    if depfavd=="Erreur":
        return "Erreur"
    if depfag=="Erreur":
        return "Erreur"
    if depfavg=="Erreur":
        return "Erreur"
    dep+=depfad+depfavd+depfag+depfavg
    return dep

def deplacementstouravantinfo(i, echiquier):
    dep=[]
    jav=i
    couleur=echiquier[i][1]
    boolav=True
    """deplacements en avant"""
    while boolav:
        jav=avci(jav)
        if jav=="Erreur":
            return dep
        casejav=echiquier[jav]
        if casejav!=[]:
            if couleur==casejav[1]:
                return dep
            else:
                return dep+[jav]
        dep+=[jav]

def deplacementstourarriereinfo(i, echiquier):
    dep=[]
    jar=i
    couleur=echiquier[i][1]
    boolar=True
    """deplacements en arriere"""
    while boolar:
        jar=recci(jar)
        if jar=="Erreur":
            return dep
        casejar=echiquier[jar]
        if casejar!=[]:
            if couleur==casejar[1]:
                return dep
            else:
                return dep+[jar]
        dep+=[jar]

def deplacementstourdroiteinfo(i, echiquier):
    dep=[]
    jd=i
    couleur=echiquier[i][1]
    boold=True
    """deplacements à droite"""
    while boold:
        jd=drci(jd)
        if jd=="Erreur":
            return dep
        casejd=echiquier[jd]
        if casejd!=[]:
            if couleur==casejd[1]:
                return dep
            else:
                return dep+[jd]
        dep+=[jd]

def deplacementstourgaucheinfo(i, echiquier):
    dep=[]
    jg=i
    couleur=echiquier[i][1]
    boolg=True
    """deplacements à gauche"""
    while boolg:
        jg=gauci(jg)
        if jg=="Erreur":
            return dep
        casejg=echiquier[jg]
        if casejg!=[]:
            if couleur==casejg[1]:
                return dep
            else:
                return dep+[jg]
        dep+=[jg]

def deplacementstourinfo(i, echiquier):
    dep=[]
    deptav=deplacementstouravantinfo(i, echiquier)
    deptar=deplacementstourarriereinfo(i, echiquier)
    deptg=deplacementstourgaucheinfo(i, echiquier)
    deptd=deplacementstourdroiteinfo(i, echiquier)
    if deptav=="Erreur":
        return "Erreur"
    if deptar=="Erreur":
        return "Erreur"
    if deptg=="Erreur":
        return "Erreur"
    if deptd=="Erreur":
        return "Erreur"
    dep+=deptav+deptar+deptg+deptd
    return dep

def deplacementsdameinfo(i, echiquier):
    dep=[]
    dept=deplacementstourinfo(i, echiquier)
    depf=deplacementsfouinfo(i, echiquier)
    if dept=="Erreur" or depf=="Erreur":
        return "Erreur"
    dep+=dept+depf
    return dep

def deplacementsroiinfo(i, echiquier):
    av=avci(i)
    dep=[]
    roi=echiquier[i]
    if len(roi)!=2:
        return "Erreur"
    couleur=roi[1]
    if av!="Erreur":
        caseav=echiquier[av]
        if len(caseav)!=2:
           return "Erreur"
        if couleur==caseav[1]:
            dep+=[av]
    ar=recci(i)
    if ar!="Erreur":
        casear=echiquier[ar]
        if len(casear)!=2:
           return "Erreur"
        if couleur==casear[1]:
            dep+=[ar]
    g=gauci(i)
    if g!="Erreur":
        caseg=echiquier[g]
        if len(caseg)!=2:
           return "Erreur"
        if couleur==caseg[1]:
            dep+=[g]
    d=drci(i)
    if d!="Erreur":
        cased=echiquier[d]
        if len(cased)!=2:
           return "Erreur"
        if couleur==cased[1]:
            dep+=[d]
    ag=davgi(i)
    if ag!="Erreur":
        caseag=echiquier[ag]
        if len(caseag)!=2:
           return "Erreur"
        if couleur==caseag[1]:
            dep+=[ag]
    ad=davdi(i)
    if ad!="Erreur":
        casead=echiquier[ad]
        if len(casead)!=2:
           return "Erreur"
        if couleur==casead[1]:
            dep+=[ad]
    ard=dardi(i)
    if ard!="Erreur":
        caseard=echiquier[ard]
        if len(caseard)!=2:
           return "Erreur"
        if couleur==caseard[1]:
            dep+=[ard]
    arg=dargi(i)
    if arg!="Erreur":
        casearg=echiquier[arg]
        if len(casearg)!=2:
           return "Erreur"
        if couleur==casearg[1]:
            dep+=[arg]
    return dep


### Deplacements possibles



def deppossibles(echiquier, couleur):
    res=[]
    for i in range(64):
        case=echiquier[i]
        if len(case)==2 and case[1]==couleur:
            x=case[0]
            if x=="P":
                res+=[["P", i, deplacementpioninfo(i, echiquier)]]
            elif x=="C":
                res+=[["C", i, deplacementscavalierinfo(i, echiquier)]]
            elif x=="F":
                res+=[["F", i, deplacementsfouinfo(i, echiquier)]]
            elif x=="T":
                res+=[["T", i, deplacementstourinfo(i, echiquier)]]
            elif x=="R":
                res+=[["R", i, deplacementsroiinfo(i, echiquier)]]
            elif x=="D":
                res+=[["D", i, deplacementsdameinfo(i, echiquier)]]
    return res

"""à une position donnée, pour un joueur (défini par la couleur), donne tout les coups que ce joueur peut jouer
signature : tableau, string -> tableau"""



### évaluations de positions echecs gloutons
"""les fonctions suivantes servent à évaluer une position : un score positif (rec négatif) signifie un avantage pour blanc (rec noir). Plus le score est élevé en valeur absolue, plus l'avantage est conséquent
signature : tableau -> int"""
valpieces = [10, 29, 31, 50, 25,  120]

def evalpos1(echiquier):
    evaluation=0
    vic=victoire(echiquier)
    if vic[0]:
        if vic[1]=="B":
            return 10000
        else:
            return -10000
    for case in echiquier:
        if case!=[]:
            [piece, couleur]=case
            valpiece=0
            for i in range(6):
                if piece==pieces[i]:
                    valpiece=valpieces[i]
                    if couleur=="B":
                        evaluation+=valpiece
                    elif couleur=="N":
                        evaluation-=valpiece
                    else:
                        return "Erreur"
    return -evaluation

"""methode d'évaluation la plus basique, on somme la valeur des pièces
puisque la valeur maximale rendue par la fonction en valeur absolue est 120+8*10+25+2*29+2*31+2*50=445, on peut considerer que 10000 correspond à une valeur inifinie"""


"""
### arbre de jeu

création de l'arbre de jeu

def arbredejeu(profondeur, e, couleur):
    return
"""


### algorithme min max

"""afin de jouer les coups, on copie l'echiquier, neamoins ce dernier etant un tableau de tableau nous avons besoin de la fonction deepcopy du module copy"""

from copy import deepcopy




def minimax(profondeur, echiquier, couleur, dico):
    identite=identifiant(echiquier)
    string=str(identite)
    bool=string in dico
    if bool:
        [valeur, profondeurb]=dico[string]
        if profondeur==0:
            return [valeur, profondeurb]
        if abs(valeur)==10000:
            return [valeur, profondeurb]
    if not bool and (profondeur==0 or victoire(echiquier)[0]):             #remarque : ce cas sera très rare, puisqu'a priori on a déjà evalué la position dans dico au coup précedent
        evalpos=evalpos1(echiquier)
        dico[string]=[evalpos, 0]
        return [evalpos, 0]
    if couleur=="N":
        valeur=-10000
        coup=[-1, -1]
        couppos=deppossibles(echiquier, couleur)
        for coups in couppos:
            caseoriginelle=coups[1]
            couppospiece=coups[2]
            for j in couppospiece:
                echiquierbis=deepcopy(echiquier)
                if type(caseoriginelle)!=type(4) or type(j)!=type(4):
                    return caseoriginelle, j
                deplacerpieceinfo(caseoriginelle, j, echiquierbis)
                minmaxj=minimax(profondeur-1, echiquierbis, "B", dico)
                valeurbis=minmaxj[0]
                if type(valeurbis)!=type(0):
                    return 0,echiquierbis
                if valeurbis>valeur:
                    valeur=valeurbis
                    coup=[caseoriginelle, j]
            dico[string]=[valeur, profondeur]
        return [valeur, coup]
    else:
        valeur=10000
        coup=[-1, -1]
        couppos=deppossibles(echiquier, couleur)
        for coups in couppos:
            caseoriginelle=coups[1]
            couppospiece=coups[2]
            for j in couppospiece:
                echiquierbis=deepcopy(echiquier)
                if type(caseoriginelle)!=type(4) or type(j)!=type(4):
                    return caseoriginelle, j
                deplacerpieceinfo(caseoriginelle, j, echiquierbis)
                minmaxj=minimax(profondeur-1, echiquierbis, "N", dico)
                valeurbis=minmaxj[0]
                if type(valeurbis)!=type(0):
                    return 1,echiquierbis
                if valeurbis<valeur:
                    valeur=valeurbis
                    coup=[caseoriginelle, j]
            dico[string]=[valeur, profondeur]
        return [valeur, coup]
    return
#remarque : erreur d'indentation probable, considerer le cas ou on est dejà dans le dictionnaire



"""signature : int, tableau, string, dictionnaire -> [int, *[int, int]]
remarque : dans le cas où coup=[-1, -1], alors aucun coup n'est joué
problème à corriger dans le code"""


### Suite du projet

"""On attaque maintenat la partie du problème où on regarde le jeu d'échecs classique"""

#def echecs(echiquier, couleur):
#    return bool

"""vérifie si le roi de la couleur mentionnee est en échec dans la position atteinte"""

def mat(couleur):
    return bool

"""vérifie si un joueur à gagner"""


def coupspossbis(echiquier):
    return res

"""même fonction que celle déjà vue, mais en prenant en compte les regles particulieres (le roi ne peut pas être en echec par exemple, mais aussi double deplacement du pion, roque - on rajoutera des booleens en fin d'echiquier si le roque est possible, prise en passant et promotion)"""

def elaguagealphabeta(profondeur, echiquier, couleur, dico):
    return value

"""même principe que la fonction minimax mais amelioré"""

def evalpos2(echiquier):
    return value

"""fonction permettant d'évaluer une position
fonction la plus importante dans cette partie, plusieurs versions seront regardées
première version très similaire à evalpos2 (la valeur renvoyée ne sera pas inversée, et le roi n'aura pas de valeur - ne pas en avoir signifie avoir perdue
version plus avancée ou chaque pièce aura une valeure différente en fonction de la case sur laquelle elle est"""

def jouer(couleur):
    while True:
        input(coup)
        """...
        """
    return

"""fonction permettant au joueur de jouer contre l'IA
prise en compte de la règle des 50 coups (si 50 coups joué sans deplacements de pion ou piece prise alors partie nulle"""


###echiquier amelioré

"""Afin de prendre en compte les nouvelles règles, à l'echiquier de base on rajoute qques informations pour former un tableau, appelé echbis dans les fonctions qui suivent, contenant :
echbis = [echiquier, boolrb, boolrn, booltb1, booltb2, booltn1, bootn2, boolb0, ..., boolb8, booln1, ..., booln8, compteur], servant à
boolrb, boolrn verifient si le roi n'a pas bouger, booltx verifiant si les tours n'ont pas bougé (afin d'autoriser le roque), boolb1-8 et booln1-8 disent si les pions ont avancé de deux cases (afin de permettre la prise en passant) et le compteur permet de vérifier la règle des 50 coups"""

def Creationsechibisplein():
    echiquier=Creationechequierplein()
    echbis=[echiquier, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,0]
    return echbis

"""crée un echbis complet"""


### Regles ameliorées

def trouverroi(echiquier, couleur):
    for i in range(64):
        case=echiquier[i]
        if case==["R", couleur]:
                return i
    return "Erreur"

"""trouve le roi de la couleur correspondante sur l'echiquier et renvoie sur quelle case il se trouve"""

def menacecase(deposs, i):
    for deppiece in deposs:
        for j in deposs[2]:
            if i==j:
                return True
    return False

"""deposs est le resultat de la fonction depposibles, la fonction menace case vérifie si le joueur adverse peut menacer la case correspondante (utile dans le cas du roque et de la verification des echecs"""

def couleuropp(couleur):
    if couleur=="B":
        return "N"
    else:
        return "B"

"""renvoie la couleur opposée"""


def echecs(couleur, echbis):
    echiquier=echbis[0]
    couleurop=couleuropp(couleur)
    dep=deppossibles(echiquier, couleurop)
    i=trouverroi(echiquier, couleur)
    for deppiece in dep:
        for j in deppiece[2]:
            if i==j:
                return True
    return False

"""renvoie True si le roi est en echecs"""

def roq(couleur, echbis, touri):
    echiquier=echbis[0]
    """touri correspond à la case de la tour qu'on veut faire roquer"""
    dep=deppossibles(echiquier, couleuropp(couleur))
    if touri==0:
        if echbis[1] and echbis[3]:
            if menacecase(dep, 2) or menacecase(dep, 3):
                return False
            else:
                return True
    if touri==7:
        if echbis[1] and echbis[4]:
            if menacecase(dep, 5) or menacecase(dep, 6):
                return False
            else:
                return True
    if touri==56:
        if echbis[2] and echbis[5]:
            if menacecase(dep, 58) or menacecase(dep, 59):
                return False
            else:
                return True
    if touri==63:
        if echbis[2] and echbis[6]:
            if menacecase(dep, 62) or menacecase(dep, 61):
                return False
            else:
                return True

"""dit si le roi de la couleur peut roquer avec la tour sur la case touri"""

def peutroquer(couleur, echbis):
    rep=[]
    if couleur=="B":
        if roq(couleur, echbis, 0):
            rep+=[0]
        if roq(couleur, echbis, 7):
            rep+=[7]
    rep=[]
    if couleur=="N":
        if roq(couleur, echbis, 56):
            rep+=[56]
        if roq(couleur, echbis, 63):
            rep+=[63]
    return rep

"""renvoie avec quelle tour le roi peut se déplacer"""

def prepriseenpassant(i, j, couleur, echbis):
    jbis=j//8
    if couleur=="N":
        if i//8==3:
            if echbis[6 + jbis]:
                return True
            else:
                return False
    else:
        if i//8==4:
            if echbis[14 +jbis]:
                return True
            else:
                return False
    return False

"""teste si le pion en i peut prendre en passant en j"""

def priseenpassant(i, couleur, echbis):
    ibis=i%2
    rep=[]
    if couleur=="N" and i//8==3:
        if ibis!=0:
            j1=15+ibis
            if prepriseenpassant(i, j1, couleur, echbis):
                rep+=[j1]
        if ibis!=7:
            j2=17+ibis
            if prepriseenpassant(i, j2, couleur, echbis):
                rep+=[j2]
    if couleur=="B" and i//8==4:
        if ibis!=0:
            j1=39+ibis
            if prepriseenpassant(i, j1, couleur, echbis):
                rep+=[j1]
        if ibis!=7:
            j2=41+ibis
            if prepriseenpassant(i, j2, couleur, echbis):
                rep+=[j2]
    return rep

"""teste si le pion en i peut prendre en passant qqpart, renvoie ou il peut prendre"""

def priseenpassant1(i, echbis):
    echiquier=echbis[0]
    case=echiquier[i]
    couleur=case[1]
    return priseenpassant(i, couleur, echbis)

def deplacementameliore(echbis, couleur):
    echiquier=echbis[0]
    res=[]
    for i in range(64):
        case=echiquier[i]
        if len(case)==2 and case[1]==couleur:
            x=case[0]
            if x=="P":
                deppion=deplacementpioninfo(i, echiquier)
                deppion+=priseenpassant1(i, echbis)
                if couleur=="B" and i//8==1:
                    if echiquier[i+8]==[] and echiquier[i+16]==[]:
                        deppion+=[i+16]
                if couleur=="N" and i//8==6:
                    if echiquier[i-8]==[] and echiquier[i-16]==[]:
                        deppion+=[i-16]
                res+=[["P", i, deppion]]
            elif x=="C":
                res+=[["C", i, deplacementscavalierinfo(i, echiquier)]]
            elif x=="F":
                res+=[["F", i, deplacementsfouinfo(i, echiquier)]]
            elif x=="T":
                res+=[["T", i, deplacementstourinfo(i, echiquier)]]
            elif x=="R":
                deproi=deplacementsroiinfo(i, echiquier)
                if deproi=="Erreur":
                    deproi=[]
                deproi+=peutroquer(couleur, echbis)
                res+=[["R", i, deproi]]
            elif x=="D":
                res+=[["D", i, deplacementsdameinfo(i, echiquier)]]
    return res

"""renvoie un tableau de type [deplacementspiece1, deplacementspiece2...] où deplacementspiece est un tableau de la forme [type de la piece, emplacement de la piece, [tableau des endroits ou la piece peut aller]"""

def verificationcouproq(piece, i, j, couleur):
    if piece=="R":
        if abs(j-i)==2:
            if couleur=="B":
                if j=="0":
                    return [3, 0]
                if j=="7":
                    return [5, 7]
            if couleur==[N]:
                if j==63:
                    return [61, 63]
                if j==56:
                    return [59, 56]
    return False

""" Verifie si le coup est un roque ou non, et si oui renvoie les cases d'arrivée puis de depart de la tour"""

def jouercoupinfo(i, j, echbis):
    [piece, couleur]=echbis[0][i]
    if verificationcouproq(piece, i, j, couleur)!=False:
        [itarr, itdep]=verificationcouproq(piece, i, j, couleur)
        echbis[0][itarr]=echbis[0][itdep]
        echbis[0][itdep]=[]
    echbis[0][j]=echbis[0][i]
    echbis[0][i]=[]
    if piece=="P":
        if couleur=="B":
            if j//8==7:
                piecebis=input("Promotion en quelle pièce ?")
                echbis[0][j]=[piecebis, couleur]
            else:
                if abs(i-j)==16:
                    echbis[7+i%8]=True
                if i//8==4 and echbis[j%8+15]:
                    echbis[0][j-8]=[]
        else:
            if j//8==0:
                piecebis=input("Promotion en quelle pièce ?")
                echbis[0][j]=[piecebis, couleur]
            else:
                if abs(i-j)==16:
                    echbis[15+i%8]=True
                if i//8==3 and echbis[j%8+7]:
                    echbis[0][j+8]=[]

    return

"""permet de jouer un coup sur l'echiquier"""

def jouercoupechiq(coordi, coordj, echbis):
    i=Coordechequiennestocoordinfo(coordi)
    j=Coordechequiennestocoordinfo(j)
    jouercoupinfo(i, j, echbis)
    return

"""meme fonction, mais en coordonnées echiqueenes"""

def mat(echbis, couleur):
    echiquier=echbis[0]
    bool=echecs(couleur, echbis)
    if bool==False:
        return False
    dep=deplacementameliore(echbis, couleur)
    for deppiece in dep:
        for j in deppiece[2]:
            echbissec=deepcopy(echbis)
            if not echecs(couleur, echbissec):
                return False
    return True

"""verifie si le joueur de la couleur est en echecs et mat"""

def pat(echbis, couleur):
    if echecs(couleur, echbis):
        return False
    dep=deplacementameliore(echbis, couleur)
    for deppiece in dep:
        for j in deppiece[2]:
            echbissec=deepcopy(echbis)
            if not echecs(couleur, echbissec):
                return False
    return True

"""vérifie si le joueur de la couleur est en pat"""

def couplégal(i, j, echbis, couleur):
    dep=deplacementameliore(echbis, couleur)
    for deppiece in dep:
        if deppiece[1]==i:
            for arr in deppiece[2]:
                if arr==j:
                    echbistier=deepcopy(echbis)
                    jouercoupinfo(i, j, echbistier)
                    if echecs(couleur, echbistier):
                        return False
                    else:
                        return True
    return False




def jouerhumvshum():
    echbis=Creationsechibisplein()
    couleur="B"
    while True:
        if echbis[22]==50:
            return "Partie nulle"
        coorddep=input("Quelle pièce voulez vous déplacer - mettez un doublet sous la forme de xn ou x est un string et n un chiffre")
        coorddep=stringtotab(coorddep)
        coordarr=input("Où voulez vous déplacer - mettez un doublet sous la forme de xn ou x est un string et n un chiffre")
        coordarr=stringtotab(coordarr)
        i=Coordechequiennestocoordinfo(coorddep)
        j=Coordechequiennestocoordinfo(coordarr)
        bool=couplégal(i, j, echbis, couleur)
        while not bool:
            print("Coup non légal")
            coorddep=stringtotab(input("Quelle pièce voulez vous déplacer - mettez un tableau de la forme [x, n] ou x est un string et n un chiffre"))
            coordarr=stringtotab(input("Où voulez vous déplacer - mettez un tableau de la forme [x, n] ou x est un string et n un chiffre"))
            i=Coordechequiennestocoordinfo(coorddep)
            j=Coordechequiennestocoordinfo(coordarr)
            bool=couplégal(i, j, echbis, couleur)
        if echbis[0][i][1]!="P" and echbis[0][j]==[]:
            echbis[22]+=1

        else:
            echbis[22]=0
        jouercoupinfo(i, j, echbis)
        couleur=couleuropp(couleur)
        print(echbis[0])
        if couleur=="B":
            for k in range(8):
                echbis[15+k]=True
        else:
            for k in range(8):
                echbis[7+k]=True
        if mat(echbis, couleur):
            if couleur=="B":
                return "Victoire des noirs"
            else:
                return "Victoire des blancs"
        else:
            if pat(echbis, couleur):
                return "Partie nulle"



"""Remarque : pour déplacer une pièce on rentre d'abord ses coordonnées de départ puis ses coordonnées d'arrivée"""






