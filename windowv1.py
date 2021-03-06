# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowv1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout

from plotcanvas import PlotCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = PlotCanvas(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 90, 351, 331))
        self.widget.setObjectName("widget")

        self.Edge_Title = QtWidgets.QLabel(self.centralwidget)
        self.Edge_Title.setGeometry(QtCore.QRect(420, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Edge_Title.setFont(font)
        self.Edge_Title.setObjectName("Edge_Title")
        self.comboBoxFrom = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxFrom.setGeometry(QtCore.QRect(440, 100, 73, 22))
        self.comboBoxFrom.setObjectName("comboBoxFrom")
        self.comboBoxFrom.addItem("")
        self.comboBoxFrom.addItem("")
        self.comboBoxFrom.addItem("")
        self.comboBoxFrom.addItem("")
        self.comboBoxFrom.addItem("")
        self.comboBoxTo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTo.setGeometry(QtCore.QRect(560, 100, 73, 22))
        self.comboBoxTo.setObjectName("comboBoxTo")
        self.comboBoxTo.addItem("")
        self.comboBoxTo.addItem("")
        self.comboBoxTo.addItem("")
        self.comboBoxTo.addItem("")
        self.comboBoxTo.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 100, 31, 16))
        self.label.setObjectName("label")
        self.pushButton_addEdge = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addEdge.setGeometry(QtCore.QRect(670, 100, 93, 28))
        self.pushButton_addEdge.setObjectName("pushButton_addEdge")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_addEdge.clicked.connect(self.pressed)
        # self.widget.setParent(None)
        print("yes")
        # self.widget = PlotCanvas(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Edge_Title.setText(_translate("MainWindow", "Add An Edge"))
        self.comboBoxFrom.setItemText(0, _translate("MainWindow", "RI"))
        self.comboBoxFrom.setItemText(1, _translate("MainWindow", "JK"))
        self.comboBoxFrom.setItemText(2, _translate("MainWindow", "HU"))
        self.comboBoxFrom.setItemText(3, _translate("MainWindow", "SE"))
        self.comboBoxFrom.setItemText(4, _translate("MainWindow", "KH"))
        self.comboBoxTo.setItemText(0, _translate("MainWindow", "RI"))
        self.comboBoxTo.setItemText(1, _translate("MainWindow", "JK"))
        self.comboBoxTo.setItemText(2, _translate("MainWindow", "HU"))
        self.comboBoxTo.setItemText(3, _translate("MainWindow", "SE"))
        self.comboBoxTo.setItemText(4, _translate("MainWindow", "KH"))
        self.label.setText(_translate("MainWindow", "to"))
        self.pushButton_addEdge.setText(_translate("MainWindow", "Add"))

    def pressed(self):
        node_from = self.comboBoxFrom.currentText()
        node_to = self.comboBoxTo.currentText()
        print(node_to)
        #PlotCanvas.add_an_edge(PlotCanvas, node_from, node_to, 5000)
        #PlotCanvas.add_an_edge(PlotCanvas, PlotCanvas.get_graph(), node_from, node_to, 5000)
        # PlotCanvas.test(PlotCanvas)
        #PlotCanvas.add_an_edge(PlotCanvas, PlotCanvas.get_graph(PlotCanvas), node_from, node_to, weight=100)
        #self.widget = PlotCanvas(self.centralwidget)
        self.widget.get_graph().add_edge(node_from, node_to, weight=100)
        # self.widget.get_graph().update()
        # PlotCanvas.plot(self, PlotCanvas.get_graph(self))
        self.widget = PlotCanvas(self.centralwidget)
        print("test")

    def update_graph(self):
        self.widget = PlotCanvas(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
