import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os


def plot_network(adj_matrix, node_names, dir_name, name):
    name_to_idx = {i: node_names[i] for i in range(len(node_names))}
    graph = nx.DiGraph()

    graph.add_nodes_from(node_names)
    graph.add_edges_from([[name_to_idx[a], name_to_idx[b]] for a, b in np.argwhere(adj_matrix == 1)])
    nx.draw_kamada_kawai(graph, with_labels=True)
    plt.savefig(os.path.join(dir_name, '{}.pdf'.format(name)))
