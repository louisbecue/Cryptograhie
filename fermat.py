
from random import randrange
from arithmetique import pgcd, est_premier


def est_temoin_de_Fermat(a, n):
    '''
    :param int a, n:
    :return:
        - True si a est un témoin de non primalité de n
        - False sinon
    :rtype: bool
    :CU: n > 1

    Attention, bizarrement cette procédure ne considère comme témoin de non
    primalité que les "a<n" avec pgcd(a, n) == 1 (et la condition supplémentaire
    du texte).

    Pourtant si pgcd(a, n) > 1 avec a < n alors certainement on a prouvé que n
    n'était pas premier (on a trouvé un diviseur propre !). Néanmoins il faut
    renvoyer False dans ce cas.

    :Exemples:
    
    >>> n = 2**32 + 1
    >>> est_temoin_de_Fermat(2, n)
    False
    >>> est_temoin_de_Fermat(3, n)
    True
    '''
    return pow(a,n,n) != a%n


# Exercice

# Trouvez l'entier inférieur à 10000 dont le nombre de témoins de Fermat
# est relativement le plus grand, i.e. telle que la fréquence de ce
# nombre de témoins nbre temoins/(n−2) est la plus grande. Même question avec
# la fréquence la plus petite mais non nulle.

def liste_temoins(n):
    return [a for a in range(n) if est_temoin_de_Fermat(a,n)]


def est_carmichael_sans_korselt(n):
    '''Détermine si n est un nombre de Carmichael

    La méthode consistera à parcourir les a de 2 à n-1 (on s'occupera
    donc directement de n égal à 1, 2, 3 ou 4), à calculer pgcd(a, n)
    et pour ceux pour lequel ce pgcd vaut 1 à évaluer a**(n-1) modulo
    n (bien sûr par exponentiation modulaire rapide) et à regarder
    si c'est 1 dans tous les cas ; si oui, et si n n'est pas premier,
    c'est-à-dire si au moins un "a" a été trouvé avec pgcd(a, n) > 1
    (le premier a est le plus petit diviseur de n, en fait), alors 
    n est un nombre de Carmichael.

    La méthode est donc naïve et lente, ne la testez pas avec des
    entiers trop grands.

    Réfléchir aussi à gagner un facteur 2 d'efficacité. Il faut réfléchir
    au cas de a==n-1 et s'il est important de le tester. (Optionnel).

    :param int n:
    :return:
       - True si n est un nombre de Carmichael
       - False sinon
    :rtype: bool
    :CU: n > 0

    >>> est_carmichael(561)
    True
    '''
    return est_premier(n) in liste_temoins(n)


def est_carmichael(n):
    '''Détermine si n est un nombre de Carmichael par le critère de Korselt

    On utilisera la procédure decomposition_en_facteurs_premiers() et on
    lira attentivement l'énoncé du théorème de Korselt.

    :param int n:
    :return:
       - True si n est un nombre de Carmichael
       - False sinon
    :rtype: bool
    :CU: n > 0
    :Exemples:
    
    >>> any(est_carmichael(k) for k in range(1, 561))
    False
    >>> est_carmichael(561)
    True
    '''
    return n > 1 and liste_temoins(n) == [] and est_premier(n) == False



# Exercice :
#
# La décomposition en facteurs premiers des nombres de Carmichael comprend au
# moins trois facteurs premiers. Trouvez tous les nombres de Carmichael
# produits de trois nombres premiers inférieurs à 1000. Combien y en a-t-il ?
#


def est_compose(n, nbre_essais=20):
    '''
    :param int n:
    ;param int nbre_essais: nbre maximal de tentatives de trouver
                            un témoin de non primalité
    :return:
       - True si un témoin de non primalité a été trouvé
       - False sinon
    :rtype: bool
    :CU: n > 2

    '''
    return any(est_temoin_de_Fermat(randrange(2,n),n) for _ in range(nbre_essais))


# Exercice: Existe-t-il un nombre de Fermat Fn = 2**(2**n) + 1, avec 8≤n≤14
# qui soit premier ?

# Exercice : Utilisez le prédicat est_compose pour trouver un nombre
# (probablement) premier ayant 30 chiffres.


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
