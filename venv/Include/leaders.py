from leaders_interface import LeadersInterface


class Leaders:
    def __init__(self):
        self.leaders = []
        self.fill_leader_board()

    def show_leader_board(self, main_window):
        self.fill_leader_board()
        self.leader_interface = LeadersInterface(main_window, self.leaders)

    def fill_leader_board(self):
        with open("leaders.txt") as file:
            file_contains = file.read()
        row = ""
        leaders_list = []
        for line in file_contains:
            if line == "\n":
                leaders_list.append(row)
                row = ""
                continue
            row += line
        leaders_list.append(row)
        self.leaders = []
        for line in leaders_list[0:10]:
            self.leaders.append([line.split(" ")[0], line.split(" ")[1]])
