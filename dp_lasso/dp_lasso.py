import numpy as np
import copy
from sklearn.linear_model import Lasso


class Node:
    def __init__(self, vertex, vertices_order, edge_path, z, beta_z, g):
        self.vertex = vertex
        self.vertices_order = vertices_order
        self.edge_path = edge_path
        self.adj_matrix = z
        self.beta_z = beta_z
        self.g = g


def remove(all_v, parent):
    return [x for x in all_v if x not in parent]


def run_lasso(x, y, lambda_c):
    lasso = Lasso(alpha=lambda_c)
    lasso.fit(x, y)
    return lasso.coef_


def list_to_key(vertex_path):
    path = [str(x) for x in sorted(vertex_path)]
    return '#'.join(path)


def dp_lasso(data, lambda_c):
    n, q = np.shape(data)

    z = np.zeros((q, q))
    beta_z = np.zeros((q, q))
    all_vertices = np.arange(q)
    level = 0

    history = {}
    queue = []
    # vertex = []
    parent_vertices_order = []
    parent_edge_path = []
    g = 0

    queue.append(Node(-1, parent_vertices_order, parent_edge_path, z, beta_z, g))

    while True:
        if level != 0 and len(queue) == 1:
            solution = queue[0]
            return solution, level

        pos = 0
        temp_queue = []

        for p in range(len(queue)):
            parent = queue[p]
            # vertices_order = copy.deepcopy(parent.vertices_order)
            candidate_children = remove(all_vertices, parent.vertices_order)

            for i in range(len(candidate_children)):
                child = candidate_children[i]
                parent_vertices_order = copy.deepcopy(parent.vertices_order)
                parent_edge_path = copy.deepcopy(parent.edge_path)
                parent_z = copy.deepcopy(parent.adj_matrix)
                parent_beta_z = copy.deepcopy(parent.beta_z)
                parent_g = parent.g

                vertices_order = parent_vertices_order + [child]
                y = data[:, child]

                if len(parent_vertices_order) == 0:
                    curr_g = y.dot(y)
                else:
                    pvo = parent_vertices_order
                    num_potential_parent = len(pvo)
                    parent_data = data[:, pvo]
                    beta = np.zeros(num_potential_parent)
                    if num_potential_parent != 0:
                        beta = run_lasso(parent_data, y, lambda_c)
                        parent_beta_z[pvo, child] = beta

                        identity = beta != 0
                        parent_z[pvo, child] = identity

                        for j in range(len(pvo)):
                            if identity[j] == 0:
                                continue
                            parent_edge_path.append([pvo[j], child])

                    y_minus = y - parent_data.dot(beta)
                    curr_g = y_minus.dot(y_minus) + lambda_c * np.sum(np.abs(beta))

                g = curr_g + parent_g

                key = list_to_key(vertices_order)
                node = Node(child, vertices_order, parent_edge_path, parent_z, parent_beta_z, g)

                if key not in history:
                    history[key] = pos
                    temp_queue.append(node)
                    pos += 1
                else:
                    queue_pos = history[key]
                    dup_node = temp_queue[queue_pos]
                    if g < dup_node.g:
                        temp_queue[queue_pos] = node
            level += 1
        queue = temp_queue
