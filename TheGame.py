def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def crosses_and_toes():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "1"

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, выберите ряд (0, 1, or 2): "))
        col = int(input(f"Игрок {current_player}, выберите колонку (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif board_full(board):
                print_board(board)
                print("Ничья.")
                break
            else:
                current_player = "2" if current_player == "1" else "1"
        else:
            print("Выберите другую клетку.")

if __name__ == "__main__":
    crosses_and_toes()