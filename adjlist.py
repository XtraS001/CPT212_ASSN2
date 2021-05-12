class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_an_edge(self, src, dest):
        # Adding node to the source node
        node = AdjNode(dest)
        node.next = self.graph[dest]
        self.graph[src] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_an_edge(0, 1)
    graph.add_an_edge(0, 1)
    graph.add_an_edge(0, 2)
    graph.add_an_edge(1, 3)
    graph.add_an_edge(3, 4)
    graph.add_an_edge(0, 3)
    graph.add_an_edge(0, 1)

    graph.print_graph()
