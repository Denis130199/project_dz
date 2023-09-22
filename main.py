board = [" " for _ in range(9)]


def display_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("---------")


def check_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


current_player = "X"
while True:
    display_board()
    print(f"Ход игрока {current_player}")

    try:
        move = int(input("Выберите позицию (1-9): ")) - 1
        if move < 0 or move > 8 or board[move] != " ":
            print("Некорректный ход. Попробуйте еще раз.")
            continue
    except ValueError:
        print("Введите число от 1 до 9.")
        continue

    board[move] = current_player

    if check_winner(current_player):
        display_board()
        print(f"Игрок {current_player} победил!")
        break

    if " " not in board:
        display_board()
        print("Ничья!")
        break

    current_player = "X" if current_player == "O" else "O"
