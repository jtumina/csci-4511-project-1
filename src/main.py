import sys
from graph import * 
import time

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

    # Run both searches n times
    n = 1000

    # Uniformed search
    t_sum = 0
    for _ in range(n):
        t_start = time.time()
        ret_uninformed = graph.dijkstra_uninformed_search \
            (path_endpoints[0], path_endpoints[1])
        t_sum += time.time() - t_start

        # If endpoints are not in graph, break
        if ret_uninformed == None:
            break
  
    # Get average time from n iterations, convert to milliseconds 
    t_uninformed = t_sum / n * 1000 

    # Informed search
    t_sum = 0
    for _ in range(n):
        t_start = time.time()
        ret_informed = graph.a_star_informed_search \
            (path_endpoints[0], path_endpoints[1])
        t_sum += time.time() - t_start

        # If endpoints are not in graph, break
        if ret_informed == None:
            break
  
    # Get average time from n iterations, convert to milliseconds 
    t_informed = t_sum / n * 1000 

    if ret_uninformed and ret_informed:
        print("Uninformed search using Dijkstra's algorithm:" \
                + "\nShortest path: " + str(ret_uninformed["path"]) \
                + "\nLength: " + str(ret_uninformed["path_length"]) \
                + "\nAverage time over " + str(n) + " iterations: " \
                + str(t_uninformed) + " ms")
        print("\nInformed search using A* search algorithm:" \
                + "\nShortest path: " + str(ret_informed["path"]) \
                + "\nLength: " + str(ret_informed["path_length"]) \
                + "\nAverage time over " + str(n) + " iterations: " \
                + str(t_informed) + " ms")
    else:
        print("Error: Either soure or destination is not in graph")

