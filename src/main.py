from graph import * 
from random import random

def rand():
    return int(random() * 11 + 1)

g = { "a" : ["c"],
      "b" : ["c", "e"],
      "c" : ["a", "b", "d", "e"],
      "d" : ["c"],
      "e" : ["c", "b"],
      "f" : []
    }

graph = Graph()

graph.add_node("a", rand())
graph.add_node("b", rand())
graph.add_node("c", rand())
graph.add_node("d", rand())
graph.add_node("e", rand())
graph.add_node("f", rand())

graph.add_edge("a", "c", rand())

graph.add_edge("b", "c", rand())
graph.add_edge("b", "e", rand())

graph.add_edge("c", "d", rand())
graph.add_edge("c", "e", rand())

graph.add_edge("d", "e", rand())

print(graph)

