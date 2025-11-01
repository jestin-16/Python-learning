import random

board=["-","-","-",
        "-","-","-",
        "-","-","-"]

currentPlayer = "X"
winner =None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("_________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("_________")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    # This function is now ONLY for the human player 'X'
    while True:
        try:
            # Added an explicit check for the current player being 'X'
            if currentPlayer == 'X':
                inp = int(input(f"Player {currentPlayer}, enter a number 1-9: "))
                if 1 <= inp <= 9 and board[inp-1] == "-":
                    board[inp-1] = currentPlayer
                    break # Exit the loop if input is valid
                elif 1 <= inp <= 9:
                    print("Oops! That spot is already taken. Try again.")
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
            else:
                 # Should not happen in this flow, but as a safeguard
                 break
        except ValueError:
             print("Invalid input. Please enter a valid number.")


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner =board[0]
        return True
    elif board[3]== board[4] == board[5] and board[3] != "-":
        winner =board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner =board[6]
        return True

def checkRow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0] != "-":
        winner =board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1] != "-":
        winner =board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2] != "-":
        winner =board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner =board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner =board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a Tie!")
        gameRunning = False
        return True

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def checkWin(board):
    global gameRunning
    if checkHorizontal(board) or checkDiagonal(board) or checkRow(board):
        printBoard(board)
        print(f"🎉 The winner is {winner}! 🎉")
        gameRunning = False


# --- Corrected Computer Logic ---
def computer(board):
    # Only run if the computer's turn ('O') and the game is running
    if currentPlayer == "O" and gameRunning:
        print("Computer (O) is thinking...")
        while True:
            # Computer selects a random position from 0 to 8
            position = random.randint(0, 8)
            # Check if the chosen spot is empty
            if board[position] == "-":
                board[position] = "O"
                break # Break out of the infinite loop once a valid move is made


# --- Main Game Loop ---
while gameRunning:
    # 1. Human Player 'X' Turn
    printBoard(board)
    playerInput(board)

    # 2. Check for Win/Tie after Human Move
    checkWin(board)
    if not gameRunning:
        break # End game if X won
    checkTie(board)
    if not gameRunning:
        break # End game if tie

    # 3. Switch to Computer Player 'O'
    switchPlayer()

    # 4. Computer Player 'O' Turn
    computer(board)

    # 5. Check for Win/Tie after Computer Move
    checkWin(board)
    if not gameRunning:
        break # End game if O won
    checkTie(board)
    if not gameRunning:
        break # End game if tie

    # 6. Switch back to Human Player 'X'
    switchPlayer()