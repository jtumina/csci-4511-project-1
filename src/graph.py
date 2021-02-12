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
        self.adj[neighbor] = int(weight)

    def __str__(self):
        s = ""
        for v in self.adj:
            s += self.id + " --(" + str(self.adj[v]) + ")--> " + v.id + "\n"
        return s

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, square_id):
        self.nodes[node] = Vertex(node, int(square_id))

    def add_edge(self, src, dst, weight):
        self.nodes[src].add_neighbor(self.nodes[dst], weight)
        self.nodes[dst].add_neighbor(self.nodes[src], weight)

    def __str__(self):
        s = ""
        for v in self.nodes:
            s += str(self.nodes[v])
        return s

    """
    Finds matching tuple and decreases priority.
    Assumes each element is a tuple formated as such:
        k(<priority>, <vertex_id>, <vertex_obj>)
    If tuple is not found, returns false
    """
    def decrease_priority(queue, v, new_prio):
        for i in range(0, len(queue)):
            if queue[i][1] == v.id:
                queue[i] = (new_prio, v.id, v) 
                return True

        return False

    def ucs_uninformed_search(self, src, dst):
        # Check if src and dst exist in graph
        if src not in self.nodes or dst not in self.nodes:
            return None

        # Get the vertex object of src and dst
        src = self.nodes[src]
        dst = self.nodes[dst]

        prev = {}
        prev[src] = None
        dist = {}
        dist[src] = 0
        num_explored_nodes = 0
        frontier = [] # Priority queque to maintain closed list
        visited = [] # List to track opened nodes 
        found = False

        # Each element of the queue is a 3 tuple.
        # The vertex id is neccessary to allow heapq to properly sort 
        # when multiple elementes share the same priority.
        heapq.heappush(frontier, (dist[src], src.id, src))

        while not found and frontier:
            # Get the neighbor with least cost
            v = heapq.heappop(frontier)[2]
            num_explored_nodes += 1

            if v.id == dst.id:
                found = True
                break

            visited.append(v)

            for u in v.adj:
                new_cost = dist[v] + u.adj[v]

                if u not in dist or new_cost < dist[u]:
                    dist[u] = new_cost
                    prev[u] = v

                    # If decrease_priority returns False, u is not in frontier
                    # so it must be added if it has not been visited
                    in_frontier = Graph.decrease_priority(frontier, u, new_cost)
                    if not in_frontier and u not in visited:
                        prev[u] = v
                        heapq.heappush(frontier, (dist[u], u.id, u))

        ret = self.construct_path(src, dst, prev) 
        ret["num_explored_nodes"] = num_explored_nodes

        return ret 

    def heuristic(self, v, dst):
        """
        Compute heuristic using manhattan distance. One's place of square_id
        represents x coordinate while ten's place represents y coordinate.
        Multiplying by 100 gives more range to the heuristic and usally
        produces quicker results. Subtracting by 100 also ensures that the
        heuristic will be admisable by constraining it to a square size.
        """
        dx = abs(dst.square_id % 10 - v.square_id % 10)
        dy = abs(dst.square_id // 10 - v.square_id // 10)

        return 100 * (dx + dy) - 100

    def a_star_informed_search(self, src, dst):
        # Check if src and dst exist in graph
        if src not in self.nodes or dst not in self.nodes:
            return None

        # Get the vertex object of src and dst
        src = self.nodes[src]
        dst = self.nodes[dst]

        prev = {} # Map to track a nodes previous in the path
        prev[src] = None
        dist = {} # Map to track a nodes distance to src so far
        dist[src] = 0
        frontier = [] # Priority queue to maintain closed list
        visited = [] # List to track opened nodes
        found = False
        num_explored_nodes = 0

        # Each element of the queue is a 3 tuple.
        # The vertex id is neccessary to allow heapq to properly sort 
        # when multiple elementes share the same priority.
        heapq.heappush(frontier, (dist[src], src.id, src))

        # While we haven't reached dst and there are still nodes to explore in
        # the frontier
        while not found and frontier:
            # Get the node with least cost
            v = heapq.heappop(frontier)[2]
            num_explored_nodes += 1
            
            if v.id == dst.id:
                found = True
                break
        
            visited.append(v)

            # For each neighbor of v, check if there's a shorter path
            for u in v.adj: 
                new_cost = dist[v] + u.adj[v]

                if u not in dist or new_cost < dist[u]:
                    dist[u] = new_cost
                    prev[u] = v

                    # If decrease_priority returns False, u is not in frontier 
                    # so it must be added if it has not been visited
                    priority = new_cost + self.heuristic(u, dst)
                    in_frontier = Graph.decrease_priority(frontier, u, priority)
                    if not in_frontier and u not in visited:
                        prev[u] = v
                        heapq.heappush(frontier, (priority, u.id, u))

        ret = self.construct_path(src, dst, prev) 
        ret["num_explored_nodes"] = num_explored_nodes

        return ret 

    # Construct the shortest path and return as list
    def construct_path(self, src, dst, prev):
        path = []
        path_length = 0

        v = dst
        path.append(v.id)

        while prev[v] and v.id != src.id:
            u = prev[v]
            path.append(u.id)
            path_length += int(v.adj[u])
            v = u

        path.reverse() 
        
        ret = {
                "path": path,
                "path_length": path_length
              }

        return ret 

