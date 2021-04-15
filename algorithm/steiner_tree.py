import networkx as nx
import numpy as np
import itertools


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
    # compute pairwise length
    length_set = {}
    dataset = itertools.combinations(set(t_list), 2)
    for data in dataset:
        length_set[(min(data[0], data[1]), max(data[0], data[1]))] = nx.shortest_path_length(
            g, source=data[0], target=data[1], weight='weight')

    # iterate over K
    lb_all_subset = []
    for s in range(2, len(t_list) + 1):
        dataset = itertools.combinations(set(t_list), s)
        for data in dataset:
            # find d_min(K)
            min_length = np.infty
            data_list = list(data)
            for index1 in range(len(data_list)):
                t1 = data_list[index1]
                for index2 in range(index1 + 1, len(data_list)):
                    t2 = data_list[index2]
                    length = length_set[(min(t1, t2), max(t1, t2))]
                    if min_length >= length:
                        min_length = length
            lb_all_subset.append(min_length / 2 * len(data_list))
    # computer lower bound
    lb = max(lb_all_subset)

    return lb
