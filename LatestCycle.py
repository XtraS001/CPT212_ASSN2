import random
import heapq
from collections import defaultdict


class Graph:
    def __init__(self, start_input, is_directed=False):
        self.start_point = start_input  # A,B,C,D An array
        self.adj_list = {}
        self.weight = {}
        self.is_directed = is_directed
        self.isCycle = False
        self.queue = []

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

    def detectAlgo(self, num, pred, n, v):
        n += 1
        num[v] = n
        self.queue.append(v)

        for u in self.adj_list[v]:
            if num[u] == 0:
                pred[u] = v
                self.detectAlgo(num, pred, n, u)

            elif num[u] != 999:
                pred[u] = v
                stack2 = []
                stack3 = []
                print("Cycle start point:", u)
                for i in self.queue:
                    stack2.append(i)

                while stack2:
                    if stack2[-1] != u:
                        stack3.append(stack2.pop())
                    elif stack2[-1] == u:
                        stack3.append(stack2.pop())
                        break

                while stack3:
                    print(stack3.pop(), "->", end="")
                print(u)

                self.isCycle = True

        num[v] = 999
        self.queue.pop()
        return self.isCycle

    def cycleDetection(self):
        num = defaultdict()
        for i in self.start_point:
            num[i] = 0

        pred = defaultdict()
        for i in self.start_point:
            pred[i] = ""

        n = 0

        self.detectAlgo(num, pred, n, 'RI')

        if self.isCycle:
            print("Cycle Detected")
        else:
            print("Cycle Not Detected")

        print(" ")
        return self.isCycle

    def gen_Cycle(self):
        while not self.cycleDetection():
            self.add_random_edge(other_edges)
        self.print_adj_list()


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

graph.gen_Cycle()


