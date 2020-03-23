import numpy as np
import heapq
import copy
from sklearn.linear_model import Lasso


class Node:
    def __init__(self, vertex, vertices_order, edge_path, adj_m, beta, h, g):
        self.vertex = vertex
        self.vertices_order = vertices_order
        self.edge_path = edge_path
        self.adj_matrix = adj_m
        self.beta = beta
        self.h = h
        self.g = g
        self.f = h + g

    def __hash__(self):
        return repr(self).__hash__()

    def __repr__(self):
        return '#'.join([str(x) for x in sorted(self.vertices_order)])

    def __lt__(self, other):
        return self.f < other.f


def list_to_key(vertex_path):
    path = [str(x) for x in sorted(vertex_path)]
    return '#'.join(path)


def run_lasso(x, y, lambda_c):
    lasso = Lasso(alpha=lambda_c)
    lasso.fit(x, y)
    return lasso.coef_


def remove(all_v, parent):
    return [x for x in all_v if x not in parent]


def get_h_score(data, lambda_c):
    pre_computed_lasso_scores = []
    _, q = np.shape(data)
    sum_score = 0
    for j in range(q):
        # print('pre-computing score for vertex_{}'.format(j))
        mask = np.ones(q, dtype=np.bool)
        mask[j] = 0
        y = data[:, j]
        x = data[:, mask]
        beta = run_lasso(x, y, lambda_c)
        y_diff = y - x.dot(beta)
        score = y_diff.dot(y_diff) + lambda_c * np.sum(np.abs(beta))
        pre_computed_lasso_scores.append(score)
        sum_score += score

    return sum_score, pre_computed_lasso_scores


def a_star_lasso(data, lambda_c):
    n, q = np.shape(data)

    all_vertices = np.arange(q)
    level = 0

    min_heap = []
    visited = set()

    print('running full A* lasso')
    sum_score, pc_lasso_score = get_h_score(data, lambda_c)
    print(sum_score)
    start_node = Node(-1, list(), list(), np.zeros((q, q)), np.zeros((q, q)), sum_score, 0)
    heapq.heappush(min_heap, start_node)
    # visited.add(repr(start_node))

    while len(min_heap) > 0:
        cur_node = heapq.heappop(min_heap)
        visited.add(repr(cur_node))

        if len(cur_node.vertices_order) == q:
            return cur_node, level

        candidate_child = remove(all_vertices, cur_node.vertices_order)

        for child in candidate_child:
            vertices_order = copy.deepcopy(cur_node.vertices_order)
            vertices_order.append(child)
            if list_to_key(vertices_order) in visited:
                continue

            edge_path = copy.deepcopy(cur_node.edge_path)
            adj_m = copy.deepcopy(cur_node.adj_matrix)
            beta = copy.deepcopy(cur_node.beta)
            h_score = cur_node.h
            g_score = cur_node.g

            y = data[:, child]

            if len(cur_node.vertices_order) == 0:
                curr_g = y.dot(y)
            else:
                parent = cur_node.vertices_order
                parent_data = data[:, parent]

                beta_child = run_lasso(parent_data, y, lambda_c)
                beta[parent, child] = beta_child
                identity = beta_child != 0
                adj_m[parent, child] = identity

                y_diff = y - parent_data.dot(beta_child)
                curr_g = y_diff.dot(y_diff) + lambda_c * np.sum(np.abs(beta_child))
            g_score += curr_g
            h_score -= pc_lasso_score[child]

            child_node = Node(child, vertices_order, edge_path, adj_m, beta, h_score, g_score)
            heapq.heappush(min_heap, child_node)
