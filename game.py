import numpy as np
import random
from board import create_board
import time


def roll_dice():
    choices = [1, 2, 3, 4, 5, 6]

    roll = random.choice(choices)

    return roll


def check(temp_index, adj_matrix):
    for row in range(100):
        if adj_matrix[temp_index][row] == 1:
            if row < temp_index:
                print("Oops snake encountered...")
            else:
                print("Yayyy thats a ladder.....")
            return row
    print("Normal Move")
    return -1


def move(idx, roll, adj_matrix):
    temp_idx = idx+roll
    perm_idx = check(temp_idx, adj_matrix)

    if perm_idx == -1:
        perm_idx = temp_idx

    return perm_idx


def game(adj_matrix):
    human_index = 0
    comp_index = 0

    # Continue till goal state is reached
    print("You may start first")
    while True:
        print("Click anything to roll dice")
        opt = int(input())
        print("You have rolled the dice....")

        time.sleep(3)
        hum_roll = roll_dice()

        human_index = move(human_index, hum_roll, adj_matrix)

        if human_index > 99:
            # In case of crossing finish line, continue until exact no of steps have been reached.
            human_index = human_index-hum_roll

        print(f"You have moved to index {human_index}")
        if human_index == 99:
            print("You win!!!")
            break

        print("Turn of Computer")
        print("Computer rolls dice....")
        time.sleep(3)

        comp_roll = roll_dice()
        comp_index = move(comp_index, comp_roll, adj_matrix)

        if comp_index > 99:
            comp_index = comp_index-comp_roll

        print(f"Computer has moved to index {comp_index}")
        if comp_index == 99:
            print("Computer wins!!!")
            break
