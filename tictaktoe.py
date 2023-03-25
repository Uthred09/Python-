board = {"top-L" : ' ', "top-M":' ', "top-R": ' ',
         "mid-L" : ' ', "mid-M":' ', "mid-R": ' ',
         "low-L" : ' ', "low-M":' ', "low-R": ' '
}

def printboard(board):
    print(board['top-L'] + "|" + board['top-M'] + "|", board['top-R'] )
    print("-+-+-")
    print(board['mid-L'] + "|" + board['mid-M'] + "|", board['mid-R'] )
    print("-+-+-")
    print(board['low-L'] + "|" + board['low-M'] + "|", board['low-R'] )


turn = 'x'
for i in range(9):
    printboard(board)
    print("Turn for ", turn, " Move to which place: ")
    move = input()
    board[move]= turn
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
printboard(board)
