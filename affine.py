from alphabet import Alphabet, ALPHABETS
from arithmetique import pgcd, inverse_mod


def cle_valide(cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """
    :param cle: (tuple) couple (a, b) de deux entiers
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (bool)
      - True si cle est une clé valide, i.e. si a est premier avec la taille de l'alphabet
      - False sinon
    :CU: aucune

    >>> cle_valide((4, 3))
    False
    >>> cle_valide((5, 3))
    True
    >>> cle_valide((5, 3), ALPHABETS['DECIMAL_DIGITS'])
    False
    >>> cle_valide((12, 9), ALPHABETS['LOWER_GREEK'])
    True
    """
    return pgcd(cle[0], len(alphabet))==1
     


def chiffre_lettre(lettre, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """
    :param lettre: (str) lettre à chiffrer
    :param cle: (tuple) couple d'entiers (a, b), clé de chiffrement
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: la lettre lettre chiffrée avec la clé cle.
    :CU: cle = (a,b) doit être tel que a inversible modulo la taille de alphabet
         lettre : str de long 1 et dans alphabet

    >>> tuple(chiffre_lettre(k, (3, 7)) for k in 'ABC')
    ('H', 'K', 'N')
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> tuple(chiffre_lettre(k, (3, 7), decimal) for k in '012')
    ('7', '0', '3')
    >>> greek = ALPHABETS['LOWER_GREEK']
    >>> tuple(chiffre_lettre(k, (12, 9), greek) for k in 'μιακ')
    ('ρ', 'ζ', 'κ', 'ς')
    """
    return alphabet[(alphabet.index(lettre)*cle[0]+cle[1])%len(alphabet)]

def chiffre_message(msg, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """
    :param msg: (str) message à chiffrer
    :param cle: (tuple) couple d'entiers (a, b), clé de chiffrement
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (str) message msg chiffré avec la clé cle.
    :CU: cle = (a,b) doit être tel que a inversible modulo la taille de alphabet
         les caractères de msg doivent être dans alphabet

    >>> chiffre_message('ABC', (3, 7))
    'HKN'
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> chiffre_message('012', (3, 7), decimal)
    '703'
    >>> greek = ALPHABETS['LOWER_GREEK']
    >>> chiffre_message('μιακ', (12, 9), greek)
    'ρζκς'
    """
    res = ''
    for lettre in msg:
            res += alphabet[(alphabet.index(lettre)*cle[0]+cle[1])%len(alphabet)]
    return res


def dechiffre_message(msg, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """
    :param msg: (str) message à déchiffrer
    :param cle: (tuple) couple d'entiers (a, b), clé de chiffrement
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (str) le message msg déchiffré avec la clé cle.
    :CU: cle = (a,b) doit être tel que a inversible modulo la taille de alphabet
         les caractères de msg doivent être dans alphabet

    >>> dechiffre_message('HKN', (3, 7))
    'ABC'
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> dechiffre_message('703', (3, 7), decimal)
    '012'
     >>> greek = ALPHABETS['LOWER_GREEK']
    >>> dechiffre_message('ρζκς', (12, 9), greek)
    'μιακ'
    """
    ainv = inverse_mod(cle[0], len(alphabet))
    return chiffre_message(msg, (ainv, -ainv * cle[1]), alphabet)

    
if __name__ == '__main__':
    import doctest, sys
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)