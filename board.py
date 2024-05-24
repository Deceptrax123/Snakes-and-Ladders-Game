# Create the board for the game
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def create_board(ladders, snakes):
    # Connect adjacent nodes
    adjacency_matrix = np.zeros((100, 100))

    # Create ladder and snake loops depending on board configuration
    n_ladders = ladders
    n_snakes = snakes

    print("Ladder Config")
    for i in range(n_ladders):
        low = int(input("Enter lowest point: "))
        high = int(input("Enter highest point: "))

        adjacency_matrix[low][high] = 1

    print("Snake Config")
    for i in range(n_snakes):
        head = int(input("Enter head point: "))
        tail = int(input("Enter tail point: "))

        adjacency_matrix[head][tail] = 1

    return adjacency_matrix
