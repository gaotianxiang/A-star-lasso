import numpy as np
import utils


def get_dag_asia():
    node_names = ['Y{}'.format(i) for i in range(1, 9)]

    n = len(node_names)
    adj_matrix = np.zeros((n, n))
    adj_matrix[0, 1] = 1
    adj_matrix[1, 4] = 1
    adj_matrix[2, 3] = 1
    adj_matrix[2, 5] = 1
    adj_matrix[3, 4] = 1
    adj_matrix[5, 6] = 1
    adj_matrix[4, 6] = 1
    adj_matrix[4, 7] = 1

    top_order = utils.topological_permutation(adj_matrix)

    return adj_matrix, node_names, top_order
