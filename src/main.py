import sys
from graph import * 

def populate_graph(graph, filename):
    f = open(filename, "r")
    lines = f.readlines()
    count_hash = 0
    path_endpoints = []

    for line in lines:
        # Track when we reach a new section
        if line[0] == "#":
            count_hash += 1
            continue

        # Before node section
        if count_hash < 2:
            continue

        # Node section
        elif count_hash == 2:
            vals = line.lstrip().rstrip().split(",")
            if len(vals) == 2:
                graph.add_node(str(vals[0]), vals[1])
           
        # Edge Section
        elif count_hash == 4:
            vals = line.lstrip().rstrip().split(",")
            if len(vals) == 3:
                graph.add_edge(str(vals[0]), vals[1], vals[2])

        if count_hash == 5:
            vals = line.lstrip().rstrip().split(",")
            if len(vals) == 2:
                path_endpoints.append(str(vals[1]))

    if count_hash != 5:
        print("Error: Unable to create graph")
        return None
    else:
        return path_endpoints

if __name__ == "__main__":
    if len(sys.argv) < 2: 
        sys.exit("Incorrect arguments. Must provide filename of graph data.")

    graph = Graph()
    path_endpoints = populate_graph(graph, sys.argv[1])
    path = graph.dijkstra_uniformed_search(path_endpoints[0], path_endpoints[1])
    print(path)
