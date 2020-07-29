import random
import sys
print("Tic Tac Toe")
#asks user if the want to play game
i = True
while i == True:
    try:
        game = input('If you want to play tic tac toe then type "tic tac toe": ')
        assert game == "tic tac toe" or game == "continue"
    except(AssertionError):
        print("try again")
        continue
    i = False
#if user enters an invalid response ask them to enter a valid response
'''while game != "tic tac toe" and game != "continue":
    print("This program does not support that game yet")
    game = input('If you want to play tic tac toe then type "tic tac toe": ')'''
#program starts when user enters valid response
while game == "tic tac toe" or game == "continue":
    print("How to play: ")
    print("You and the computer take turns placing an X.")
    print("To place an X type the corresponding number")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")
    print("The player who acheives 3 X's first wins.")
    #prints board with the spaces provided
    def printBoard(x_spaces,o_spaces):
        for num in x_spaces:
            board[num] = "X"
        for num in o_spaces:
            board[num] = "O"
        print(board[0],"|",board[1],"|",board[2])
        print(board[3],"|",board[4],"|",board[5])
        print(board[6],"|",board[7],"|",board[8])
    #checks if either X or O have won the game
    def checkWin(board):
        for i in range(3):
            if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i]!="_":
                print("Player " + board[i] + " is the winner!")
                return True
                break
        for i in range(7):
            if i==0 or i==3 or i==6:
                if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i]!="_":
                    print("Player " + board[i] + " is the winner!")
                    return True
                    break
        if board[0] == board[4] and board[4] == board[8] and board[0]!="_":
            print("Player " + board[0] + " is the winner!")
            return True
        if board[2] == board[4] and board[4] == board[6] and board[2]!="_":
            print("Player " + board[2] + " is the winner!")
            return True
    #checks if the board is full
    def fullBoard(board):
        if board[0]!="_" and board[1]!="_" and board[2]!="_" and board[3]!="_" and board[4]!="_" and board[5]!="_" and board[6]!="_" and board[7]!="_" and board[8]!="_":
            print("It is a draw")
            return True
    #laying out variables needed within the game itself
    gamerun = True
    x_spaces = []
    o_spaces = []
    board = ["_","_","_","_","_","_","_","_","_"]
    while gamerun == True:
        #asks user for where to mark the X
        x_move = int(input("Where do you want to mark your X? "))
        #check if user input is valid
        #if user input is not valid ask for valid input
        while x_move > 8:
            x_move = int(input("Enter a number 0-8: "))
        while board[x_move] != "_":
            x_move = int(input("Pick a spot that has not been taken? "))
            while x_move > 8:
                x_move = int(input("Enter a number 0-8: "))
        if board[x_move] == "_":
            x_spaces.append(x_move)
        printBoard(x_spaces,o_spaces)
        print("++++++++++++++++++++")
        #checks if either "O" or "X" have won
        if checkWin(board) == True:
            break
        #checks if the game board is full
        if fullBoard(board) == True:
            break
        #produces random spot for the computer to place the O
        o_move = random.randrange(9)
        #checks if spot is availabe.
        #if spot is not availabe then computer randomly chooses different spot
        while board[o_move] != "_" or o_move==x_move:
            o_move = random.randrange(9)
        if board[o_move] == "_":
            o_spaces.append(o_move)
        printBoard(x_spaces,o_spaces)
        #checks if either "O" or "X" have won
        if checkWin(board) == True:
            break
        #checks if the game board is full
        if fullBoard(board) == True:
            break
    #asks user if the want to continue
    print('Type "continue" if you want to play again.')
    print('Type "exit" if you want to exit the game.')
    endgameinput= input()
    if endgameinput == "exit":
        sys.exit()
    if endgameinput == "continue":
        game == "continue"
    #if userinput is not valid ask for valid input
    while endgameinput != "exit" and endgameinput != "continue":
        endgameinput= input('Type either "exit" or "continue"')
