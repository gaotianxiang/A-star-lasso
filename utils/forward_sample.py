import numpy as np


def forward_sample(adj_matrix, top_order, num_samples, q, lower_bd, upper_bd):
    print(top_order)
    data = np.zeros((num_samples, q))
    sigma = 1
    s = np.random.binomial(1, 0.5, (q, 1))
    s[s == 0] = -1
    beta_y = np.random.uniform(lower_bd, upper_bd, (q, 1))
    beta_y *= s

    for j in range(len(top_order)):
        curr = top_order[j]
        pay = np.argwhere(adj_matrix[:, curr])
        if len(pay) == 0:
            data[:, curr] = np.random.normal(0, 1, num_samples)
        else:
            m = np.sum(data[:, pay] * beta_y[pay], axis=1)
            data[:, curr] = np.random.normal(m, sigma)

    return data, beta_y