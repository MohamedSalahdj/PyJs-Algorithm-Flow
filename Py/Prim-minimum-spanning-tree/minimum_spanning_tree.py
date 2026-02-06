class MinimumSpanningTree:
    def __init__(self, nodes, graph):
        self.nodes = nodes
        self.graph = graph
        self._num_nodes = len(nodes)
        self._num_selected_edges = 0
        self._selected = [False] * self._num_nodes
        self._selected[0] = True
        self._mst_edges = []

    def _get_min_edge(self):
        while self._num_selected_edges < self._num_nodes - 1:
            minimum_weight = float('inf')
            temp_from = -1
            temp_to = -1
            for i in range(self._num_nodes):
                if self._selected[i]:
                    for j in range(self._num_nodes):
                        if not self._selected[j] and self.graph[i][j] > 0 and self.graph[i][j] < minimum_weight:
                            minimum_weight = self.graph[i][j]
                            temp_from = i
                            temp_to = j
            self._selected[temp_to] = True
            self._num_selected_edges += 1
            self._mst_edges.append((self.nodes[temp_from], self.nodes[temp_to], minimum_weight))
