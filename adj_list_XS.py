
class Graph:
    def __init__(self,start_input, is_directed=False):
        self.start_point = start_input  # A,B,C,D An array
        self.adj_list = {}
        self.weight = {}
        self.is_directed = is_directed

        for node in self.start_point:
            self.adj_list[node] = []    #Create array to store Destination for that node
            self.weight[node] = []      #Create array to store weight

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

    def print_adj_list(self):
        for node in self.start_point:   # node= destination
            # print("List  : ", node, "->", self.adj_list[node])
            print(node, "-> [", end=" ")
            for x, y in zip(self.adj_list[node], self.weight[node]):
                if y != self.weight[node][-1]:
                    print("(", x, ",", y, "),", end=" ")
                else:
                    print("(", x, ",", y, ")", end=" ")
            print("]")

all_edges = {
    ("A", "B", 1), ("A", "C", 2), ("B", "D", 3), ("C", "D", 4), ("C", "E", 5), ("D", "E", 6), ("E", "A", 7)
}

default_edges = {
    ("RI", "JK", 7349), ("RI", "HU", 12733),("JK", "KH", 8527), ("HU", "SE", 11328), ("SE", "KH", 9340)
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

for u, v, w in default_edges:
    graph.add_edge(u, v, w)

# graph.del_edge("C", "B", 1)
# graph.del_edge("A", "B", 1)
graph.print_adj_list()