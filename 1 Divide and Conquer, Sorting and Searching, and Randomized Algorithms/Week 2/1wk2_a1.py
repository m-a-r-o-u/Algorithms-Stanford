#!/usr/bin/env python


def split_inversion(bl, br):
    b = []
    i, j, sp = 0, 0, 0

    while i < len(bl) and j < len(br):
        if bl[i] <= br[j]:
            b += [bl[i]]
            i += 1
        else:
            b += [br[j]]
            j += 1
            sp += len(bl)-i

    b += bl[i:]
    b += br[j:]
    return b, sp


def inversion(a):
    """
    Count the number of Inversions.
    Inversion: elements at i and j from input a, where i<j but a[i]>a[j].
    Using Merge Sort.
    """

    n, m = len(a), len(a)//2

    if n == 1:
        return a, 0
    else:
        bl, nl = inversion(a[:m])
        br, nr = inversion(a[m:])
        b, sp = split_inversion(bl, br)
        return (b, nl + nr + sp)


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        a = [int(i) for i in f.readlines()]
    
    sa, n = inversion(a)
    is_sorted = all(sa[i] <= sa[i+1] for i in range(len(sa)-1))
    print('is sorted: ', is_sorted)
    print('inversion: ', n)
