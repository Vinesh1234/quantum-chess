from enum import Enum
from board import Board

class Color(Enum):
    WHITE = True
    BLACK = False

class Move:
    def __init__(self, move):
        # move is a string of the format rowcol-rowcol
        self.start
        self.end

    def __repr__(self):
        # algebraic notation

class Player:
    def __init__(self, color=Color.WHITE):
        self.side = color

    def get_move(self, board):
        #get the user input

        # while move is not valid
        #  . . .

        # return move
