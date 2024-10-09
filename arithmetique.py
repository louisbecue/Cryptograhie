def mon_divmod(a, b):
    '''
    :param a,b: (int) deux entiers
    :valeur renvoyée: (tuple) l'unique couple (q, r) tel que 
             a = bq + r   avec 0 <= r < bcorrespondant au quotient et au reste 
             (division euclidienne de a par b)
    :CU: a >= 0 et b > 0

    Algo : recherche du plus grand multiple de b <= a

    Exemples :

    >>> mon_divmod(10, 3)
    (3, 1)
    >>> mon_divmod(12, 3)
    (4, 0)
    '''
    r, q = 0, 0
    while b*q <= a:
        q += 1
    q -= 1
    return (q, a - b*q)

def pgcd(a,b):
    r = a % b
    q = (a+r)//b
    while r != 0:
        a = b
        b = r
        r = a % b
        q = (a+r)//b
    return b

def euclide_pos(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        pgcd, u, v = euclide_pos(b, a%b)
        assert b*u + (a%b) * v == pgcd
        q = a//b
        return (pgcd, v, u -v * q)

def algorithme_euclide(a,b):
    """  
    :param a, b: (int) deux nombres entiers
    :returns: (int) pgcd de a et b
    :CU: (a, b) != (0, 0)
    :Exemples:
    >>> algorithme_euclide(230,126)
    (2, -23, 42)
    """ 
    (pgcd, u , v) = euclide_pos(abs(a), abs(b))
    if a < 0 :
        u = -u
    if b < 0: 
        v= -v
    return (pgcd, u, v)

def inverse_mod(a, n):
    """
    :param a, n: (int) deux entiers
    :valeur renvoyée: (int) l'inverse de a modulo n
    :CU: n non nul et a inversible modulo n 
    :Exemples:
    >>> inverse_mod(3, 7)
    5
    >>> inverse_mod(3, 26)
    9
    >>> inverse_mod(47337338776803609, 114875698154581919)
    64484911222477487
    """
    (d, u ,v) = algorithme_euclide(a, n)
    if d >1:
        res  = 0
    else :
        res = u %n 
    return res


def plus_petit_diviseur_premier(n):
    """Renvoie le plus petit diviseur premier de n.
    CU : n est un entier positif strictement plus grand que 1.
    Exemples:

    >>> plus_petit_diviseur_premier(2)
    2

    >>> plus_petit_diviseur_premier(2431)
    11

    >>> plus_petit_diviseur_premier(17**2)
    17
    """
    assert n >= 2
    d = 2
    while n%d!=0:
        d += 1
    return d

def decomposition_facteurs_premiers(n):
    """Renvoie la décomposition en facteur premier de n
        CU : n est un entier positif strictement plus grand que 1.
        Exemples:

        >>> decomposition_facteurs_premiers(40500)
        {2: 2, 3: 4, 5: 3}
    """
    n = 1

def racine_entiere(n):
    """
    CU : n >= 0
    >>> racine_entiere(82)
    9
    >>> racine_entiere(99)
    9
    >>> racine_entiere(100)
    10
    >>> racine_entiere(101)
    10
    """
    pass

def plus_petit_diviseur_premier(n):
    """Renvoie le plus petit diviseur premier de n.
    CU : n est un entier positif strictement plus grand que 1.
    Exemples:

    >>> plus_petit_diviseur_premier(2)
    2

    >>> plus_petit_diviseur_premier(2431)
    11

    >>> plus_petit_diviseur_premier(17**2)
    17
    """


def test_primalite1(p):
    """Renvoie vrai si p est un nombre premier, faux sinon. Pour cela, la fonction cherche un diviseur inférieur à p.
    CU : p est un entier positif strictement plus grand que 1.
    Exemples:

    >>> test_primalite1(2)
    True

    >>> test_primalite1(13)
    True

    >>> test_primalite1(100)
    False
    """
    assert type(p)==int and p>1, "p doit être un entier positif strictement plus grand que 1."
    if p <= 2:
        return False
    for i in range(1,p):
        if p%i == 0:
            return False
    return True


def nombres_premiers_inferieurs(n):
    """Renvoie la liste des nombres premiers inférieurs à n.
    CU : n est un entier supérieur ou égal à 2
    >>> nombres_premiers_inferieurs(10)
    [2, 3, 5, 7]
    """

def crible_eratosthene(n):
    """Renvoie la liste des nombres premiers inférieurs à n.
    CU : n est un entier supérieur ou égal à 2
    >>> crible_eratosthene(10)
    [2, 3, 5, 7]
    """


def test_primalite2(p):
    """Renvoie vrai si p est un nombre premier, faux sinon. Pour cela, la fonction cherche un diviseur inférieur à p.
    CU : p est un entier positif strictement plus grand que 1.
    Exemples:

    >>> test_primalite2(2)
    True

    >>> test_primalite2(13)
    True

    >>> test_primalite2(100)
    False
    """

def est_premier(p):
    if p < 2:
        return False
    for i in range(2,p):
        if p%i == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)