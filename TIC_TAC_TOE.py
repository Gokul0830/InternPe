#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def print_board(board):
    print("-------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print("\n-------")

def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if "-" in row:
            return False
    return True

def get_user_move():
    while True:
        try:
            move = input("Enter your move (row column): ")
            row, col = map(int, move.split())
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid move. Please enter a valid move.")
        except ValueError:
            print("Invalid input. Please enter row and column as integers.")

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                empty_cells.append((row, col))
    return empty_cells

def server_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [["-" for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        if player == "X":
            print_board(board)
            row, col = get_user_move()
        else:
            row, col = server_move(board)

        if board[row][col] == "-":
            board[row][col] = player

            if is_winner(board, player):
                print_board(board)
                if player == "X":
                    print("Congratulations! You win!")
                else:
                    print("Sorry, you lost. Server wins.")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("That cell is already occupied. Please choose another move.")

    print_board(board)


# Start the game
play_game()


# In[ ]:




