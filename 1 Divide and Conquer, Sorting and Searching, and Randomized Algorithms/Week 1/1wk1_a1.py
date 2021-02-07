def multi(x,y):
    '''
    Recursive algorithm to multiply two integers
    '''

    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m = max(len(str(x)), len(str(y))) // 2

        a, b = x // 10**m, x % 10**m
        c, d = y // 10**m, y % 10**m

        ac = multi(a, c)
        ad = multi(a, d)
        bc = multi(b, c)
        bd = multi(b, d)

        return ac * 10**(2*m) + (ad + bc) * 10**m + bd


def karat(x,y):
    '''
    Karatsuba algorithm to multiply two integers recursively
    '''

    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m = max(len(str(x)), len(str(y))) // 2

        a, b = x // 10**m, x % 10**m
        c, d = y // 10**m, y % 10**m

        ac = karat(a, c)
        bd = karat(b, d)
        zz = karat((a+b), (c+d))

        return ac * 10**(2*m) + (zz - ac - bd) * 10**m + bd
