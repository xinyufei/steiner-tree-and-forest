from import_data import read_data
import networkx as nx

if __name__ == '__main__':
    # create graph (g) and terminal list (t_list) from the data file.
    g, t_list = read_data("data/B/b01.stp", mode='tree')
    g, pair_list = read_data("data/B/b01.stp", mode="forest")
    # read_data("data/ES10FST/es10fst01.stp")
    print(list(g.nodes))
    for (u, v, wt) in g.edges.data('weight'):
        print((u, v, wt))
    print(t_list)
    print(pair_list)
    print(nx.shortest_path(g, source=1, target=47, weight='weight'),
          nx.shortest_path_length(g, source=1, target=47, weight='weight'))
