import checkers_board as cb
import random


class Computer(cb.CheckersBoard):
    def __init__(self, desk):
        super().__init__()
        self.color = 'O'  # Computer playing with black figures
        self.desk = desk
        self.what_to_move = None
        self.where_to_move = None

    def find_all_computer_figures(self):
        obj_list = []
        for l_inx, lst in enumerate(self.desk):
            for i, v in enumerate(lst):
                if self.color in v:
                    obj_list.append([l_inx+1, i])
        return obj_list

    def check_correct_move(self, x, y):
        # print(x, y)
        error_list = []  # 0 is False, 1 is True.
        theoretical_possible_moves = [x-1, [y-1, y+1]]
        possible_moves = []  # here will be contain the right moves
        for i in range(1, 3):
            test_pos = None
            if i == 1:
                test_pos = [theoretical_possible_moves[0], theoretical_possible_moves[1][0]]
            elif i == 2:
                test_pos = [theoretical_possible_moves[0], theoretical_possible_moves[1][1]]

            try:
                if 'O' in self.desk[test_pos[0]][test_pos[1]]:
                    # print('!Error, you can not put the two figures one square')
                    error_list.append(0)
            except IndexError:
                # print('!You went out of the field.')
                error_list.append(0)

            if test_pos[0] == 0 or test_pos[1] == 0:  # Checking for the exit from the field
                # print('!You went out of the field.')
                error_list.append(0)

            try:
                beat = None
                if '0' in self.desk[test_pos[0]][test_pos[1]]:
                    # print('Прийдется бить')
                    beat = True
                    if 'O' in self.desk[test_pos[0] - 1][test_pos[1] - 1 if i == 1 else test_pos[1] + 1] \
                            or '0' in self.desk[test_pos[0] - 1][test_pos[1] - 1 if i == 1 else test_pos[1] + 1] \
                            or ' ' in self.desk[test_pos[0] - 1][test_pos[1] - 1 if i == 1 else test_pos[1] + 1]:
                        # print('The figure is covered.')
                        error_list.append(0)
                        beat = False
            except IndexError:
                # print("Can't go outside the field")
                beat = False
                error_list.append(0)

            if 0 not in error_list and not beat:
                possible_moves.append([test_pos[0], test_pos[1]])
            elif 0 not in error_list and beat:
                possible_moves.append([test_pos[0]-1,
                                       test_pos[1] - 1 if i == 1 else test_pos[1] + 1,
                                      'beat'])
            error_list.clear()

        return possible_moves if possible_moves else False

    def rearrange_the_checker(self, start_x, start_y, end_x, end_y, beat=False):
        # print(f'S_x = {start_x}\nS_y = {start_y}\nE_x = {end_x}\nE_y = {end_y}\nBeat = {beat}')
        empty, checker = '|||', '|O|'
        self.desk[start_x][start_y] = empty
        self.desk[end_x][end_y] = checker
        if beat:
            self.desk[int(start_x - 1)][int((start_y + end_y)/2)] = empty

        print('-------Computer Turn-------\n', self.desk,
              f'Computer made his move: {start_x, start_y} -> {end_x, end_y}', beat, end='\n')

    def move(self):
        """Computer running. We check for possible moves,
        choose a random one and move on. If there are none,the player wins."""

        all_figures = self.find_all_computer_figures()  # Creating a list with coordinates of computer shapes
        available_moves, random_figure = [], None
        search = True

        while search:
            if len(all_figures) == 1:
                search = False

            random_figure = random.choice(all_figures)  # Select a random shape from the list, then remove it from it
            all_figures.remove(random_figure)
            x_pos, y_pos = random_figure[0], random_figure[1]
            moves = self.check_correct_move(x=x_pos, y=y_pos)  # List with correct moves
            if moves:
                available_moves.append([[x_pos, y_pos], moves])
        else:
            if not available_moves:
                print('The computer has no moves left. You won!')
                return

        for moves in available_moves:  # We choose the first of the available moves.
            for move in moves:         # Beat a checker in priority
                for item in move:
                    try:
                        if 'beat' in item:
                            start = [moves[0][0], moves[0][1]]
                            end = [moves[1][0][0], moves[1][0][1]]
                            self.rearrange_the_checker(start_x=start[0], start_y=start[1],
                                                       end_x=end[0], end_y=end[1], beat=True)
                            return
                    except TypeError:
                        continue
        else:
            start = available_moves[0][0]
            end = available_moves[0][1][0]
            self.rearrange_the_checker(start_x=start[0], start_y=start[1],
                                       end_x=end[0], end_y=end[1])
