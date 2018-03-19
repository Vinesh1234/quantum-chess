from enum import Enum
from board import Board

class Color(Enum):
    WHITE = True
    BLACK = False

class Move:
    def __init__(self, move):
        # move is a string of the format rowcol-rowcol[q]
        assert isinstance(move, str)
        # could also initialize from [Coordinate, Coordinate, Bool]
        self.move = move
        self.start = Coordinate(move[0], move[1])
        self.end = Coordinate(move[3], move[4])
        self._quantum = len(move) > 5

    def __str__(self):
        #TODO: algebraic notation
        return self.move

class Player:
    def __init__(self, name="Player", color=Color.WHITE):
        # add whatever characteristics you want
        # e.g. name, rating, etc.
        assert isinstance(name, str)
        assert isinstance(color, Color)
        self.name = name
        self.color = color

    def get_move(self, board):
        #get the user input
        # while not board.validate_move( . . .)

        return # Move(move)
