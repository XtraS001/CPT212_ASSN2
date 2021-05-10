import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main():
    # Create a Digraph and add the nodes
    G = nx.DiGraph()
    G.add_node("RI", pos=(1.5, 5))  # 1. Riyadh, Saudi Arabia (RI)
    G.add_node("JK", pos=(3.2, 6.3))  # 2. Jakarta, Indonesia (JK)
    G.add_node("HU", pos=(2.3, 1.3))  # 3. Houston, United States (HU)
    G.add_node("SE", pos=(4.6, 1.7))  # 4. Seoul, South Korea (SE)
    G.add_node("KH", pos=(5, 5))  # 5. Khartoum, Sudan (KH)

    # add edges between the nodes
    G.add_edge("RI", "JK", weight=7349)
    G.add_edge("RI", "HU", weight=12733)
    # G.add_edge("RI", "SE", weight=7549)
    # G.add_edge("RI", "SE", weight=1792)
    # G.add_edge("JK", "HU", weight=16511)
    # G.add_edge("JK", "SE", weight=5294)
    G.add_edge("JK", "KH", weight=8527)
    G.add_edge("HU", "SE", weight=11328)
    # G.add_edge("HU", "KH", weight=12492)
    G.add_edge("SE", "KH", weight=9340)

    # draw using networkx
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # save it as an image and show it
    plt.savefig("random.png")
    plt.show()


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("Graph")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


# Window
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
main()
