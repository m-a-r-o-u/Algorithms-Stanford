#!/usr/bin/env python


def mergeStep(l, r):
    i, j = 0, 0
    b = []
    inv = 0

    while i<len(l) and j<len(r):
        if l[i] <= r[j]:
            b += [l[i]]
            i += 1
        else:
            b += [r[j]]
            j += 1
    b += l[i:] + r[j:]
    return b


def mergeSort(a):
    n, m = len(a), len(a) // 2
    if n <= 1:
        return a
    else:
        l = mergeSort(a[:m])
        r = mergeSort(a[m:])
        b = mergeStep(l, r)
        return b


if __name__ == "__main__":
    array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
    sarray = mergeSort(array)
    is_sorted = all(sarray[i] <= sarray[i+1] for i in range(len(sarray)-1))

    print('Inp: ', array)
    print('Out: ', sarray)
    print('Is sorted: ', is_sorted)
