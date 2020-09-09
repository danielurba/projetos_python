from random import randint

board = []
for tj in range(5):
    board.append(["O"]*5)

def printboard(boardin):
    for row in board:
        print (" ".join(row))

printboard(board)

def randomrow(boardin):
    return randint(0,len(boardin) - 1)

def randomcol(boardin):
    return randint(0,len(boardin) - 1)

shiprow = randomrow(board)
shipcol = randomcol(board)

print(shiprow)
print(shipcol)

for turn in range(4):
    print("Tentativa", turn + 1)
    guessrow = int(input("Qual linha?:"))
    guesscol = int(input("Qual coluna?:"))

    if guessrow == shiprow and guesscol == shipcol:
        print ("Parabéns! Você afundou meu navio de guerra! ")
        break
    else:    
        if guessrow not in range(5) or \
            guesscol not in range(5):
            print("Opa, isso nem está no oceano.")
        elif board[guessrow][guesscol] == "x":
            print("Você já tentou esse.")
        else:
            print("Você perdeu meu navio de guerra!")
            board[guessrow][guesscol] = "x"
        if turn == 3:
            print("Fim de Jogo")
        
printboard(board)
randomrow(board)
randomcol(board)
    
