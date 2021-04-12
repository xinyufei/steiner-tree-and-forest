import networkx as nx


def read_data(file_name):
    dataset = []
    file = open(file_name, mode='r')
    for line in file:
        line = line.strip('\n')
        line = line.split(' ')
        if line[0] != '':
            dataset.append(line)
    file.close()

    # create the graph and the terminal list
    g = nx.Graph()
    t_list = []
    for data in dataset:
        if data[0] == 'Nodes':
            g.add_nodes_from([i + 1 for i in range(int(data[1]))])
        if data[0] == 'E':
            g.add_edge(int(data[1]), int(data[2]), weight=float(data[3]))
        if data[0] == 'T':
            t_list.append(int(data[1]))

    # print(list(g.nodes), list(g.edges), t_list)
    return g, t_list
