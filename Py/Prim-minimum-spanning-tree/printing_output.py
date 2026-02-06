def print_mst_edges(mst_edges):
    for from_node, to_node, weight in mst_edges:
        print(f"{from_node} -- {to_node} : {weight}")
