from enum import Enum
from board import Board

class Color(Enum):
    WHITE = True
    BLACK = False

class Move:
    def __init__(self, move):
        # move is a string of the format rowcol-rowcol[q]
        self.start
        self.end
        self._quantum

    def __str__(self):
        #TODO: algebraic notation
        return

class Player:
    def __init__(self, color=Color.WHITE):
        # add whatever characteristics you want
        # e.g. name, rating, etc.
        self._side = color

    def get_move(self, board):
        #get the user input

        # while move is not valid
        #  . . .

        return # move
