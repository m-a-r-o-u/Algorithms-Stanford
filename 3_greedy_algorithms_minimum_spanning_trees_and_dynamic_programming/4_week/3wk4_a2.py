#!/usr/bin/env python

"""
Knapsack algorithm 2
"""

import numpy as np

def read_file(name):
    data = np.loadtxt(name, dtype=int)
    capacity, n = data[0]

    V, W = [0], [0]
    for v, w in data[1:]:
        V.append(v)
        W.append(w)
    return V, W, capacity, n


def knapsack(v, w , Wall, N):
    solution = [[N, Wall]]
    ans = solution[0]
    soludic = {(N, Wall): 0}
    i = 0
    ni = N
    while True:
        ni, wi = ans
        x, y = [ni-1, wi], [ni-1, wi-w[ni-1]]
        if ni >= 1:
            if tuple(x) not in soludic:
                solution += [x]
                soludic[tuple(x)] = 0
            if wi >= w[ni-1]:
                if tuple(y) not in soludic:
                    solution += [y]
                    soludic[tuple(y)] = 0
        i += 1
        if i == len(solution):
            break
        else:
            ans = solution[i]
        if i % 1000000 == 0:
            print(i)
    
    nn = len(solution)
    for i in list(range(nn))[::-1]:
        ni, wi = solution[i]
        if i % 1000000 == 0:
            print(i)
        if ni == 0:
            continue
        soludic[(ni, wi)] = max(soludic[(ni-1, wi)], soludic[(ni-1), wi-w[ni-1]]+v[ni-1]) if wi >= w[ni-1] else soludic[(ni-1, wi)]
    print(soludic[(N, Wall)])


if __name__ == "__main__":
    v, w, Wall, N = read_file('knapsack_big.txt')
    knapsack(v, w, Wall, N)

