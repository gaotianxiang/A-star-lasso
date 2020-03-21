import numpy as np


def topological_permutation(adj_matrix):
    indices = np.argwhere(adj_matrix)

    topo_sort = []
    queue = []
    node_to_indegree = {}
    node_to_next = {}
    for i in range(len(adj_matrix)):
        node_to_indegree[i] = 0
        node_to_next[i] = []

    for a, b in indices:
        node_to_indegree[b] = node_to_indegree[b] + 1
        node_to_next[a].append(b)

    for k, v in node_to_indegree.items():
        if v == 0:
            queue.append(k)

    queue.sort()
    topo_sort += queue

    while queue:
        this_level = []
        n = len(queue)

        for _ in range(n):
            curr = queue.pop(0)
            for node in node_to_next[curr]:
                node_to_indegree[node] = node_to_indegree[node] - 1
                if node_to_indegree[node] == 0:
                    this_level.append(node)
                    queue.append(node)
        this_level.sort()
        topo_sort += this_level

    return topo_sort
