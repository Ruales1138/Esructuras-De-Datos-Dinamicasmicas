class Graph:
    def __init__(self):
        self.adj_matrix: list[list[int]] = []
        self.nodes: list[int] = []
        self.size: int = 0
        self.nonweight_value = 0
        self.relation_value = 1

    def add_vertex(self, vertex_value):
        if vertex_value in self.nodes:
            return
        self.nodes.append(vertex_value)
        self.size += 1
        for row in self.adj_matrix:
            row.append(self.nonweight_value)   
        self.adj_matrix.append([self.nonweight_value] * self.size)

    def add_edge(self, vertex_1, vertex_2, directed = True, weight = None,):
        if vertex_1 not in self.nodes:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.nodes:
            self.add_vertex(vertex_2)
        pos_1 = self.nodes.index(vertex_1)
        pos_2 = self.nodes.index(vertex_2)
        relation_weight = self.relation_value if weight is None else weight
        if not directed:
            self.adj_matrix[pos_2][pos_1] = relation_weight
        self.adj_matrix[pos_1][pos_2] = relation_weight

    # DFS (Depth-First Search)
    # Visitar todos los nodos de un grafo siguiendo un camino lo más profundo posible, antes de retroceder.

    def DFZ(self, current, visited = []):
        pass

    def __repr__(self):
        repr_matrix = ""
        for row in self.adj_matrix:
            repr_matrix += str(row) + "\n"
        repr_matrix += f"\n{self.nodes}"
        return repr_matrix
        

g = Graph()
g.add_edge("H", "A")
g.add_edge("H", "O")
g.add_edge("O", "X")
g.add_edge("O", "A")
g.add_edge("O", "L")
g.add_edge("O", "O")
g.add_edge("L", "A")
g.add_edge("L", "Z")
g.add_edge("L", "O")
g.add_edge("X", "Y")
g.add_edge("Y", "U")
g.add_edge("Y", "S")
g.add_edge('I', 'R')
g.add_vertex('D')
print(g)