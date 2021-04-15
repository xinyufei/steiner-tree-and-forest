import random
import numpy as np
import time
import networkx as nx
from import_data import read_data
from algorithm.steiner_tree import steiner_tree, steiner_tree_lb


if __name__ == '__main__':
    # file_name_list = ["c01.stp", "c02.stp", "c03.stp", "c04.stp", "c05.stp", "c06.stp", "c07.stp", "c08.stp",
    #                   "c09.stp", "c10.stp", "c11.stp", "c12.stp", "c13.stp", "c14.stp", "c15.stp", "c16.stp",
    #                   "c17.stp", "c18.stp", "c19.stp", "c20.stp"]
    # file_name_list = ["b07.stp", "b08.stp",
    #                   "b09.stp", "b10.stp", "b11.stp", "b12.stp", "b13.stp", "b14.stp", "b15.stp", "b16.stp",
    #                   "b17.stp", "b18.stp"]
    file_name_list = ["es100fst01.stp", "es100fst02.stp", "es100fst03.stp", "es100fst04.stp", "es100fst05.stp",
                      "es100fst06.stp", "es100fst07.stp", "es100fst08.stp", "es100fst09.stp", "es100fst10.stp",
                      "es100fst11.stp", "es100fst12.stp", "es100fst13.stp", "es100fst14.stp", "es100fst15.stp"]
    for file_name in file_name_list:
        # create graph (g) and terminal list (t_list) from the data file.
        g, t_list = read_data("data/ES100FST/" + file_name, mode='tree')
        # print(steiner_tree_lb(g, t_list))
        # randomly generate order of t_list
        origin_t_list = t_list.copy()     # copy as the original list
        num_instances = 20
        result_file = open("result_tree/" + file_name.split('.')[0] + "_" + str(num_instances) + ".log", "w+")
        random_seed = 0
        obj_list = []
        for i in range(num_instances):
            t_list = origin_t_list.copy()
            random.seed(random_seed * 100)
            random.shuffle(t_list)
            print("instance ", i, file=result_file)
            print("terminal list with order", t_list, file=result_file)
            start = time.time()
            sol_edge, obj = steiner_tree(g, t_list)
            end = time.time()
            obj_list.append(obj)
            print("solution edge set", sol_edge, file=result_file)
            print("objective value", obj, file=result_file)
            print("computational time", end - start, file=result_file)
            random_seed += 1
        print("average objective value", np.mean(obj_list), file=result_file)
        print("max and min objective value", max(obj_list), min(obj_list), file=result_file)
        print("standard deviation of objective value", np.std(obj_list), file=result_file)
        print("theoretical competitive bound", 1 + np.log2(len(t_list)), file=result_file)
        # print("lower bound", steiner_tree_lb(g, t_list), file=result_file)
