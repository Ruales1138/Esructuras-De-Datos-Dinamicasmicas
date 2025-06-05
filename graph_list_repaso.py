class Graph:
    def __init__(self):
        self.adj_list = {}
        self.size = 0
        self.nonweight_value = 0
        self.relation_value = 1

    def add_vertex(self, vertex_value):
        if vertex_value in self.adj_list:
            return
        self.adj_list[vertex_value] = []
        self.size += 1

    def add_edge(self, vertex_1, vertex_2, weight = None, directed = True):
        if vertex_1 not in self.adj_list:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.adj_list:
            self.add_vertex(vertex_2)
        if not directed:
            if vertex_1 not in self.adj_list[vertex_2]:
                self.adj_list[vertex_2].append((vertex_1, weight))
        if vertex_2 not in self.adj_list[vertex_1]:
            self.adj_list[vertex_1].append((vertex_2, weight))

    # BFS (Breadth-First Search)
    # Visitar todos los nodos de un grafo nivel por nivel, comenzando desde un nodo origen.

    def BFS(self, start):
        if start not in self.adj_list:
            return
        visited = []
        to_visit = [(start, 0)]
        while to_visit:
            current_tuple = to_visit.pop(0)
            current = current_tuple[0]
            if current not in visited:
                visited.append(current)
                to_visit.extend(self.adj_list[current])
        return visited
    
    # DFS (Depth-First Search)
    # Visitar todos los nodos de un grafo siguiendo un camino lo más profundo posible, antes de retroceder.

    def DFS(self, current, visited = []):
        if current not in self.adj_list:
            return
        if visited == []:
            visited.append(current)
        neighbors = self.adj_list[current]
        for neighbor in neighbors:
            if neighbor[0] not in visited:
                visited.append(neighbor[0])
                self.DFS(neighbor[0], visited)
        return visited
    
    def GS(self, node): # Grados de salida
        count = 0
        for _ in self.adj_list[node]:
            count += 1
        return count
    
    def GE(self, node): # Grados de entrada
        count = 0
        for item in self.adj_list:
            for tuple in self.adj_list[item]:
                if tuple[0] == node:
                    count += 1
        return count
    
    def delete(self, node):
        self.adj_list.pop(node)
        for item in self.adj_list:
            for tuple in self.adj_list[item]:
                if tuple[0] == node:
                    self.adj_list[item].remove(tuple)

    def group_counter(self):
        visited = []
        count = 0
        for item in self.adj_list:
            if item not in visited:
                count += 1
                visited_2 = self.DFS(item, [])
                visited.extend(visited_2)
        return count
    
    def shortest_route(self, start, end):
        if start not in self.adj_list or end not in self.adj_list:
            return []
        parent_map = {start: None}
        queue = [start]
        while queue:
            current = queue.pop(0)
            if current == end:
                path = []
                while current is not None:
                    path.insert(0, current)
                    current = parent_map[current]
                return path
            for ch in self.adj_list[current]:
                if ch[0] not in parent_map:
                    parent_map[ch[0]] = current
                    queue.append(ch[0])
        return []
    
    def calculate_routes(self, start, end, current = None, visited = [], paths = [], count = 0):
        if start not in self.adj_list or end not in self.adj_list:
            return []
        if current is None:
            current = start
        if visited == []:
            visited.append(current)
        if current == end:
            copy = visited.copy()
            paths.append((copy, count))
            return
        neighbors = self.adj_list[current]
        for neighbor in neighbors:
            if neighbor[0] not in visited:
                visited.append(neighbor[0])
                count += neighbor[1]
                self.calculate_routes(start, end, neighbor[0], visited, paths, count)
                visited.pop()
                count -= neighbor[1]
        return paths
                
        


    def __repr__(self):
        return str(self.adj_list)


g = Graph()
g.add_edge(1,3,2)
g.add_edge(2,10,1)
g.add_edge(3,1,6)
g.add_edge(4,6,8)
g.add_edge(1,4,2)
g.add_edge(10,1,20)
g.add_edge(10,3,9)
g.add_edge(3,2,1)
g.add_edge(11,9,12)
g.add_edge(10,6,9)
print(g)
print(g.BFS(1))
print(g.DFS(1))
print(g.GS(10))
print(g.GE(6))
# g.delete(1)
# print(g)
print(g.group_counter())
print(g.shortest_route(1, 6))
print(g.calculate_routes(1, 6))