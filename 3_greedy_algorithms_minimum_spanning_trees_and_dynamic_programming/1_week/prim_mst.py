#!/usr/bin/env python

import random


def read_file(name):
    """
    Given path/name of the file, return the undirected graph in list.
    	list[1] is a tuple, which contains (node, weights) of node 1.
    """
    
    with open(name, 'r') as f:
        data = [list(map(int, line.split())) for line in f.readlines()]

    num_nodes = data[0][0]
    num_edges = data[0][1]
    
    graph = [[] for i in range(num_nodes+1)]
    for node1, node2, weight in data[1:]:
        graph[node1] += [(node2, weight)]
        graph[node2] += [(node1, weight)]
    return graph


def Prim_MST(graph):
    """
    Given the graph as a list, return the minimum spanning tree using Prim's method.
    """

    # Initialize the visited list
    X = set()

    X.add(random.choice([i for i in range(1,len(graph))]))
    T = 0
    
    while(len(X) < len(graph)-1):
        edge = {}
        
        for node in X:
            for v in graph[node]:
                if v[0] not in X:
                    edge[(node, v[0])] = v[1]

        # find the shortest edge
        (u,v),dist = min(edge.items(), key = lambda x : x[1])
    
        X.add(v)
        T+=dist

    return T


if __name__ =='__main__':
    graph = read_file('edges.txt')
    print(Prim_MST(graph))
