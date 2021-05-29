# Is Strongly Connected Success
# Simplified version
import random

from collections import defaultdict


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

    def print_adj_list(self):
        for node in self.start_point:  # node= destination
            # print("List  : ", node, "->", self.adj_list[node])
            print(node, "-> [", end=" ")
            for x, y in zip(self.adj_list[node], self.weight[node]):
                if y != self.weight[node][-1]:
                    print("(", x, ",", y, "),", end=" ")
                else:
                    print("(", x, ",", y, ")", end=" ")
            print("]")

    def DFS(self, s):
        # Initially mark all vertices as not visited
        visited = defaultdict()
        for i in self.start_point:
            visited[i] = False

        # Create a stack for DFS
        stack = []

        # Push the current source node.
        stack.append(s)

        print("Start from node: ", s)

        while len(stack):
            # Pop a vertex from stack and print it
            s = stack[-1]  # The top value of the stack
            stack.pop()

            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if not visited[s]:
                visited[s] = True

            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.adj_list[s]:
                if not visited[node]:
                    stack.append(node)

        for node in visited:
            if not visited[node]:
                return False
            return True

    def isSC(self, listY):
        listX = listY
        for x in listX:
            if not self.DFS(x):
                return False

        return True

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

nodes = ["RI", "SE", "JK", "HU", "KH"]
graph = Graph(nodes, True)
# graph.print_adj_list()

for u, v, w in default_edges:  # Default edge
    graph.add_edge(u, v, w)
# for u, v, w in other_edges:  # Default edge
#     graph.add_edge(u, v, w)

print(graph.isSC(nodes))
