# Python code to create a graph using adjacency list representation

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # for undirected graph

    def print_graph(self):
        for i in range(self.num_vertices):
            print(f"Adjacency list of vertex {i}: {self.adj_list[i]}")

# Create a graph with 5 vertices
g = Graph(5)

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Print the graph
g.print_graph()



