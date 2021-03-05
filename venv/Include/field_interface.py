from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QTableWidget, QPushButton
from PyQt5.QtCore import QSize


class Interface:
    def __init__(self, main_window, current_state, white_stones, black_stones, end_game, w_points, b_points):
        self.white_points = w_points
        self.black_points = b_points
        self.passes = 0
        self.white_stones = white_stones
        self.black_stones = black_stones
        self.current_state = current_state
        self.main_window = main_window
        self.main_window.setWindowTitle("Go")
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        points = self.current_state[len(self.current_state) - 1]
        self.size = points[len(points) - 1].x + 70
        self.main_window.setFixedSize(self.size, self.size + 100)
        if end_game:
            self.main_window.setFixedSize(self.size, self.size + 250)
            self.drow_end_widget(w_points, b_points)
        else:
            self.draw_pass_button()
        self.main_window.setCentralWidget(self.centralwidget)
        self.create_field()
        self.create_stones(self.black_stones, True)
        self.create_stones(self.white_stones, False)
        self.first_button_clicked = False
        self.second_button_clicked = False

    def create_field(self):
        for points in self.current_state:
            for point in points:
                point_label = QtWidgets.QLabel(self.centralwidget)
                point_label.setGeometry(point.x, point.y, 5, 5)
                point_label.setPixmap(QtGui.QPixmap("pictures/black.png"))
                point_label.setScaledContents(True)

    def create_stones(self, stones, is_black):
        for stone in stones:
            point_label = QtWidgets.QLabel(self.centralwidget)
            point_label.setGeometry(stone.x - 10, stone.y - 10, 25, 25)
            if is_black:
                point_label.setPixmap(QtGui.QPixmap("pictures/black.png"))
            else:
                point_label.setPixmap(QtGui.QPixmap("pictures/white.png"))
            point_label.setScaledContents(True)

    def drow_end_widget(self, black_points, white_points):
        self.score = QtWidgets.QLineEdit(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(self.size/2 - 150, self.size - 25, 300, 40))
        self.score.setReadOnly(True)
        if (white_points > black_points):
            self.score.setText("                  Game over! White wins")
        elif (white_points == black_points):
            self.score.setText("                  Game over! Dead heat")
        else: self.score.setText("                  Game over! Black wins")
        self.white_score = QtWidgets.QLineEdit(self.centralwidget)
        self.white_score.setGeometry(QtCore.QRect(30, self.size + 35, 140, 40))
        self.white_score.setReadOnly(True)
        self.white_score.setText("White points:   " + str(white_points))
        self.black_score = QtWidgets.QLineEdit(self.centralwidget)
        self.black_score.setGeometry(QtCore.QRect(self.size - 170, self.size + 35, 140, 40))
        self.black_score.setReadOnly(True)
        self.black_score.setText("Black points:   " + str(black_points))
        self.print_names()

    def draw_pass_button(self):
        first_button = QtWidgets.QPushButton("pass", self.centralwidget)
        first_button.setGeometry(self.size/2 - 50, self.size - 30, 70, 70)
        first_button.clicked.connect(self.click_pass)

    def click_pass(self):
        self.passes += 1

    def print_names(self):
        self.first_name = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name.setGeometry(QtCore.QRect(30, self.size + 90, 200, 30))
        self.first_name.setReadOnly(True)
        self.first_name.setText("Fill name white player!")
        self.write_first_name = QtWidgets.QLineEdit(self.centralwidget)
        self.write_first_name.setGeometry(QtCore.QRect(30, self.size + 130, 200, 30))
        self.second_name = QtWidgets.QLineEdit(self.centralwidget)
        self.second_name.setGeometry(QtCore.QRect(30, self.size + 170, 200, 30))
        self.second_name.setReadOnly(True)
        self.second_name.setText("Fill name black player!")
        self.write_second_name = QtWidgets.QLineEdit(self.centralwidget)
        self.write_second_name.setGeometry(QtCore.QRect(30, self.size + 210, 200, 30))
        self.first_button = QPushButton("Edit", self.centralwidget)
        self.first_button.setGeometry(250, self.size + 130, 30, 30)
        self.first_button.clicked.connect(self.edit_first_name)
        self.second_button = QPushButton("Edit", self.centralwidget)
        self.second_button.setGeometry(250, self.size + 210, 30, 30)
        self.second_button.clicked.connect(self.edit_second_name)

    def edit_first_name(self):
        if not self.first_button_clicked:
            text = self.write_first_name.text()
            self.write_first_name.setReadOnly(True)
            self.first_button_clicked = True
            self.write_scores(text, self.white_points)

    def edit_second_name(self):
        if not self.second_button_clicked:
            text = self.write_second_name.text()
            self.write_second_name.setReadOnly(True)
            self.second_button_clicked = True
            self.write_scores(text, self.black_points)

    def write_scores(self, name, points):
        scores_file_read = open('leaders.txt', 'r')
        scores = []
        for line in scores_file_read:
            scores.append([int(line.split(" ")[0]), line.split(" ")[1]])
        scores_file_read.close()
        if len(scores) == 10 and points > int(scores[-1][0]):
            del scores[-1]
            scores.append([int(points), name + "\n"])
        scores.sort(key=lambda x: x[0], reverse=True)
        scores_file_write = open('leaders.txt', 'w')
        scores_file_write.truncate()
        for score in scores:
            scores_file_write.write(str(score[0]) + " " + score[1])
        scores_file_write.close()
