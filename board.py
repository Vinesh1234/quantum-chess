# from pieces import *
# from player import *
import pieces
import player

class Board:
    def __init__(self, player_white, player_black):
        #TODO: initilize with custom position (just for fun)
        self.position = self._set_default()

        self._history = []

        # self.white and self.black may be quite confusing
        if isinstance(player_white, str):
            self.white = Player(player_white, player.Color.WHITE)
        elif isinstance(player_white, player.Player):
            self.white = player_white
        else:
            raise AssertionError("Argument at position 0 should be either type \'str\' or \'Player\'")

        if isinstance(player_black, str):
            self.black = Player(player_black, player.Color.BLACK)
        elif isinstance(player_black, player.Player):
            self.black = player_black
        else:
            raise AssertionError("Argument at position 1 should be either type \'str\' or \'Player\'")

        self.to_move = self.white

        self._game_over = False

    def get_player_move(self):
        return self.to_move.get_move(self)

    def validate_move(self, move):
        assert isinstance(move, player.Move)
        piece = self.get_piece(move.start.row, move.start.col)
        return piece != 'o' and piece.color is self.to_move.color and piece.is_legal(move, self)

    def make_move(self, move):
        #TODO
        """Called when the move has been validated"""


        self._history.append(move)
        return


    def _set_default(self):
        # unfortunately python doesn't have real 2D lists
        board = [[pieces.Rook(0,0), pieces.Knight(0,1), pieces.Bishop(0,2), pieces.Queen(0,3),
            pieces.King(0,4), pieces.Bishop(0,5), pieces.Knight(0,6), pieces.Rook(0,7)]]
        board.append([pieces.Pawn(1,i) for i in range(8)])
        board.extend([['o' for _ in range(8)] for __ in range(4)])
        board.append([pieces.Pawn(6,i,player.Color.BLACK) for i in range(8)])
        board.append([pieces.Rook(7,0,player.Color.BLACK), pieces.Knight(7,1,player.Color.BLACK),
            pieces.Bishop(7,2,player.Color.BLACK), pieces.Queen(7,3,player.Color.BLACK),
            pieces.King(7,4,player.Color.BLACK), pieces.Bishop(7,5,player.Color.BLACK),
            pieces.Knight(7,6,player.Color.BLACK), pieces.Rook(7,7,player.Color.BLACK)])
        return board

    def get_piece(self, row, col):
        return self.position[row][col]

    def move_piece(self, move):
        #TODO
        """updates row, col, and superpositions of the piece"""
        return

    def switch_turn(self):
        if self.to_move == self.white:
            self.to_move = self.black
        else:
            self.to_move = self.white

    @property
    def in_progress(self):
        return not self._game_over

    def print_board(self, rotate=False):
        #TODO: rotate: whether the board is flipped. default: white on top
        board_string = "  a b c d e f g h\n"
        for i in range(7, -1, -1):
            board_string += str(i+1) + " "
            for j in range(0, 8):
                board_string += str(self.get_piece(i, j))
                if j == 7:
                    board_string += "\n"
                else:
                    board_string += " "
        print(board_string)

class Coordinate:
    def __init__(self, row, col):
        assert type(row) is type(col)
        if isinstance(row, int):
            self.row = row
            self.col = col
        elif isinstance(row, str):
            self.row = int(row) - 1
            self.col = ord(col) - 97
        else:
            raise TypeError("Use either Integer or String format")
