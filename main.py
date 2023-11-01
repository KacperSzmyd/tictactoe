import random
board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
currentPlayer = ' X '


def resetBoard():
    return ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]


def resetPlayer():
    return ' X '


def checkMove(move):
    if move in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if board[int(move)-1] == '   ':
            return True
    else:
        return False


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 15)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 15)
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerMove(board):
    while True:
        move = input("Pick a number from 1 to 9: ")
        if checkMove(move):
            board[int(move)-1] = currentPlayer
            break
        else:
            print('Please pick another number!')


def SIMove(board):
    while True:
        move = random.randint(1, 9)
        if board[move-1] == '   ':
            board[move-1] = currentPlayer
            break


def switchPlayers():
    global currentPlayer
    if currentPlayer == ' X ':
        currentPlayer = ' O '
    else:
        currentPlayer = ' X '


def checkHorizontal(board):
    if (board[0] == board[1] == board[2] and board[0] != "   ") or (board[3] == board[4] == board[5] and board[3] != "   ") or (board[6] == board[7] == board[8] and board[6] != "   "):
        return True


def checkRow(board):
    if (board[0] == board[3] == board[6] and board[0] != "   ") or (board[1] == board[4] == board[7] and board[1] != "   ") or (board[2] == board[5] == board[8] and board[2] != "   "):
        return True


def checkDiagonal(board):
    if (board[0] == board[4] == board[8] and board[0] != "   ") or (board[2] == board[4] == board[6] and board[2] != "   "):
        return True


def checkWin(board):
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        return True


def checkTie(board):
    if "   " not in board:
        return True


while True:
    board = resetBoard()
    currentPlayer = resetPlayer()

    mode = input('Are you playing with friend or against SI? (f/s)')
    if mode not in ['f', 's']:
        print('Choose a correct value (f for playing with friend or s for SI')
        continue

    if mode == 'f':
        while mode:
            printBoard(board)
            playerMove(board)
            if checkWin(board):
                print(f"The winner is {currentPlayer}")
                printBoard(board)
                break
            if checkTie(board):
                print("Its a tie")
                printBoard(board)
                break
            switchPlayers()

    if mode == 's':
        while mode:
            printBoard(board)
            playerMove(board)
            if checkWin(board):
                print(f"The winner is {currentPlayer}")
                printBoard(board)
                break
            if checkTie(board):
                print("Its a tie")
                printBoard(board)
                break
            switchPlayers()
            SIMove(board)
            if checkWin(board):
                print(f"The winner is {currentPlayer}")
                printBoard(board)
                break
            if checkTie(board):
                print("Its a tie")
                printBoard(board)
                break
            switchPlayers()