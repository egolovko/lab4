import networkx as nx 

N = 15
V = 20
K = 5

FILE_PATH = "./graph.txt"

def _build(n_components):
    res_graph = nx.Graph()
    for i in range(n_components+1):
        res_graph = nx.disjoint_union(res_graph, nx.complete_graph(i))
    return res_graph

g = _build(K)

print(g.number_of_nodes() == N, g.number_of_edges() == V, len(list(nx.connected_components(g))) == K)

nx.write_adjlist(g, FILE_PATH)