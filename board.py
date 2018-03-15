from pieces import *
from player import Color, Player

class Board:
    def __init__(self, player_white, player_black):
        #TODO: initilize with custom position (just for fun)
        self.position = self._set_default()
        self.to_move = player_white

    def validate_move(self, move):
        return self.position[move.start[0], move.start[1]].is_legal(move, self)

    def _set_default(self):
        # unfortunately python doesn't have real 2D lists
        board = [[], [], [], [], [], [], [], []]
        # . . . fill the board with pieces
        return board

    def print_board(self, rotate=False):
