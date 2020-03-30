import numpy as np
import utils
import os
import re


def get_dag_rain():
    node_names = ['Y{}'.format(i) for i in range(14)]

    n = len(node_names)
    adj_matrix = np.zeros((n, n))

    path = r'C:\Users\gtx97\Google Drive\2019-2020_2_UNC_DATA\acflow\AstarLasso\networks'
    with open(os.path.join(path, 'getDAGrain.m'), 'r') as file:
        data = file.readlines()

    string = ''.join(data)

    pattern = r'\(\d+\,\d+\)'

    res = re.findall(pattern, string)

    res = [x[1:-1].split(',') for x in res]
    res = [[int(a) - 1 for a in x] for x in res]
    res = np.array(res)
    rows, cols = np.split(res, indices_or_sections=2, axis=1)
    adj_matrix[rows, cols] = 1

    top_order = utils.topological_permutation(adj_matrix)

    return adj_matrix, node_names, top_order
