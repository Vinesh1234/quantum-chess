# imports from other .py files
# from board import Board
# from player import Player, Color
import board
import player


def main():
    """
    Eventually we should have a TKinter GUI, but for now the user(s) will play
    the game through the terminal.
    This is the way this function should run:
    1. print board
    2.1. ask for player's move while the inputed move is not legal
    2.2. player can choose between a 'normal' and a 'quantum' move
    3. make the move, switch turn, go to 1.
    """

    p1 = player.Player(name="p1", color=player.Color.WHITE)
    p2 = player.Player(name="p2", color=player.Color.BLACK)
    game = board.Board(p1, p2)

    while game.in_progress:
        game.make_move(game.get_player_move())
        game.print_board()


if __name__ == "__main__":
    main()
