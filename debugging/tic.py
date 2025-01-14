#!/usr/bin/python3
def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there is a winner on the board.
    
    Returns:
    str: The symbol of the winning player ("X" or "O"), or None if no winner.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_draw(board):
    """
    Checks if the board is full, indicating a draw.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        
        # Validate user input for row and column
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Check if the chosen spot is available
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken! Try again.")
            continue

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
