#Game Pedra papel tesoura com o computador.. Ira pedir qual dos 3 você escolhe
#E o computador ira jogar com você !!
from random import randint

opçao = ["pedra", "papel", "tesoura"]
mensagem = {
    "empate" : ["Deu Empate !!"],
    "ganhou" : ["ISSO, Você Ganhou !!"],
    "perdeu" : ["Aww Você Perdeu !!"]
}

def decidewinner(userchoice, computerchoice):
    print ("Você mostrou %s" % userchoice)
    print ("O computador mostrou %s" % computerchoice)
    if userchoice == computerchoice:
        print (mensagem["empate"])
    elif userchoice == opçao[0] and computerchoice == opçao[2]:
        print (mensagem["ganhou"])
    elif userchoice == opçao[2] and computerchoice == opçao[1]:
        print (mensagem["ganhou"])
    elif userchoice == opçao[1] and computerchoice == opçao[0]:
        print (mensagem["ganhou"])
    else:
        print (mensagem["perdeu"])

def playppt():
    userchoice = input("Pedra, Papel ou Tesoura ?: ").lower()
    computerchoice = opçao[randint(0, 2)]
    decidewinner(userchoice, computerchoice)
playppt()
