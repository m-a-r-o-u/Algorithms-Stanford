#!/usr/bin/env python

import numpy as np

def read_file(name):
    """
    Given the path/nname of a file,
    return the Values list, Weights list, capacity and number of jobs.
    """
    data = np.loadtxt(name, dtype=int)
    capacity, n = data[0]

    V, W = [0], [0]
    for v, w in data[1:]:
        V.append(v)
        W.append(w)
    return V, W, capacity, n


def knapsack_dynamic(V, W, capacity, numbers):
    """
    Return the matrix of maximum value
    """
    # initialize the 2-d array
    A = [[0]*(capacity+1) for x in range(numbers+1)]
    for i in range(1,numbers+1):
        for j in range(capacity+1):
            # make sure the size of current is not larger than the current capacity.
            if W[i]>j:
                A[i][j] = A[i-1][j]
            else:
                A[i][j] = max(A[i-1][j],A[i-1][j-W[i]]+V[i])
    return A


if __name__ == '__main__':
    V,W, capacity, n = read_file('knapsack.txt')
    A = knapsack_dynamic(V,W, capacity, n)
    print(A[-1][-1])

### Test case:
#V,W, capacity, n = read_file('knapsack.txt')
#values = [0,3,2,4,4]
#sizes = [0,4,3,2,3]
#capacity = 6
#numbers = 4
#B = knapsack_dynamic(values, sizes, capacity, numbers)
#B[-1][-1] # The answer should be 8.
