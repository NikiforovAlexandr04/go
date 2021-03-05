import sys
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QMainWindow
from buttons_interface import Buttons
from field import Field
from leaders import Leaders


class Game(QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        self.mainWindow = self
        self.move_white = True
        self.interface = Buttons(self.mainWindow)
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.button_click)
        self.update_timer.start(100)
        self.game_load = False
        self.field = Field()
        self.timer_passes = QtCore.QTimer()
        self.timer_passes.timeout.connect(self.click_pass)
        self.old_passes = 0
        self.leaders = Leaders()
        self.t_pressed = False
        self.first_move = True

    def button_click(self):
        if self.interface.field != 0:
            self.first_move = False
            self.update_timer.stop()
            self.field.board_size = self.interface.field
            self.field.current_state = self.field.field_game()
            self.field.redraw(self.mainWindow)
            self.interface = self.field.interface
            self.game_load = True
            self.timer_passes.start(100)

    def mousePressEvent(self, event):
        if self.game_load:
            if event.button() == Qt.Qt.LeftButton:
                if self.field.press_key(event.x(), event.y(), self.move_white):
                    self.field.redraw(self.mainWindow)
                    self.old_passes = 0
                    if self.move_white:
                        self.move_white = False
                    else:
                        self.move_white = True

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_T:
            if not self.t_pressed:
                self.t_pressed = True
                self.game_load = False
                self.leaders.show_leader_board(self.mainWindow)
            else:
                self.t_pressed = False
                self.game_load = True
                if self.first_move:
                    self.interface = Buttons(self.mainWindow)
                else: self.field.redraw(self.mainWindow)

    def click_pass(self):
        if self.field.interface.passes - self.old_passes != 0:
            if self.move_white:
                self.move_black = True
            else:
                self.move_white = True
        if self.field.interface.passes == 2:
            self.end_game()

    def end_game(self):
        self.update_timer.stop()
        self.field.capture()
        self.field.total_count()
        self.field.end_game = True
        self.field.redraw(self.mainWindow)
        self.game_load = False


def main():
    app = QtWidgets.QApplication(sys.argv)
    game = Game()
    game.setObjectName("mainWindow")
    game.show()
    app.exec_()


if __name__ == '__main__':
    main()