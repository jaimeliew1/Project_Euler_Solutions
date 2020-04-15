# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 107 - Minimal network

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions

Using Kruskal algorithm written by:
https://gist.github.com/hayderimran7/09960ca438a65a9bd10d0254b792f48f
"""
import numpy as np

parent = dict()
rank = dict()


def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal(graph):
    for vertice in graph["vertices"]:
        make_set(vertice)
        minimum_spanning_tree = set()
        edges = list(graph["edges"])
        edges.sort()

    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)


network_mat_example = np.array(
    [
        [0, 16, 12, 21, 0, 0, 0],
        [16, 0, 0, 17, 20, 0, 0],
        [12, 0, 0, 28, 0, 31, 0],
        [21, 17, 28, 0, 18, 19, 23],
        [0, 20, 0, 18, 0, 0, 11],
        [0, 0, 31, 19, 0, 0, 27],
        [0, 0, 0, 23, 11, 27, 0],
    ]
)


def run():
    network_mat = np.loadtxt("Data/p107_network.txt", delimiter=",", dtype=int)

    edges = []
    N = len(network_mat)
    for i in range(N):
        for j in range(i):
            if network_mat[i, j] != 0:
                edges.append((network_mat[i, j], i, j))
    graph = {"vertices": list(range(N)), "edges": edges}
    minimum_tree = kruskal(graph)

    weight_0 = sum(x[0] for x in edges)
    weight = sum(x[0] for x in minimum_tree)

    return weight_0 - weight


if __name__ == "__main__":
    print(run())
