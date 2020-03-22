import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from dp_lasso import dp_lasso
from dp_lasso.get_beta_least_sq import get_beta_least_sq

Networks = ['tree', 'inversetree', 'factors', 'alarm', 'barley', 'carpo', 'chain',
            'hailfinder', 'insurance', 'mildew', 'water', 'vstructure', 'treebranch',
            'inversetreebranch', 'skinnytree', 'asia', 'dsep', 'bowling', 'funnel',
            'insurancesmall', 'alarm300', 'walrus', 'shallow21', 'chain20', 'rain',
            'cloud', 'galaxy', 'hailfinder300']


def calculate_loss(data, beta):
    return np.sqrt(np.sum(np.matmul(data, beta) ** 2) / np.shape(data)[0])


def wrap_dp_lasso(net_id, num_samples, lower_bd, upper_bd, lambda_, set_):
    name = Networks[net_id]
    file_name = os.path.join('./simdata', name,
                             '{}_lb{}_ub{}_set{}.pkl'.format(name, lower_bd * 10, upper_bd * 10, set_))
    with open(file_name, 'rb') as file:
        data = pickle.load(file)

    # standardize
    y_complete = data['Y']
    y_train = y_complete[:num_samples, :]
    mean_y = np.mean(y_train, axis=0)
    y_train -= mean_y

    # validation set
    y_val = y_complete[num_samples: num_samples + 500, :]
    y_val -= y_val - mean_y

    # test set
    y_test = y_complete[num_samples + 500:, :]
    y_test -= mean_y

    solution, _ = dp_lasso(y_train, lambda_)
    adj_matrix = solution.adj_matrix

    beta_optima = get_beta_least_sq(y_train, adj_matrix)
    val_error = calculate_loss(y_val, beta_optima)
    test_error = calculate_loss(y_test, beta_optima)

    content = {
        'meany': mean_y,
        'true_adj': data['Ayy'],
        'val_error': val_error,
        'test_error': test_error,
        'lambda': lambda_,
        'beta_optima': beta_optima
    }

    out_dirname = './results_simulations'
    out_dirname = os.path.join(out_dirname, name)
    os.makedirs(out_dirname, exist_ok=True)
    out_filename = '{}_dplasso_n{}_lb{}_ub{}_lambda{}_set{}'.format(name, num_samples, lower_bd * 10, upper_bd * 10,
                                                                    lambda_, set_)
    with open(os.path.join(out_dirname, '{}.{}'.format(out_filename, 'pkl')), 'wb') as file:
        pickle.dump(content, file)

    plt.figure()
    plt.subplot(2, 1, 1)
    sns.heatmap(data['betamatrix'], annot=True)

    plt.subplot(2, 1, 2)
    sns.heatmap(beta_optima, annot=True)
    plt.savefig(os.path.join(out_dirname, '{}.{}'.format(out_filename, 'pdf')))
