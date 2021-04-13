import networkx as nx
import numpy as np


def steiner_tree(g, t_list):
    """
    Find heuristic solution of Steiner tree problem by online algorithm
    :param g: given graph (networkx.Graph)
    :param t_list: terminal list (list)
    :return: solution edge set and objective value (list, double)
    """
    sol_edge = set([])
    sol_node = [t_list[0]]
    for i in range(1, len(t_list)):
        current_t = t_list[i]
        length_arr = []
        path_arr = []
        # find the shortest path to the solution set by examining the nodes in the solution set
        for s in sol_node:
            path_node = nx.shortest_path(g, source=s, target=current_t, weight='weight')
            length = nx.shortest_path_length(g, source=s, target=current_t, weight='weight')
            # build path from shortest path
            path = []
            for index in range(len(path_node) - 1):
                node1 = path_node[index]
                node2 = path_node[index + 1]
                path.append((min(node1, node2), max(node1, node2)))
            length_arr.append(length)
            path_arr.append(path)
        min_index = length_arr.index(min(length_arr))
        min_path = path_arr[min_index]
        sol_edge = sol_edge.union(set(min_path))
        sol_node.append(current_t)

    # compute the objective value
    obj = 0
    for edge in sol_edge:
        obj += g[edge[0]][edge[1]]['weight']

    return list(sol_edge), obj


def steiner_tree_lb(g, t_list):
    """
    Find the lower bound of Steiner tree problem
    :param g: given graph (networkx.Graph)
    :param t_list: terminal list (list)
    :return: lower bound of Steiner tree problem (double)
    """
    # find d_min(K)
    min_length = np.infty
    for index1 in range(len(t_list)):
        t1 = t_list[index1]
        for index2 in range(index1 + 1, len(t_list)):
            t2 = t_list[index2]
            length = nx.shortest_path_length(g, source=t1, target=t2, weight='weight')
            if min_length >= length:
                min_length = length
    # computer lower bound
    lb = min_length / 2 * len(t_list)

    return lb
