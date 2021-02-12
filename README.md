# CSCI 4511 - Project 1: Search Algorithms
### Author: Jack Umina

## Uninformed Search

For uninformed search I implemented **Uniform Cost Search**. In sorting nodes in the priority queue there is no heuristic used. Nodes are instead sorted soley based on their distance from the source node.

## Informed Search

For informed search, I implemented **A\* Search**. In this algorithm nodes are sorted by a priority that's based on their distance from source plus the heuristic. My heuristic uses manhattan distance that's also multiplied by a constant of 100 to give more range to the heuristic's output.

## Usage
##### Running the script:
```
python3 src/main.py "<path/to/file/with/graph/data>"
```
#### Formatting the graph data files:
Text files containing the data for the graph *must* be formatted as follows:
```
# Vertices
# Vertex ID, Square ID
<vertex_id>, <square_id>

# Edges
# From, To, Distance
<source>, <target>, <distance>

# Source and Destination
S, <source vertex_id>
D, <destination vertex_id>
```
