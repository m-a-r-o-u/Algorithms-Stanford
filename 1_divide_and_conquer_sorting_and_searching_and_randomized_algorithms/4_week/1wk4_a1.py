#!/usr/bin/env python

import copy
import random


def mincut(g):
    '''
    Karger Algorithm: Estimate the graph split with the minimum number of cuts
    '''
    while len(g) > 2:
        '''Choose a random node'''
        _ = random.choice(range(len(g)))
        v_del = g.pop(_)
        _ = random.choice(range(1, len(v_del)))
        v1, v2 = v_del[0], v_del[_]

        while v2 in v_del:
            v_del.remove(v2)

        for i in range(len(g)):
            if g[i][0] == v2:
                g[i] += v_del
                while v1 in g[i]:
                    g[i].remove(v1)
            for j in range(len(g[i])):
                if g[i][j] == v1:
                    g[i][j] = v2
    return len(g[0]) - 1


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = [list(map(int, i.split('\t')[:-1])) for i in f.readlines()]

    cuts = []
    for i in range(1000):
        cuts += [mincut(copy.deepcopy(data))]
        minimum = min(cuts)
        if not i % 50:
            print(f'Split: {i:4d}, Minimum: {minimum}')

    print(f'Final Estimated Minimum: {minimum}')
