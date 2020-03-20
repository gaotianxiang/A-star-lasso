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

    p = utils.topological_permutation(adj_matrix)

    return adj_matrix, node_names,


# function [adjMatrix,nodeNames,toporder] = getDAGasia()
# nodeNames{1} = 'Y1';
# nodeNames{2} = 'Y2';
# nodeNames{3} = 'Y3';
# nodeNames{4} = 'Y4';
# nodeNames{5} = 'Y5';
# nodeNames{6} = 'Y6';
# nodeNames{7} = 'Y7';
# nodeNames{8} = 'Y8';
#
# adjMatrix = zeros(length(nodeNames));
# adjMatrix(1,2) = 1;
# adjMatrix(2,5) = 1;
# adjMatrix(3,4) = 1;
# adjMatrix(3,6) = 1;
# adjMatrix(4,5) = 1;
# adjMatrix(6,7) = 1;
# adjMatrix(5,7) = 1;
# adjMatrix(5,8) = 1;
#
# P = topologicalPermutation(adjMatrix);
# % adjMatrix = adjMatrix(P,P);
# % nodeNames = nodeNames(P);
# toporder = P;
#
# end