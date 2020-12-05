import checkers_board


class Player(checkers_board.CheckersBoard):
    def __init__(self, desk):
        super().__init__()
        self.color = '0'
        self.desk = desk

    def check_correct_move(self, old_position, new_position):
        old_pos_list = [int(old_position[0]), int(old_position[2])]
        new_pos_list = [int(new_position[0]), int(new_position[2])]

        res_list = []  # 0 is False, 1 is True.

        if '0' not in self.desk[old_pos_list[0]][old_pos_list[1]] \
                or '___' in self.desk[new_pos_list[0]][new_pos_list[1]]:  # Figure selection error
            print('!The error in the choice of shapes.')
            res_list.append(0)

        if '0' in self.desk[new_pos_list[0]][new_pos_list[1]]:
            print('!Error, you can not put the two figures one square')
            res_list.append(0)

        if 'O' in self.desk[new_pos_list[0]][new_pos_list[1]]:
            beat = True
            beat_x, beat_y = new_pos_list[0]+1, new_pos_list[1] + (new_pos_list[1]-old_pos_list[1])
            try:
                if 'O' in self.desk[beat_x][beat_y]\
                        or '0' in self.desk[beat_x][beat_y]:
                    print('The figure is covered.')
                    beat = False
                    res_list.append(0)
            except IndexError:
                beat = False
                res_list.append(0)
                print("Can't go outside the field")

            if beat:
                new_pos_list = [beat_x, beat_y]

        return [old_pos_list, new_pos_list] if 0 not in res_list else False

    def move(self):
        old_pos = input('Select the figure (example: 2.4): ')
        new_pos = input('Where to go? (example: 3.5): ')

        if len(old_pos) + len(new_pos) < 6:
            print('!Input Error. Try again.')
            return False

        if int(new_pos[0]) <= 0 or int(new_pos[2]) <= 0 \
                or int(old_pos[2]) > 8 or int(old_pos[2]) > 8:  # Checking for the exit from the field
            print('!You went out of the field.')
            return False

        if not old_pos[0].isdigit() or not old_pos[2].isdigit() \
                or not old_pos[0].isdigit() or not old_pos[2].isdigit():
            print('!The error in the choice of figure. Try again.')
            return False

        check_the_move = self.check_correct_move(old_position=old_pos, new_position=new_pos)

        if not check_the_move:
            print('Your move is wrong, try again.')
            return False
        else:
            empty, checker = '|||', '|0|'
            self.desk[check_the_move[0][0]][check_the_move[0][1]] = empty
            self.desk[check_the_move[1][0]][check_the_move[1][1]] = checker
            if check_the_move[1][0] - check_the_move[0][0] == 2:
                self.desk[int(check_the_move[0][0] + 1)][int((check_the_move[0][1] + check_the_move[1][1]) / 2)] = empty
            print('---------Player move---------\n', self.desk)
            return True
