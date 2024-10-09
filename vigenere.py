from alphabet import Alphabet, ALPHABETS
from cesar import chiffre_lettre

def chiffre_message(msg, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """
    renvoie la chaîne msg chiffrée par le système de Vigenere 
    avec la clé cle.
    
    :param msg: (str) message à chiffrer
    :param cle: (tuple) clé de chiffrement sous forme d'un tuple d'entiers (les décalages)
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (str) message chiffré
    :CU: msg ne contient que des lettres de alphabet et chaque entier de cle est 
         dans l'intervalle  [0, len(alphabet)[.
    :Exemples:

    >>> chiffre_message('TIMOLEON', (0, 1, 2))
    'TJOOMGOO'
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> chiffre_message('0123456789', (1, 0, 9), decimal)
    '1114447770'
    """
    res = ''
    for i in range(len(msg)):
        res += alphabet[(alphabet.index(msg[i]) + cle[i%len(cle)])%len(alphabet)]
    return res



def dechiffre_message(msg, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """
    renvoie la chaîne msg déchiffrée par le système de Vigenere 
    avec la clé cle.

    :param msg: (str) message à déchiffrer
    :param cle: (tuple) clé de chiffrement tuple de décalages
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (str) message déchiffré
    :CU: msg  ne contient que des lettres de alphabet et chaque entier de cle est 
         dans l'intervalle  [0, len(alphabet)[.
    :Exemples:

    >>> dechiffre_message('TJOOMGOO', (0, 1, 2))
    'TIMOLEON'
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> dechiffre_message('1114447770', (1, 0, 9), decimal)
    '0123456789'
    """
    res = ''
    for i in range(len(msg)):
        res += alphabet[(alphabet.index(msg[i]) - cle[i%len(cle)])%len(alphabet)]
    return res

                               
'l|$!+d<<B/(="sy|%r|Xp|8F(p|glG&MglzA0_hV`UU'
'http://'
'https://'

if __name__ == '__main__':
    import doctest, sys
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)