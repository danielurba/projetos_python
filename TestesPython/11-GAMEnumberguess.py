# Jogo de Dados !! O computador Joga os dados, e pede para vc adivinhar a soma
# dos dados, caso voce acerte, voce vence. Caso erre o computador vence !!

from random import randint
from time import sleep

#A Pergunta Abaixo
def getuserguess():
    guess = int(input("Qual é o Numero ? "))
    return guess

#Inforções para os Dados
def rolldice(numberofsides):
    firstroll = randint(1, numberofsides)
    secondroll = randint(1, numberofsides)
    maxval = numberofsides * 2
    print (("Diga Um Valor de 1 a %d") % maxval)

#Jogo Na Ativa
    guess = getuserguess()
    if guess > maxval:
        print ("Invalido!!")
    else:
        print("Carregando...")
        sleep(2)
        print(("Lado do Dado Caiu em %d") % firstroll)
        sleep(1)
        print(("Lado do Dado Caiu em %d") % secondroll)
        sleep(1)
        totalroll = firstroll + secondroll
        print ("Resultado...")
        print(totalroll)
        sleep(1)
        if guess == totalroll:
            print ("Você Venceuuu Parabéns UHUUUUU")
        elif guess != totalroll:
            print("Você Perdeuuu '-' Que Pena !!!")


rolldice(6)
