# CSCI 4511 - Project 1: Search Algorithms

## Uninformed Search

For uninformed search I implemented Uniform Cost Search. In sorting nodes in the priority queue there is no heuristic used. Nodes are instead sorted soley based on their distance from the source node.

## Informed Search

For informed search, I implemented A\* search. In this algorithm nodes are sorted by a priority that's based on their distance from source plus the heuristic. My heuristic uses manhattan distance that's also multiplied by a constant of 100 to give more range to the heuristic's output.

## Usage
You can run the script with the following command:

```
python3 src/main.py "<name of file with graph data>"
```

## Benchmarks


