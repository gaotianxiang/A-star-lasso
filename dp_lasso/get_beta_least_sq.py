import numpy as np


def get_beta_least_sq(data, adj_matrix):
    _, n = np.shape(adj_matrix)
    beta = np.zeros((n, n))

    for col in range(n):
        y = data[:, col]
        parent = np.argwhere(adj_matrix[:, col]).squeeze(axis=-1)
        if len(parent) == 0:
            continue

        x = data[:, parent]
        cur_beta = np.linalg.inv(np.matmul(x.T, x))
        cur_beta = np.matmul(cur_beta, x.T).dot(y)

        beta[parent, col] = cur_beta
    return beta
