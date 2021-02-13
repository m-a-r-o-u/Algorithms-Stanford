#!/usr/bin/env python

import time
from ast import literal_eval


def graph_from_file(name):
    """
    Given the name of the file , return the graph in list.
    Graph Format: list over nodes,
        contain lists of tuples of the form [(adjacent_node, weight), ...]
    """

    with open(name, 'r') as f:
        lines = f.readlines()

    num_nodes = len(lines) + 1
    graph = [None] * num_nodes
    for line in lines:
        items = [literal_eval(l) for l in line.split()]
        graph[items[0]] = items[1:]

    return graph, num_nodes


def dijkstra(graph, num_nodes=201):
    """
    The Main function of Dijkatra's shortest path algorithm.
    Initialize distances to a large value: 1000000.
    First calculate the distance scores for crossing edges.
    A crossing edge connects between visited and unvisited nodes.
    The node with the minimal distance scores is added to the visited nodes.
    """

    visited = [1]

    dis = [1000000] * (num_nodes)
    dis[1] = 0

    while len(visited) < (num_nodes-1):
        scores = {}
        for vnode in visited:
            for node, weight  in graph[vnode]:
                if node not in visited:
                    scores[(vnode, node)] = dis[vnode] + weight

        (_, edge), dist = min(scores.items(), key=lambda x: x[1])
        dis[edge] = dist
        visited.append(edge)
    return dis


if __name__ == "__main__":
    graph, num_nodes = graph_from_file('data.txt')
    dis = dijkstra(graph, num_nodes)

    end_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    end_score = [str(dis[end]) for end in end_nodes]
    print(','.join(end_score))
