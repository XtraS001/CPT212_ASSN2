# Test is Cycle
# Worked
from collections import defaultdict
import random


# ------------------My code (The Main Graph Class)--------------------------------
class Graph:

    def __init__(self, start_input, is_directed=False):
        self.start_point = start_input  # A,B,C,D An array
        self.adj_list = {}
        self.weight = {}
        self.is_directed = is_directed

        for node in self.start_point:
            self.adj_list[node] = []  # Create array to store Destination for that node
            self.weight[node] = []  # Create array to store weight

    def add_edge(self, u, v, w):
        self.adj_list[u].append(v)
        self.weight[u].append(w)

        if not self.is_directed:
            self.adj_list[v].append(u)
            self.weight[u].append(w)

# ------------------------Storing All the edges-------------------------------------
all_edges = {
    ("A", "B", 1), ("A", "C", 2), ("B", "D", 3), ("C", "D", 4), ("C", "E", 5), ("D", "E", 6), ("E", "A", 7)
}

default_edges = {
    ("RI", "JK", 7349), ("RI", "HU", 12733), ("JK", "KH", 8527), ("HU", "SE", 11328), ("SE", "KH", 9340)
}

other_edges = {
    ("RI", "SE", 7549), ("RI", "KH", 1792),
    ("JK", "RI", 7349), ("JK", "HU", 16511), ("JK", "SE", 5294),
    ("HU", "RI", 12733), ("HU", "JK", 16511), ("HU", "KH", 12492),
    ("SE", "RI", 7549), ("SE", "JK", 5294), ("SE", "HU", 11328),
    ("KH", "RI", 1792), ("KH", "JK", 8527), ("KH", "HU", 12492), ("KH", "SE", 9340)
}

# -----------------------Adding edges into Main Graph-------------------------------
nodes = ["RI", "SE", "JK", "HU", "KH"]
print(nodes)
graph1 = Graph(nodes, True)

for u, v, w in default_edges:  # Default edge
    graph1.add_edge(u, v, w)

# subGraph for function 1&2 uses
def subGraph(mainGraph):
    graphC = defaultdict(list)

    for i in mainGraph.start_point:
        for j in mainGraph.adj_list[i]:
            graphC[i].append(j)

    return graphC

# -----------------------Check cycle in Graph-----------------------------
def isCyclicUntil(graph, node, visited):
    if (visited[node]):
        return True

    visited[node] = True
    flag = False

    for j in graph[node]:
        flag = isCyclicUntil(graph, j, visited)

        if (flag):
            return True

    visited[node] = False

    return False


def isCycle(graph):
    visited = [False] * 5
    flag = False
    for i in range(5):

        visited[i] = True

        for j in graph[i]:
            flag = isCyclicUntil(graph, j, visited)

            if (flag):
                return True

        visited[i] = False

    return False

subGraph(graph1)
graphN = subGraph(graph1)
print(isCycle(graphN))