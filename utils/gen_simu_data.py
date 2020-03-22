import networks
import os
import pickle

from utils import forward_sample
from utils import plot_network

networks = ['tree', 'inversetree', 'factors', 'alarm', 'barley', 'carpo', 'chain',
            'hailfinder', 'insurance', 'mildew', 'water', 'vstructure', 'treebranch',
            'inversetreebranch', 'skinnytree', 'asia', 'dsep', 'bowling', 'funnel',
            'insurancesmall', 'alarm300', 'walrus', 'shallow21', 'chain20', 'rain',
            'cloud', 'galaxy', 'hailfinder300']


def gen_simu_data(net_id, num_sets, lower_bd, upper_bd, num_samples):
    name = networks[net_id]
    func_name = 'get_dag_{}'.format(name)
    # adj_matrix, node_names, top_order = getattr(networks, func_name)
    adj_matrix, node_names, top_order = networks.get_dag_asia()

    q = len(node_names)
    dir_name = '../simdata'
    os.makedirs(dir_name, exist_ok=True)
    plot_network(adj_matrix, node_names, dir_name, name)

    print('Generating data for network {}'.format(name))

    for i in range(num_sets):
        msg = 'generating set {}'.format(i)
        print(msg)

        file_name = os.path.join(dir_name, name, '{}_lb{}_ub{}_set{}.pkl'.format(name, lower_bd * 10,
                                                                                 upper_bd * 10, i))
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        data, beta_true, beta_matrix = forward_sample(adj_matrix, top_order, num_samples, q, lower_bd, upper_bd)

        with open(file_name, 'wb+') as file:
            content = {
                'Y': data,
                'Ayy': adj_matrix,
                'toporder': top_order,
                'name': name,
                'lowerbd': lower_bd,
                'upper': upper_bd,
                'betature': beta_true,
                'betamatrix': beta_matrix
            }
            pickle.dump(content, file)
