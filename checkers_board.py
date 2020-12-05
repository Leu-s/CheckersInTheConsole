class CheckersBoard:
    def __init__(self):
        self._cursor = 0
        self.desk = [['XY', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 '],
                     [' 1 ', '___', '|||', '___', '|||', '___', '|||', '___', '|||'],
                     [' 2 ', '|||', '___', '|||', '___', '|||', '___', '|||', '___'],
                     [' 3 ', '___', '|||', '___', '|||', '___', '|||', '___', '|||'],
                     [' 4 ', '|||', '___', '|||', '___', '|||', '___', '|||', '___'],
                     [' 5 ', '___', '|||', '___', '|||', '___', '|||', '___', '|||'],
                     [' 6 ', '|||', '___', '|||', '___', '|||', '___', '|||', '___'],
                     [' 7 ', '___', '|||', '___', '|||', '___', '|||', '___', '|||'],
                     [' 8 ', '|||', '___', '|||', '___', '|||', '___', '|||', '___']]

    def start_game(self):
        """We place the checkers in their original positions."""
        self.desk.__str__()
        white, black = 'O', '0'
        for p in (1, 2, 3, 6, 7, 8):
            for i, j in enumerate(self.desk[p]):
                s = list(self.desk[p][i])
                if i != 0 and i % 2 == 0 and p in (1, 3) or \
                        p == 2 and i % 2 != 0:
                    s[1] = black
                    self.desk[p][i] = ''.join(s)
                elif i != 0 and i % 2 != 0 and p in (6, 8) or \
                        p == 7 and i % 2 == 0:
                    s[1] = white
                    self.desk[p][i] = ''.join(s)
                else:
                    self.desk[7][0] = ' 7 '
        return self.desk

    def __str__(self):
        string = ''
        for i in self.desk:
            for j in i:
                string += j
            else:
                string += '\n'
        return string

    def __next__(self):
        if self._cursor + 1 >= len(self.desk):
            self._cursor = 0
            raise StopIteration()
        self._cursor += 1
        return self.desk[self._cursor]

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self.desk[item]
