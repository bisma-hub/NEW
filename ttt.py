def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board, player):
    # Winning combinations
    wins = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    return all(space != ' ' for space in board)

def tic_tac_toe():
    board = [' '] * 9  # Empty board
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Players take turns to enter a number (1-9) to place their mark.")
    print("The positions on the board are numbered as follows:")
    print_board([str(i) for i in range(1,10)])

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 9.")
            continue

        if move < 1 or move > 9:
            print("Invalid move! Please enter a number from 1 to 9.")
            continue

        if board[move - 1] != ' ':
            print("That position is already taken. Choose another.")
            continue

        board[move - 1] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    print("Game over!")

if __name__ == "__main__":
    tic_tac_toe()
