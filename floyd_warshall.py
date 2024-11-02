import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import product
INF = float('inf')
def floyd(graph):
    nV = len(graph)
    dist = np.copy(graph)
    for k in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][k] + dist[k][q])
    return dist
def print_solution(dist):
    nV = len(dist)
    for p in range(nV):
        for q in range(nV):
            if dist[p][q] == INF:
                print("INF", end=" ")
            else:
                print(dist[p][q], end=" ")
        print()
G = [
    [0, 5, INF, INF],
    [50, 0, 15, 5],
    [30, INF, 0, 15],
    [15, INF, 5, 0]
]
dist_matrix = floyd(G)
print("Shortest distance matrix after running Floyd-Warshall:")
print_solution(dist_matrix)

'''output:Shortest distance matrix after running Floyd-Warshall:
0 5 15 10 
20 0 10 5 
30 35 0 15 
15 20 5 0 '''
