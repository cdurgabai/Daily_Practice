class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_mat = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edges(self, u, v):
        self.adj_mat[u][v] = 1
        self.adj_mat[v][u] = 1

    def display(self):
        print("Adjacency Matrix:")
        for row in self.adj_mat:
            print(row)

graph = Graph(4)
graph.add_edges(0, 1)
graph.add_edges(0, 2)
graph.add_edges(1, 2)
graph.add_edges(2, 3)
graph.display()


#list
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display_adj_list(self):
        print("Adjacency List:")
        for vertex, neighbors in self.adj_list.items():
            print(vertex, ":", neighbors)

graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

graph.display_adj_list()
