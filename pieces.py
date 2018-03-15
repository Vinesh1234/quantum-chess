from player import Color

class Piece:
    def __init__(self, row, col, color=Color.WHITE):
        self._row = row
        self._col = col
        self._side = color

        self._superpositions = [] # this will store the piece's possible locations

    def is_legal(self, move, board):
        # each child class will define its own version of is_legal
        pass


class King(Piece):
    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    def is_legal(self, move, board):


class Queen(Piece):
    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    def is_legal(self, move, board):


class Rook(Piece):
    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    def is_legal(self, move, board):


class Bishop(Piece):
    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    def is_legal(self, move, board):


class Knight(Piece):
    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    def is_legal(self, move, board):


class Pawn(Piece):
    def __init__(self, row, col, color=Color.WHITE):
        super().__init__(row, col, color)

    def is_legal(self, move, board):
