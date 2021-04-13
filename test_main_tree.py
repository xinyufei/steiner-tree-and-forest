import random
import numpy as np
import networkx as nx
from import_data import read_data
from algorithm.steiner_tree import steiner_tree, steiner_tree_lb


if __name__ == '__main__':
    # create graph (g) and terminal list (t_list) from the data file.
    file_name = "b01.stp"
    g, t_list = read_data("data/B/" + file_name, mode='tree')
    # g, pair_list = read_data("data/B/b01.stp", mode="forest")
    # read_data("data/ES10FST/es10fst01.stp")
    # print(list(g.nodes))
    # for (u, v, wt) in g.edges.data('weight'):
    #     print((u, v, wt))
    # print(t_list)
    # print(pair_list)
    # print(nx.shortest_path(g, source=1, target=47, weight='weight'),
    #       nx.shortest_path_length(g, source=1, target=47, weight='weight'))

    # randomly generate order of t_list
    origin_t_list = t_list.copy()     # copy as the original list
    result_file = open("result/" + file_name.split('.')[0] + ".log", "w+")
    random_seed = 0
    num_instances = 5
    obj_list = []
    for i in range(num_instances):
        t_list = origin_t_list.copy()
        random.seed(random_seed)
        random.shuffle(t_list)
        print("instance ", i, file=result_file)
        print("terminal list with order", t_list, file=result_file)
        sol_edge, obj = steiner_tree(g, t_list)
        obj_list.append(obj)
        print("solution edge set", sol_edge, file=result_file)
        print("objective value", obj, file=result_file)
        random_seed += 1
    print("average objective value", np.mean(obj_list), file=result_file)
    print("standard deviation of objective value", np.std(obj_list), file=result_file)
    print("lower bound", steiner_tree_lb(g, t_list), file=result_file)

