from enum import Enum
from board import Board

class Color(Enum):
    WHITE = True
    BLACK = False

class Player:
    def __init__(self, color=Color.WHITE):
        self.side = color

    def move(self, board):
        #get the user input
        continue
