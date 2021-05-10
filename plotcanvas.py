import networkx as nx
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# By inheriting the FigureCanvas class,
# this class is both a PyQt5 Qwidget and a Matplotlib FigureCanvas,
# which is the key to connecting pyqt5 and matplotlib
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=351, height=331, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        default_graph = self.default_nodes_edges()
        modified_graph = self.add_an_edge(default_graph, "RI", "SE", 7549)
        self.plot(modified_graph)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def default_nodes_edges(self):
        gr = nx.DiGraph()
        gr.add_node("RI", pos=(1.5, 5))  # 1. Riyadh, Saudi Arabia (RI)
        gr.add_node("JK", pos=(3.2, 6.3))  # 2. Jakarta, Indonesia (JK)
        gr.add_node("HU", pos=(2.3, 1.3))  # 3. Houston, United States (HU)
        gr.add_node("SE", pos=(4.6, 1.7))  # 4. Seoul, South Korea (SE)
        gr.add_node("KH", pos=(5, 5))  # 5. Khartoum, Sudan (KH)

        # add edges between the nodes
        gr.add_edge("RI", "JK", weight=7349)
        gr.add_edge("RI", "HU", weight=12733)
        # G.add_edge("RI", "SE", weight=7549)
        # G.add_edge("RI", "SE", weight=1792)
        # G.add_edge("JK", "HU", weight=16511)
        # G.add_edge("JK", "SE", weight=5294)
        gr.add_edge("JK", "KH", weight=8527)
        gr.add_edge("HU", "SE", weight=11328)
        # G.add_edge("HU", "KH", weight=12492)
        gr.add_edge("SE", "KH", weight=9340)
        return gr

    def add_an_edge(self, gr, node_from, node_to, weight):
        gr.add_edge(node_from, node_to, weight=weight)
        return gr

    def plot(self, gr):
        pos = nx.get_node_attributes(gr, 'pos')
        nx.draw(gr, pos, node_color='w', ax=self.axes,
                edge_color='b', with_labels=True, alpha=1,
                font_size=15, node_size=500, arrows=True)
