def pgcd(a, b):
    if b ==0:
        return a
    else :
        return pgcd(b, a%b)

def euclide_pos(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        pgcd, u, v = euclide_pos(b, a%b)
        assert b*u + (a%b) * v == pgcd
        q = a//b
        return (pgcd, v, u -v * q)

def euclide(a, b):
    (pgcd, u , v) = euclide_pos(abs(a), abs(b))
    if a < 0 :
        u = -u
    if b < 0: 
        v= -v
    return (pgcd, u, v)

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)