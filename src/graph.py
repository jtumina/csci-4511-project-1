class Vertex:
    def __init__(self, node, square_id):
        self.id = node
        self.square_id = square_id
        self.adj = {}

    def add_neighbor(self, neighbor, weight):
        self.adj[neighbor] = weight

    def __str__(self):
        s = ""
        for v in self.adj:
            s += self.id + " --(" + str(self.adj[v]) + ")--> " + v.id + "\n"
        return s

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, square_id):
        self.nodes[node] = Vertex(node, square_id)

    def add_edge(self, src, dst, weight):
        self.nodes[src].add_neighbor(self.nodes[dst], weight)
        self.nodes[dst].add_neighbor(self.nodes[src], weight)

    def __str__(self):
        s = ""
        for v in self.nodes:
            s += str(self.nodes[v])
        return s
