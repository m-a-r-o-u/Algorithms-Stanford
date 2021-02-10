#!/usr/bin/env python
"""
QuickSort with different pivot
"""

def elect(a):
    findpivot = [a[0], a[(len(a)-1)//2], a[-1]]
    k = findpivot.copy()
    k.remove(min(k))
    knum = findpivot.index(min(k))
    pivotnum = 0 if knum == 0 else (len(a)-1)//2 if knum == 1 else len(a)-1
    a[0], a[pivotnum] = a[pivotnum], a[0]
    return a[0]

def final(a):
    a[0], a[-1] = a[-1], a[0]
    return a[0]

def first(a):
    return a[0]

select_pivot = {'first':first, 'final':final, 'elect':elect}

def quick_sort(a, method):
    if len(a) <= 1:
        return (a, 0)

    pivot = select_pivot[method](a)

    i, j = 1, 1
    n = len(a)-1
    while j < len(a):
        if a[j] > pivot:
            j += 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1

    a[0], a[i-1] = a[i-1], a[0]
    a[:i-1], l = quick_sort(a[:i-1], method)
    a[i:], r = quick_sort(a[i:], method)
    return (a, n + l + r)


if __name__ == "__main__":
    with open('data.txt', 'r') as f:
        data = [int(i) for i in f.readlines()]

    d1, n1 = quick_sort(data.copy(), 'first')
    d2, n2 = quick_sort(data.copy(), 'final')
    d3, n3 = quick_sort(data.copy(), 'elect')

    print(f'first:{n1}, final:{n2}, advanced:{n3}')
