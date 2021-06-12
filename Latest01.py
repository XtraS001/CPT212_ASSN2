# Latest Graph class
import random
import heapq
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

    def del_edge(self, u, v, w):
        self.adj_list[u].remove(v)
        self.weight[u].remove(w)

        if not self.is_directed:
            self.adj_list[v].remove(u)
            self.weight[v].remove(w)

    def degree(self, node):
        deg = len(self.adj_list[node])
        return deg

    def super_add(self, u, v, w):  # ONLY Add edge that doesnt exist
        num = 0
        for i in self.adj_list[u]:
            if i != v:
                num += 1

        if num == len(self.adj_list[u]):
            self.adj_list[u].append(v)
            self.weight[u].append(w)

    def super_del(self, u, v, w):  # ONLY Delete edge that exist
        for i in self.adj_list[u]:
            if i == v:
                self.adj_list[u].remove(v)
                self.weight[u].remove(w)

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

    def add_random_edge(self, rand_edges):
        a, b, c = random.choice(list(rand_edges))
        graph.super_add(a, b, c)
        print("(", a, ",", b, ",", c, ") is randomly generated and added")

    def DFS(self, s):
        # Initially mark all vertices as not visited
        visited = defaultdict()
        for i in self.start_point:  #start_point = all nodes
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

    def isSC(self):
        # listX = listY
        for x in self.start_point:
            if not self.DFS(x):
                return False

        return True

    def gen_SC(self, other_edge):
        while not self.isSC():
            self.add_random_edge(other_edge)

# function 3
def shortest_path(source, destination):
    queue = [(0, source, [])]  # initialize a priority queue
    visited = set()  # create hash set to store visited node
    heapq.heapify(queue)  # create heap priority queue (this can pop the smallest value)
    # traverse graph with BFS
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        # visit the node that has not been visited before
        if node not in visited:
            visited.add(node)
            path = path + [node]
            # if the node is the destination
            if node == destination:
                return cost, path
            # visit neighbours
            for c, neighbour in zip(graph.weight[node], graph.adj_list[node]):
                if neighbour not in visited:
                    heapq.heappush(queue, (cost+c, neighbour, path))
    # if the destination is not reachable, add random edge until it does
    add_random_edge(other_edges)  # this function is a global function and other edges are global dict (may need to fix)
    return shortest_path(source, destination)

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
for u, v, w in default_edges:
    graph.add_edge(u, v, w)
graph.print_adj_list()


