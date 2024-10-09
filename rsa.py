from arithmetique import *
from random import randint
from fermat import *

def genere_pseudo_premier(intervalle):
    res = randrange(min(intervalle), max(intervalle))
    while est_compose(res):
        res = randrange(min(intervalle), max(intervalle))
    assert min(intervalle) <= res < max(intervalle)
    return res

def chiffre(x, cp):
    return pow(x, cp[0], cp[1])

def dechiffre(x, cp, cprivee):
    return pow(x, cprivee, cp[0])
