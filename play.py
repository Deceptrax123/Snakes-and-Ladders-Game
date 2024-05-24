import numpy as np
from board import create_board
from game import game

if __name__ == '__main__':
    print("Welcome to yee-haw snake and ladders game. Played when bored i guess :((")
    print("Terminal based game to increase suffering aaah")
    print("For creating the board, follow instructions to enter ladder and snake positions. Configure number of ladders and snakes directly in source below")
    print("Game indexing starts at 0")

    board = create_board(ladders=8, snakes=8)  # Create custom board.

    game(board)  # Play Game
