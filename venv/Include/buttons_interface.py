import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QTableWidget, QPushButton
from PyQt5.QtCore import QSize
from functools import partial


class Buttons():
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.setWindowTitle("Go")
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.main_window.setObjectName("MainWindow")
        self.main_window.setFixedSize(600, 600)
        self.main_window.setCentralWidget(self.centralwidget)
        self.main_window.setStyleSheet("background-color:#808080;")
        self.field = 0
        self.create_button()

    def create_button(self):
        first_button = QtWidgets.QPushButton("9x9", self.centralwidget)
        first_button.setGeometry(100, 300, 100, 100)

        second_button = QtWidgets.QPushButton("13x13", self.centralwidget)
        second_button.setGeometry(250, 300, 100, 100)

        third_button = QtWidgets.QPushButton("15x15", self.centralwidget)
        third_button.setGeometry(400, 300, 100, 100)

        widget = QtWidgets.QLineEdit(self.centralwidget)
        widget.setGeometry(50, 100, 500, 100)
        widget.setReadOnly(True)
        widget.setStyleSheet("font-size: 27px;")
        widget.setText("    Select the size of the playing field")

        first_button.clicked.connect(partial(self.select_size, 9))
        second_button.clicked.connect(partial(self.select_size, 13))
        third_button.clicked.connect(partial(self.select_size, 15))

    def select_size(self, number: int):
        self.field = number
