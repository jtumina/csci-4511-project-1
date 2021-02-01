import heapq
import math

class Vertex:
    def __init__(self, node, square_id):
        """
        Track the nodes id, its block number and its adjaceny list.
        Adjaceny list is a dictionary where the the key is an adjacent node
        and the value is the weight of the edge between them.
        """
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

    def dijkstra_uniformed_search(self, src, dst):
        prev = {}
        dist = {}
        dist[self.nodes[src]] = 0

        # Priority queque
        q = []

        for v in self.nodes.values():
            if v.id != src:
                # Distance between src and v is unknown
                dist[v] = math.inf
                prev[v] = None

            # Each element of the queuque is a 3 tuple.
            # The vertex id is neccessary to allow heapq to properly sort when
            # multiple elementes share the same priority.
            heapq.heappush(q, (dist[v], v.id, v))

        while q:
            # Get the neighbor with least cost
            v = heapq.heappop(q)[2]

            # For each neighbor of v, check if there's a shorter path
            for u in v.adj: 
                new_path = dist[u] + float(v.adj[u])

                if new_path < dist[v]:
                    dist[v] = new_path
                    prev[v] = u
                    # Decrease u's priority

        # Construct the shortest path between src and dst
        path = []
        v = self.nodes[dst]
        while v.id != src:
            v = prev[v]
            path.append(v.id)

        return path
