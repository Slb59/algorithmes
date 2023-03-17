class Noeud:
    def __init__(self, valeur:int, gauche=None, droite=None) -> None:
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite

    def __str__(self):
        if self.valeur is None:
            return ''
        else:
            return str(self.valeur)
        
    def hauteur(self):
        if self.gauche is None:
            hgauche = -1
        else:
            hgauche = self.gauche.hauteur()
        if self.droite is None:
            hdroite = -1
        else:
            hdroite = self.droite.hauteur()    
        
        return 1 + max(hgauche, hdroite)
    
    def nb_noeuds(self):
        if self.gauche is None :
            nbg = 0
        else:
            nbg = self.gauche.nb_noeuds()
        if self.droite is None :
            nbd = 0
        else:
            nbd = self.droite.nb_noeuds()    
        return 1 + nbg + nbd
    
    def nb_feuilles(self):
        if self.gauche is None and self.droite is None:
            return 1
        elif self.gauche is None:
            return self.droite.nb_feuilles()
        elif self.droite is None:
            return self.gauche.nb_feuilles()
        else:
            return self.gauche.nb_feuilles() + self.droite.nb_feuilles()
        
       
def inserer(arbre, valeur):
    if valeur:
        if arbre.gauche == None:
            arbre.gauche = Noeud(valeur,None,None)
        else:
            inserer(arbre.gauche, valeur)
    else:
        if arbre.droite == None:
            arbre.droite = Noeud(valeur,None,None)
        else:
            inserer(arbre.droite, valeur)

def afficher(arbre):
    if arbre != None:
        print(arbre, end='')
        afficher(arbre.gauche)
        print(' ', end='')
        print(arbre, end='')
        afficher(arbre.droite)
        
def hauteur(a):
    if len(a) == 0:
        return -1
    else:
        return 1 + max(hauteur(a[1]), hauteur(a[2]))
    
def nb_noeuds(a):
    if len(a) == 0:
        return 0
    else:
        return 1 + nb_noeuds(a[1]) + nb_noeuds(a[2])
    
def nb_feuilles(a):
    if len(a) == 0:
        return 0
    elif len(a[1]) + len(a[2]) == 0:
        return 1
    else:
        return nb_feuilles(a[1]) + nb_feuilles(a[2])
        

if __name__ == '__main__':
    a=[40,[14,[5,[],[]],[4,[],[8,[],[]]]],[6,[],[]]]
    print(hauteur(a))
    print(nb_noeuds(a))
    print(nb_feuilles(a))
    print('---')
    a=Noeud(40,None,None)
    a.gauche=Noeud(14,None,None)
    a.droite=Noeud(6,None,None)
    a.gauche.gauche = Noeud(5,None,None)
    a.gauche.droite = Noeud(4,None,None)
    a.gauche.droite.droite = Noeud(8,None,None)
    print(a.hauteur())
    print(a.nb_noeuds())
    print(a.nb_feuilles())


        
