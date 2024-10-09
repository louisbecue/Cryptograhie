from alphabet import Alphabet, ALPHABETS

def chiffre_lettre(lettre, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """
    renvoie la lettre chiffrée correspondant à ̀`lettre`` par la méthode de César,
    avec un décalage donné par ``cle``.

    :param lettre: (str) lettre à chiffrer
    :param cle: (int) clé de chiffrement (décalage)
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (str) lettre chiffrée
    :CU: lettre doit appartenir à alphabet
    :Exemple:

    >>> tuple(chiffre_lettre(k, 3) for k in 'CESAR')
    ('F', 'H', 'V', 'D', 'U')
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> tuple(chiffre_lettre(k, 8, decimal) for k in '012')
    ('8', '9', '0')
    >>> greek = ALPHABETS['LOWER_GREEK']
    >>> tuple(chiffre_lettre(k, 7, greek) for k in 'μιακ')
    ('σ', 'π', 'θ', 'ρ')
    """
    return alphabet[(alphabet.index(lettre)+cle)%len(alphabet)]

def chiffre_message(msg, cle, alphabet=ALPHABETS['CAPITAL_LATIN']):
    """
    renvoie le message ``msg`` chiffré par la méthode César, 
    avec un décalage donné par ``cle``.

    :param msg: (str) message à chiffrer
    :param cle: (int) clé de chiffrement (décalage)
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (str) message chiffré
    :CU: les caractères de ``msg`` doivent appartenir à ``alphabet``
    :Exemple:

    >>> chiffre_message('CESAR', 3)
    'FHVDU'
    >>> decimal = ALPHABETS['DECIMAL_DIGITS']
    >>> chiffre_message('012', 8, decimal)
    '890'
    >>> greek = ALPHABETS['LOWER_GREEK']
    >>> chiffre_message('μιακ', 7, greek)
    'σπθρ'
    """
    res = ''
    for lettre in msg:
            res += alphabet[(alphabet.index(lettre)+cle)%len(alphabet)]
    return res



def dechiffre_message(msg, cle, alphabet=Alphabet()):
    """
    renvoie le message ``msg`` déchiffré par la méthode César, 
    avec un décalage donné par ``cle``.

    :param msg: (str) message à déchiffrer
    :param cle: (int) clé de chiffrement (décalage)
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (str) message déchiffré
    :CU: les caractères de ``msg`` doivent appartenir à ``alphabet``
    :Exemple:

    >>> dechiffre_message('FHVDU', 3)
    'CESAR'
    >>> decimal = Alphabet('0123456789')
    >>> dechiffre_message('890', 8, decimal)
    '012'
    >>> greek = ALPHABETS['LOWER_GREEK']
    >>> dechiffre_message('σπθρ', 7, greek)
    'μιακ'
    """
    res = ''
    for lettre in msg:
        res += alphabet[(alphabet.index(lettre)-cle)%len(alphabet)]
    return res


def decrypte_message(msg, car_freq, alphabet=Alphabet()):
    """
    essaie de décrypter le message ``msg`` chiffré par la méthode César, 
    avec un décalage inconnu.
 
    :param msg: (str) message à décrypter
    :param car_freq: (str) caractère supposé le plus fréquent dans le clair
    :param alphabet: (Alphabet) paramètre optionnel définissant l'alphabet. 
              Valeur par défaut : alphabet des 26 lettres latines capitales
    :valeur renvoyée: (list) liste de message(s) décrypté(s) possible(s) (on l'espère)
    :CU: les caractères de ``msg`` ainsi que ``car_freq`` doivent appartenir à ``alphabet``
    :Exemple:

    >>> decrypte_message('OQYQEEMSQBAEEQPQTGUFRAUEXMXQFFDQQ', 'E')
    ['CEMESSAGEPOSSEDEHUITFOISLALETTREE']
    """
    max_E = (0,0)
    for i in range(len(alphabet)):
        msg_mod = chiffre_message(msg, i)
        if msg_mod.count(car_freq) >= max_E[0]:
            max_E = (msg.count(car_freq), i)
    return [chiffre_message(msg, max_E[1])]


    
if __name__ == '__main__':
    import doctest, sys
    doctest.testmod(verbose=False)