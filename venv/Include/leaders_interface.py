from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QTableWidget, QPushButton
from PyQt5.QtCore import QSize


class LeadersInterface:
    def __init__(self, main_window, leaders):
        self.leaders = leaders
        self.main_window = main_window
        self.main_window.setWindowTitle("Go")
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.main_window.setFixedSize(600, 500)
        self.main_window.setCentralWidget(self.centralwidget)
        self.show_board()

    def show_board(self):
        self.table_score = QTableWidget(self.centralwidget)
        self.table_score.setGeometry(QtCore.QRect(25, 25, 570, 450))
        self.table_score.setRowCount(10)
        self.table_score.setColumnCount(2)
        self.table_score.setHorizontalHeaderLabels(('Best scores', ''))
        i = -1
        j = -2
        for line in self.leaders:
            i += 1
            j += 1
            name = QtWidgets.QTableWidgetItem(str(line[1]))
            name.setFlags(QtCore.Qt.ItemIsSelectable |
                          QtCore.Qt.ItemIsEnabled)
            name.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.table_score.setItem(i, 1, name)
            self.table_score.setColumnWidth(i, 265)

            score = QtWidgets.QTableWidgetItem(str(line[0]))
            score.setFlags(QtCore.Qt.ItemIsSelectable |
                          QtCore.Qt.ItemIsEnabled)
            score.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.table_score.setItem(j, 2, score)
            self.table_score.setColumnWidth(j, 265)
