from field_interface import Interface
from stone import Stone
from math import fabs


class Field():
    def __init__(self):
        self.black_stones = []
        self.white_stones = []
        self.board_size = 0
        self.current_state = []
        self.white_points = 0
        self.black_points = 0
        self.white = []
        self.black = []
        self.white_firts = True
        self.end_game = False

    def redraw(self, main_window):
        self.interface = Interface(main_window, self.current_state, self.white_stones, self.black_stones,
                                   self.end_game, self.black_points, self.white_points)

    def field_game(self):
        field = []
        x = 50
        y = 50
        for i in range(self.board_size):
            field.append([])
            for j in range(self.board_size):
                field[i].append(Stone(x, y, "n"))
                x += 30
            x = 50
            y += 30
        return field

    def press_key(self, x, y, move_white):
        for stones in self.current_state:
            for stone in stones:
                if fabs(stone.x - x) < 10 and fabs(stone.y - y) < 10 and stone.color == 'n':
                    free_stones = self.make_list_free_stones()
                    capture_black = self.if_capture([(stone.x - 20) / 30 - 1, (stone.y - 20) / 30 - 1],
                                                    free_stones, self.black)
                    capture_white = self.if_capture([(stone.x - 20) / 30 - 1, (stone.y - 20) / 30 - 1],
                                                    free_stones, self.white)
                    if move_white:
                        stone.color = "w"
                        self.white_points += 1
                        self.white_stones.append(stone)
                    else:
                        stone.color = "b"
                        self.black_points += 1
                        self.black_stones.append(stone)
                    return True
        return False

    def capture(self):
        state = self.current_state
        for stone in self.white_stones:
            self.white.append([(stone.x - 20) / 30 - 1, (stone.y - 20) / 30 - 1])
        for stone in self.black_stones:
            self.black.append([(stone.x - 20) / 30 - 1, (stone.y - 20) / 30 - 1])
        for stone in self.white:
            if self.if_capture(stone, self.white, self.black):
                self.black_points += 1
        for stone in self.black:
            if self.if_capture(stone, self.black, self.white):
                self.white_points += 1

    def if_capture(self, stone, white, black):
        self.is_free = True
        self.queue_next_stones = []
        self.visited_points = []
        self.queue_next_stones.append(stone)
        while len(self.queue_next_stones) > 0:
            stone = self.queue_next_stones[0]
            if stone in self.visited_points:
                self.queue_next_stones.remove(stone)
                continue
            self.make_capture_query(stone, white, black)
        return self.is_free

    def make_capture_query(self, stone, white, black):
        if not stone in white and not stone in black: self.is_free = False
        if stone[0] != 0:
            if not [stone[0] - 1, stone[1]] in black:
                self.queue_next_stones.append([stone[0] - 1, stone[1]])
        if stone[0] != self.board_size - 1:
            if not [stone[0] + 1, stone[1]] in black:
                self.queue_next_stones.append([stone[0] + 1, stone[1]])
        if stone[1] != 0:
            if not [stone[0], stone[1] - 1] in black:
                self.queue_next_stones.append([stone[0], stone[1] - 1])
        if stone[1] != self.board_size - 1:
            if not [stone[0], stone[1] + 1] in black:
                self.queue_next_stones.append([stone[0], stone[1] + 1])
        self.visited_points.append(stone)
        self.queue_next_stones.remove(stone)

    def make_list_free_stones(self):
        free_stones = []
        for stones in self.current_state:
            for stone in stones:
                if stone.color == "n":
                    free_stones.append([(stone.x - 20) / 30 - 1, (stone.y - 20) / 30 - 1])
        return free_stones

    def total_count(self):
        free_stones = self.make_list_free_stones()
        for stone in free_stones:
            if self.if_capture(stone, free_stones, self.white):
                self.white_points += 1
            if self.if_capture(stone, free_stones, self.black):
                self.black_points += 1
