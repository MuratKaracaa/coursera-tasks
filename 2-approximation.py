import networkx as nx

G = nx.erdos_renyi_graph(n=5, p=1)


def approximation(g):
    mst = nx.minimum_spanning_tree(g)
    pre_ordered = list(nx.dfs_preorder_nodes(mst, 0))
    double_edged_mst = nx.Graph()

    visited = set()
    for idx, node in enumerate(pre_ordered):
        if idx != len(pre_ordered) - 1:
            double_edged_mst.add_edge(node, pre_ordered[idx + 1])
            double_edged_mst.add_edge(pre_ordered[idx + 1], node)

    new_edges = double_edged_mst.edges()
    path = []

    for idx, (v1, v2) in enumerate(new_edges):
        if len(path) == 0:
            path.append(v1)
            path.append(v2)
            visited.add(v1)
            visited.add(v2)
        else:
            if v2 not in visited:
                path.append(v2)
                visited.add(v2)
            else:
                shortened = next(x for x in list(new_edges)[idx] if x[0] == v2)
                path.append(shortened[1])
                visited.add(shortened[1])

    result = 0

    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + g[path[i]][path[0]]['weight']
        else:
            result = result + g[path[i]][path[i + 1]]['weight']

    return result
