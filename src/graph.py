class Vertex:
    def __init__(self, node, block_num):
        self.name = node
        self.block_num = block_num
        self.adj = {}

    def add_neighbor(self, neighbor, weight):
        self.adj[neighbor] = weight

    def __str__(self):
        s = ""
        for v in self.adj:
            s += self.name + " --(" + str(self.adj[v]) + ")--> " + v.name + "\n"
        return s

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, block_num):
        self.nodes[node] = Vertex(node, block_num)

    def add_edge(self, src, dst, weight):
        self.nodes[src].add_neighbor(self.nodes[dst], weight)
        self.nodes[dst].add_neighbor(self.nodes[src], weight)

    def __str__(self):
        s = ""
        for v in self.nodes:
            s += str(self.nodes[v])
        return s
