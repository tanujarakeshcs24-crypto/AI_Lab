import random

board = [' ' for _ in range(9)]

def display():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])

def check_winner(symbol):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False

def full():
    return ' ' not in board

print("TIC-TAC-TOE")
print("You = X, Computer = O")
print("Positions are 1 to 9")

while True:
    display()

    pos = int(input("Enter your position: ")) - 1

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid position!")
        continue

    board[pos] = 'X'

    if check_winner('X'):
        display()
        print("You win!")
        break

    if full():
        display()
        print("Draw!")
        break

    empty = [i for i in range(9) if board[i] == ' ']
    computer = random.choice(empty)
    board[computer] = 'O'

    print("Computer selected:", computer + 1)

    if check_winner('O'):
        display()
        print("Computer wins!")
        break

    if full():
        display()
        print("Draw!")
        break