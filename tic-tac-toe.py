theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []
for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0
    while True:
        printBoard(theBoard)
        print("Its your turn {}. \n move to which place?".format(turn))

        while True:
            try:
                move = input()
                if theBoard[move] == ' ':
                    break
                elif theBoard[move] == 'X' or theBoard[move] == 'O':
                    print(("the place is already filled.\n move to which place ?"))
                    continue
            except KeyError:
                print("you r supposed to put a number from 1 to 9")

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(" **** " + turn + " won. **** ")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['9'] == theBoard['5'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print("Game Over")
                print(" **** " + turn + " won. ****")
                break
        if count == 9:
            print("Game Over")
            print("its a tie!")
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


game()
restart = input("do u want to play again ?(y/n)")
if restart == 'y' or restart == 'Y':
    for key in board_keys:
        theBoard[key] = ' '
    game()
elif restart == 'N' or restart == 'n':
    print("Game end")
