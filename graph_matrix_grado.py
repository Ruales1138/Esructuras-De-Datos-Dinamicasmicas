# DFS (Depth-First Search)
# Visitar todos los nodos de un grafo siguiendo un camino lo más profundo posible, antes de retroceder.

# BFS (Breadth-First Search)
# Visitar todos los nodos de un grafo nivel por nivel, comenzando desde un nodo origen.

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
        
    def add_edge(self, vertex_1, vertex_2, directed = True, weight: int = None):
        if vertex_1 not in self.nodes:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.nodes:
            self.add_vertex(vertex_2)
        pos_v1 = self.nodes.index(vertex_1)
        pos_v2 = self.nodes.index(vertex_2)
        relation_weight = self.relation_value if weight is None else weight
        if directed is False:
            self.adj_matrix[pos_v2][pos_v1] = relation_weight
        self.adj_matrix[pos_v1][pos_v2] = relation_weight
        
    def DFZ(self, current, visited = []):
        if current not in self.nodes:
            return
        if visited == []:
            visited.append(current)
        current_pos = self.nodes.index(current)
        neighbors = self.adj_matrix[current_pos]
        for idx, n in enumerate(neighbors):
            if n == self.relation_value:
                if self.nodes[idx] in visited:
                    continue
                visited.append(self.nodes[idx])
                self.DFZ(self.nodes[idx], visited)
        return visited
    
    def GS(self, node): # Grado de salida
        pos = self.nodes.index(node)
        neighbors = self.adj_matrix[pos]
        count = 0
        for idx, n in enumerate(neighbors):
            if n == self.relation_value:
                count += 1
        return count
    
    def GE(self, node): # Grado de entrada
        pos = self.nodes.index(node)
        count = 0
        for fila in self.adj_matrix:
            if fila[pos] == self.relation_value:
                count += 1
        return count
    
    def delete(self, node):
        pos = self.nodes.index(node)
        for fila in self.adj_matrix:
            fila.pop(pos)
        self.nodes.pop(pos)
        self.adj_matrix.pop(pos)
        
    def group_counter(self):
        visited_2 = []
        count = 0
        for item in self.nodes:
            if item not in visited_2:
                count += 1
                visited = self.DFZ(item, [])
                visited_2.extend(visited)  
        return count
        
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
print('------------------')
# print(g.GS('O'))
# print(g.GE('O'))
# g.delete('O')
# print(g)
# print(g.DFZ('Y', []))
# print(g.DFZ('H', []))

print(g.group_counter())