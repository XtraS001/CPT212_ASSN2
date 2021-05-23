# Python program to check if a given directed graph is strongly
# connected or not
# Done and worked

from collections import defaultdict

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

# -----------------------subGraph for function 1&2 uses---------------------------
def subGraph(mainGraph):
    graphC = defaultdict(list)

    for i in mainGraph.start_point:
        for j in mainGraph.adj_list[i]:
            graphC[i].append(j)

    return graphC

# -----------------------Strongly Connected Checking--------------------------

# A function used by isSC() to perform DFS
def DFSUtil(graph, v, visited):

    # Mark the current node as visited
    visited[v] = True

    # Recur for all the vertices adjacent to this vertex
    for i in graph[v]:
        if visited[i] == False:
            DFSUtil(i, visited)

# Function that returns reverse (or transpose) of this graph
def getTranspose(graph):

    g = defaultdict(list)

    # Recur for all the vertices adjacent to this vertex
    for i in graph:
        for j in graph[i]:
            g.addEdge(j, i)

    return g

# The main function that returns true if graph is strongly connected
def isSC(graph):

    # Step 1: Mark all the vertices as not visited (For first DFS)
    visited = [False] * 5   # 5 = number of vertices

    # Step 2: Do DFS traversal starting from first vertex.
    DFSUtil(graph, 0, visited)

    # If DFS traversal doesnt visit all vertices, then return false
    if any(i == False for i in visited):
        return False

    # Step 3: Create a reversed graph
    gr = getTranspose()

    # Step 4: Mark all the vertices as not visited (For second DFS)
    visited = [False] * 5    # 5 = number of vertices

    # Step 5: Do DFS for reversed graph starting from first vertex.
    # Staring Vertex must be same starting point of first DFS
    gr.DFSUtil(graph, 0, visited)

    # If all vertices are not visited in second DFS, then
    # return false
    if any(i == False for i in visited):
        return False

    return True


graph2 = subGraph(graph1)
print(isSC(graph2))     # True = strongly connected





