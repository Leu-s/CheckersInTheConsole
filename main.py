# ||| - Черная клетка, 0 - Черная фигура
# ___ - Белая клетка, О - Белая фигура
# По горизонтали ось Х; По вертикали ось Y. Отсчет от верхнего левого угла.
# Для хода нужно указать клетку, на которой стоит фигура, и клетку куда вы хотите её поставить
# Если вы собрались бить вражескую пешку, указывайте её позицию а не пустую клетку позади неё.
# Игрок играет 0 - черными.

import computer_logic as cl
import player_logic as pl
import checkers_board as board

my_desk = board.CheckersBoard()
# my_desk.start_game()

player = pl.Player(desk=my_desk)
computer = cl.Computer(desk=my_desk)


def start_game(plr, comp, dsk):
    dsk.start_game()
    print(dsk)
    running = True
    while running:
        correct = plr.move()
        if correct:
            comp.move()


if __name__ == '__main__':
    start_game(plr=player, comp=computer, dsk=my_desk)
