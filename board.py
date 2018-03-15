from pieces import *
from player import Color, Move, Player

class Board:
    def __init__(self, player_white, player_black):
        #TODO: initilize with custom position (just for fun)
        self.position = self._set_default()
        self.to_move = player_white

        self._game_over = False

    def validate_move(self, move):
        return self.position[move.start[0], move.start[1]].is_legal(move, self)

    def _set_default(self):
        # unfortunately python doesn't have real 2D lists
        board = [[], [], [], [], [], [], [], []]

        # . . . fill the board with pieces

        return board

    def print_board(self, rotate=False):
        #TODO: rotate: whether the board is flipped. default: white on top
        board_string = " a b c d e f g h"
        for i in range(0, 8):
            board_string += str(i) + " "
            for j in range(0, 8):
                board_string += str(self.position[i][j])
                if j == 7:
                    board_string += "\n"
                else:
                    board_string += " "
        print(board_string)
