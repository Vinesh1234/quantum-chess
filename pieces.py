from player import Color, Move
from board import Board

class Piece:
    def __init__(self, row, col, color=Color.WHITE):
        assert isinstance(row, int)
        assert isinstance(col, int)
        assert isinstance(color, Color)
        self._row = row
        self._col = col
        #could (should?) initilize row and col with Coordinate
        self.color = color

        self._superpositions = [] # this will store the piece's possible locations

    def is_legal(self, move, board):
        # each child class will define its own version of is_legal
        pass

    def __repr__(self):
        if self.color.value:
            return self.piece_type
        else:
            return self.piece_type.lower()


class King(Piece):
    piece_type = 'K'

    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    #def is_legal(self, move, board):


class Queen(Piece):
    piece_type = 'Q'

    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    #def is_legal(self, move, board):


class Rook(Piece):
    piece_type = 'R'

    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    #def is_legal(self, move, board):


class Bishop(Piece):
    piece_type = 'B'

    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    #def is_legal(self, move, board):


class Knight(Piece):
    piece_type = 'N'

    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    # def is_legal(self, move, board):
    #     if abs(move.end.row - move.start.row) == 1 and
    #             abs(move.end.col - move.start.col) == 2:


class Pawn(Piece):
    piece_type = 'P'

    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    #def is_legal(self, move, board):
