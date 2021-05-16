
class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes  # A,B,C,D
        self.adj_list = {}
        self.weight = {}
        self.is_directed = is_directed

        for node in self.nodes:
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
        for node in self.nodes:
            print("List  : ", node, "->", self.adj_list[node])
            print("Weight: ", node, "->", self.weight[node])

all_edges = {
    ("A", "B", 1), ("A", "C", 2), ("B", "D", 3), ("C", "D", 4), ("C", "E", 5), ("D", "E", 6)
}


nodes = ["A", "B", "C", "D", "E"]
graph = Graph(nodes, True)
# graph.print_adj_list()

for u, v, w in all_edges:
    graph.add_edge(u, v, w)

graph.print_adj_list()