# DFS (Depth-First Search)
# Visitar todos los nodos de un grafo siguiendo un camino lo más profundo posible, antes de retroceder.

# BFS (Breadth-First Search)
# Visitar todos los nodos de un grafo nivel por nivel, comenzando desde un nodo origen.

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
    
    def add_edge(self, vertex_1, vertex_2, directed = True):
        if vertex_1 not in self.adj_list:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.adj_list:
            self.add_vertex(vertex_2)
        if not directed:
            if vertex_1 not in self.adj_list[vertex_2]:
                self.adj_list[vertex_2].append(vertex_1)
        if vertex_2 not in self.adj_list[vertex_1]:
            self.adj_list[vertex_1].append(vertex_2)
            
    def BFS(self, start):
        if start not in self.adj_list:
            return
        visited = []
        to_visit = [start]
        while to_visit:
            current = to_visit.pop(0)
            if current not in visited:
                visited.append(current)
                to_visit.extend(self.adj_list[current])
        return visited
    
    def DFS(self, current, visited = []):
        if current not in self.adj_list:
            return
        if visited == []:
            visited.append(current)
        neighbors = self.adj_list[current]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                self.DFS(neighbor, visited) 
        return visited
    
    def GS(self, nodo):
        count = 0
        for num in self.adj_list[nodo]:
            count += 1
        return count
    
    def GE(self, nodo):
        count = 0
        for item in self.adj_list:
            for num in self.adj_list[item]:
                if num == nodo:
                    count += 1
        return count
    
    def delete(self, nodo):
        self.adj_list.pop(nodo)
        for item in self.adj_list:
            if nodo in self.adj_list[item]:
                self.adj_list[item].remove(nodo)
                
    def group_counter(self):
        visited_2 = []
        count = 0
        for item in self.adj_list:
            if item not in visited_2:
                count += 1
                visited = self.DFS(item, [])
                visited_2.extend(visited)
        return count
    
    def shortest_route(self, start, end):
        if start not in self.adj_list or end not in self.adj_list:
            return []
        parent_map = {start: None}
        queue = [start]
        while queue:
            current = queue.pop()
            if current == end:
                path = []
                while current is not None:
                    path.insert(0, current)
                    current = parent_map[current]
                return path
            for ch in self.adj_list[current]:
                if ch not in parent_map:
                    parent_map[ch] = current
                    queue.append(ch)
        return []
    
    def calculate_routes(self, start, end, current = None, visited = [], paths = []):
        if start not in self.adj_list or end not in self.adj_list:
            return []
        if current is None:
            current = start
        if visited == []:
            visited.append(current)
        neighbors = self.adj_list[current]
        if current == end:
            copY = visited.copy()
            paths.append(copY)
            return paths
            
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                self.calculate_routes(start, end, neighbor, visited) 
                visited.pop()
        return paths
        
    def __repr__(self):
        return str(self.adj_list)
        
    
g = Graph()

g.add_edge(1,3)
g.add_edge(2,10)
g.add_edge(3,1)
g.add_edge(4,6)
g.add_edge(1,4)
g.add_edge(10,1)
g.add_edge(10,3)
g.add_edge(3,2)
g.add_edge(11,9)
g.add_edge(10, 6)
print(g)
# print(g.BFS(1))
# print(g.DFS(1))
# print(g.GS(2))
# print(g.GE(1))
# g.delete(3)
# print(g)
# print(g.group_counter())
# print(g.shortest_route(1, 6))

print(g.calculate_routes(1,6))