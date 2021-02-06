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

    def decrease_priority(queue, v, new_prio):
        for i in range(0, len(queue)):
            if queue[i][1] == v.id:
                queue[i] = (new_prio, v.id, v) 
                return True

        return False

    def dijkstra_uniformed_search(self, src, dst):
        # Check if src and dst exist in graph
        if src not in self.nodes or dst not in self.nodes:
            return None

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
            # The vertex id is neccessary to allow heapq to properly sort 
            # when multiple elementes share the same priority.
            heapq.heappush(q, (dist[v], v.id, v))

        while q:
            # Get the neighbor with least cost
            v = heapq.heappop(q)[2]

            # For each neighbor of v, check if there's a shorter path
            for u in v.adj: 
                new_path = dist[v] + float(u.adj[v])

                if new_path < dist[u]:
                    dist[u] = new_path
                    prev[u] = v
                    Graph.decrease_priority(q, u, new_path)

        # Construct the shortest path between src and dst
        path = []
        path_length = 0

        v = self.nodes[dst]
        path.append(v.id)

        while v.id != src:
            u = prev[v]
            path.append(u.id)
            path_length += int(v.adj[u])
            v = u

        path.reverse() 
        ret = {"path": path, "path_length": path_length}

        return ret 
