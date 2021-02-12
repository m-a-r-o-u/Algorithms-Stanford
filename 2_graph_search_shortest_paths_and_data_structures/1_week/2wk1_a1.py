#!/usr/bin/env python

import numpy as np
import sys
import threading
import time


def get_num_nodes(edges):
    set1 = set(edges[:, 0])
    set2 = set(edges[:, 1])
    return len({*set1, *set2})


def read_file(name):
    """
    Read in the file under the input variable 'name'.
    Generate forward and reverse graph.
    """

    with open(name, 'r') as f:
        edges = np.array([line.split() for line in f.readlines()]).astype(int)
        #edges = np.array([list(map(int, line.split())) for line in f.readlines()])
    
    # +1?
    num_nodes = get_num_nodes(edges) + 1
    
    G = [[] for i in range(num_nodes)]
    G_rev = [[] for i in range(num_nodes)]
    
    for i, j in edges:
        G[i] += [j]
        G_rev[j] += [i]
        
    return G, G_rev, num_nodes


def dfs1(rgraph, i):
    global t, visited
    visited[i] = True
    
    for edge in rgraph[i]:
        if not visited[edge]:
            dfs1(rgraph, edge)

    finish[t] = i
    t = t+1
    

def dfs_loop1(rgraph, num_nodes):
    global t, visited, finish
    visited = [False]*num_nodes
    finish = [None]*num_nodes
    t = 0
    for node in reversed(range(num_nodes)):
        if not visited[node]:
            dfs1(rgraph, node)
    return finish
    

def dfs2(graph, i):
    
    global scc_size, visited
    visited[i] = True
    for edge in graph[i]:
        if not visited[edge]:
            dfs2(graph,edge)
    scc_size += 1


def dfs_loop2(graph, num_nodes):
    
    global scc_size, visited, finish
    visited = [False]*num_nodes
    scc = []
    
    for node in reversed(range(num_nodes)):
        if not visited[finish[node]]:
            scc_size = 0
            dfs2(graph, finish[node])
            scc.append(scc_size)
    return scc
    
    
def combine(graph, rgraph, num_nodes):
    finish = dfs_loop1(rgraph, num_nodes)
    scc = dfs_loop2(graph, num_nodes)
    return scc


def main():
    graph, rgraph, num_nodes = read_file('data.txt')
    scc = combine(graph, rgraph, num_nodes)
    print(','.join(map(lambda x: str(x), sorted(scc)[::-1][:5])))


if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
