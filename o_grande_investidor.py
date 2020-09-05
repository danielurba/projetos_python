# -*- coding: utf-8 -*-
"""
O Grande Investidor, Jogo que você começa com 100000,00 e investe em empresas. Vai Gerar uma porcentagem de -100% ate 100% do
valor que vc investiu, e retornara na sua conta, com 15 perguntas sobre empresas.
"""

from random import randint
from time import sleep

bemvindo = {
"ola" : "Olá Bem Vindo ao Jogo",
"bem" : "O Grande Investidor - Project ",
"feito" : "Feito Por DANIEL"
}
for text in bemvindo:
    print (bemvindo[text])
print()

#Porcentagen aleartorias

numbersq1 = int(randint(10, 60))
numbersq2 = int(randint(50, 90))
numbersq3 = int(randint(-40, -10))
numbersq4 = int(randint(10, 20))
numbersq5 = int(randint(10, 30))
numbersq6 = int(randint(50, 100))
numbersq7 = int(randint(-70, -40))
numbersq8 = int(randint(-20, -10))
numbersq9 = int(randint(10, 20))
numbersq10 = int(randint(-20, -10))

#Porcentagen aleartorias

#####################################################################################################
######################################### TODAS AS PERGUNTAS ########################################
#####################################################################################################

                             # PERGUNTA 01

def quest1pt():
    conta.append(100000)
    print()
    print(f"Conta: {conta[0]},00 R$")
    print()
    true = True
    while true:
        quest1p = input("01 - A ações da empresa CALT SA estavam em 0,98 e foi para 1,45 em 10 dias e continua subindo. Deseja Investir ? S/N: ")
        print()
        if quest1p == "s":
            while True:
                try:
                    quest1 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest1 > 0 and quest1 <= 100:
                        return quest1
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest1p == "n":
            print (f"As ações tiveram alta {numbersq1}% ")
            print()
            true = False
            playquest2(numbersq2)
        else:
            print("Inválido!")



                          #PERGUNTA 02
def quest2pt():
    true = True
    while true:
        quest2p = input("02 - A CALT SA subiu de 1,45 para 1,78. Deseja Investir ? S/N: ")
        print()
        if quest2p == "s":
            while True:
                try:
                    quest2 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest2 > 0 and quest2 <= 100:
                        return quest2
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest2p == "n":
            print (f"As ações subiram {numbersq2}% em poucos dias")
            print()
            true = False
            playquest3(numbersq3)
        else:
            print("Inválido!")



                         #PERGUNTA 03
def quest3pt():
    true = True
    while true:
        quest3p = input("03 - Muito bem as ações da CALT SA subiram 300%, de 1,45 para 4,35. Porem estão com muitos dividendos!!. Deseja Investir ? S/N: ")
        print()    
        if quest3p == "s":
            while True:
                try:
                    quest3 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest3 > 0 and quest3 <= 100:
                        return quest3
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest3p == "n":
            print (f"As ações cairam dastricamente {numbersq3}% e voltou abaixo do preço inicial!!")
            print()
            true = False
            playquest4(numbersq4)
        else:
            print("Inválido!")



                                #PERGUNTA 04
def quest4pt():
    true = True
    while true:
        quest4p = input("04 - A CALT SA teve uma queda incrivel em sua acões, muitos investidores perderam muito dinheiro!!. Deseja Investir agora que está barato ? S/N: ")
        print()  
        if quest4p == "s":
            while True:
                try:
                    quest4 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest4 > 0 and quest4 <= 100:
                        return quest4
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest4p == "n":
            print (f"As ações subiram um pouco, {numbersq4}% e chegou ao valor de 1,67 !!")
            print()
            true = False
            playquest5(numbersq5)
        else:
            print("Inválido!")



                                #PERGUNTA 05
def quest5pt():
    true = True
    while true:
        quest5p = input("05 - Uma empresa grande está entrando no mercado financeiro, a MTREPS empresa alimenticía esta com valor de suas ações baixas !!. Deseja Investir ? S/N: ")
        print()
        if quest5p == "s":
            while True:
                try:
                    quest5 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest5 > 0 and quest5 <= 100:
                        return quest5
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest5p == "n":
            print (f"As ações subiram {numbersq5}%")
            print()
            true = False
            playquest6(numbersq6)
        else:
            print("Inválido!")



                                #PERGUNTA 06
def quest6pt():
    true = True
    while true:
        quest6p = input("06 - A MTREPS teve ótimos resultados, e sua ações subiram um pouco !!. Deseja Investir novamente ? S/N: ")
        print()   
        if quest6p == "s":
            while True:
                try:
                    quest6 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest6 > 0 and quest6 <= 100:
                        return quest6
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest6p == "n":
            print (f"As ações explodiram, chegando aos {numbersq6}% os investidores ficaram animados!!")
            print()
            true = False
            playquest7(numbersq7)
        else:
            print("Inválido!")



                                #PERGUNTA 07
def quest7pt():
    true = True
    while true:
        quest7p = input("07 - Explendido!! A empresa lucrou muito e sua ações subiram absurdamente, porém estão aflitos devido uma crise que se inicia no país. Deseja Investir ? S/N: ")
        print()
        if quest7p == "s":
            while True:
                try:
                    quest7 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest7 > 0 and quest7 <= 100:
                        return quest7
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest7p == "n":
            print (f"As ações cairam {numbersq7}% e a MTREPS perde muitos investidores devido a crise!")
            print()
            true = False
            playquest8(numbersq8)
        else:
            print("Inválido!")



                                #PERGUNTA 08
def quest8pt():
    true = True
    while true:
        quest8p = input("08 - A crise destruiu com as ações da empresa, porem continuam com suas ações no mercado!!. Deseja Investir ? S/N: ")
        print()    
        if quest8p == "s":
            while True:
                try:
                    quest8 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest8 > 0 and quest8 <= 100:
                        return quest8
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest8p == "n":
            print (f"As ações cairam um pouco, {numbersq8}%")
            print()
            true = False
            playquest9(numbersq9)
        else:
            print("Inválido!")



                                #PERGUNTA 09
def quest9pt():
    true = True
    while true:
        quest9p = input("09 - A SIDES-SHIRTS empresa de produção de roupas de marcas caras, oscila suas ações no mercado!!. Deseja arriscar investir ? S/N: ")
        print() 
        if quest9p == "s":
            while True:
                try:
                    quest9 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest9 > 0 and quest9 <= 100:
                        return quest9
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest9p == "n":
            print (f"As ações se elevaram aos {numbersq9}%")
            print()
            true = False
            playquest10(numbersq10)
        else:
            print("Inválido!")



                                #PERGUNTA 10
def quest10pt():
    true = True
    while true:
        quest10p = input("10 - As SIDES-SHIRTS teve um bom desempenho porem, como dito suas ações oscilam de tempos em tempos!!. Deseja Investir ? S/N: ")
        print()
        if quest10p == "s":
            while True:
                try:
                    quest10 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if quest10 > 0 and quest10 <= 100:
                        return quest10
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif quest10p == "n":
            print (f"As ações cairam {numbersq10}%")
            print()
            true = False
            writescore()
        else:
            print("Inválido!")



#####################################################################################################
######################################### TODAS AS PERGUNTAS ########################################
#####################################################################################################

                             #DINHEIRO
conta = []

#####################################################################################################
#################################  INVESTIMENTOS E CALCULOS  ########################################
#####################################################################################################
                            #PERGUNTA 01

def faturporce():
    quest1 = quest1pt()
    if quest1 != None:
        qp1 = float(quest1) / 100
        qp1result = qp1 * conta[0]
        qp1resultf = conta[0] - int(qp1result)
        print ("Comprando ações...")
        sleep(2)
        print()
        print ("Dinheiro investido na CALT SA com sucesso!!")
        sleep(1)
        print()
        print (f"Conta: {qp1resultf},00 R$")
        sleep(1)
        print()
        return qp1result

                           #PERGUNTA 02
def faturporce2():
    quest2 = quest2pt()
    if quest2 != None:
        qp2 = float(quest2) / 100
        qp1result2 = qp2 * conta[0]
        global qp1resultf2
        qp1resultf2 = conta[0] - int(qp1result2)
        print ("Comprando ações...")
        sleep(2)
        print ("Investimento concluido!!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf2)},00 R$")
        sleep(1)
        print()
        return qp1result2
                           #PERGUNTA 03
def faturporce3():
    quest3 = quest3pt()
    if quest3 != None:
        qp3 = float(quest3) / 100
        qp1result3 = qp3 * conta[0]
        global qp1resultf3
        qp1resultf3 = conta[0] - int(qp1result3)
        print ("Comprando ações...")
        sleep(2)
        print ("Comprado com sucesso!!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf3)},00 R$")
        sleep(1)
        print()
        return qp1result3

                           #PERGUNTA 04
def faturporce4():
    quest4 = quest4pt()
    if quest4 != None:
        qp4 = float(quest4) / 100
        qp1result4 = qp4 * conta[0]
        global qp1resultf4
        qp1resultf4 = conta[0] - int(qp1result4)
        print ("Comprando ações...")
        sleep(2)
        print ("Dinheiro investido na CALT SA!!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf4)},00 R$")
        sleep(1)
        print()
        return qp1result4

                           #PERGUNTA 05
def faturporce5():
    quest5 = quest5pt()
    if quest5 != None:
        qp5 = float(quest5) / 100
        qp1result5 = qp5 * conta[0]
        global qp1resultf5
        qp1resultf5 = conta[0] - int(qp1result5)
        print ("Comprando ações...")
        sleep(2)
        print ("Dinheiro investido!!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf5)},00 R$")
        sleep(1)
        print()
        return qp1result5

                           #PERGUNTA 06
def faturporce6():
    quest6 = quest6pt()
    if quest6 != None:
        qp6 = float(quest6) / 100
        qp1result6 = qp6 * conta[0]
        global qp1resultf6
        qp1resultf6 = conta[0] - int(qp1result6)
        print ("Comprando ações...")
        sleep(2)
        print ("Comprado com sucesso!!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf6)},00 R$")
        sleep(1)
        print()
        return qp1result6

                           #PERGUNTA 07
def faturporce7():
    quest7 = quest7pt()
    if quest7 != None:
        qp7 = float(quest7) / 100
        qp1result7 = qp7 * conta[0]
        global qp1resultf7
        qp1resultf7 = conta[0] - int(qp1result7)
        print ("Comprando ações...")
        sleep(2)
        print ("Investimento feito!!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf7)},00 R$")
        sleep(1)
        print()
        return qp1result7

                           #PERGUNTA 08
def faturporce8():
    quest8 = quest8pt()
    if quest8 != None:
        qp8 = float(quest8) / 100
        qp1result8 = qp8 * conta[0]
        global qp1resultf8
        qp1resultf8 = conta[0] - int(qp1result8)
        print ("Comprando ações...")
        sleep(2)
        print ("Investido !!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf8)},00 R$")
        sleep(1)
        print()
        return qp1result8

                           #PERGUNTA 09
def faturporce9():
    quest9 = quest9pt()
    if quest9 != None:
        qp9 = float(quest9) / 100
        qp1result9 = qp9 * conta[0]
        global qp1resultf9
        qp1resultf9 = conta[0] - int(qp1result9)
        print ("Comprando ações...")
        sleep(2)
        print ("Dinheiro investido na SIDES-SHIRTS com sucesso!!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf9)},00 R$")
        sleep(1)
        print()
        return qp1result9

                           #PERGUNTA 10
def faturporce10():
    quest10 = quest10pt()
    if quest10 != None:
        qp10 = float(quest10) / 100
        qp1result10 = qp10 * conta[0]
        global qp1resultf10
        qp1resultf10 = conta[0] - int(qp1result10)
        print ("Comprando ações...")
        sleep(2)
        print ("Investimento concluido!!")
        sleep(1)
        print()
        print (f"Conta: {int(qp1resultf10)},00 R$")
        sleep(1)
        print()
        return qp1result10


#####################################################################################################
#################################  RECUPERAÇÃO OU PERDA E VALOR EM CONTA  ###########################
#####################################################################################################

                           #PERGUNTA 01
def playquest1(numbersq1):
    qp1result = faturporce()
    if qp1result != None:
        porce = numbersq1 / 100
        if porce > 0:
            p1 = porce * qp1result
            resultp1 = p1 + conta[0]
            conta.clear()
            conta.append(int(resultp1))
            print (f"Você recuperou {numbersq1}% das vendas de ações CALT SA.")
            print ()
            print (f"Conta: {int(resultp1)},00 R$")
            print()
            playquest2(numbersq2)

                           #PERGUNTA 02
def playquest2(numbersq2):
    qp1result2 = faturporce2()
    if qp1result2 != None:
        porce = numbersq2 / 100
        if porce > 0:
            p2 = porce * qp1result2
            resultp2 = p2 + qp1result2 + qp1resultf2
            conta.clear()
            conta.append(int(resultp2))
            print (f"Você recuperou {numbersq2}% das vendas de ações CALT SA.")
            print ()
            print (f"Conta: {int(resultp2)},00 R$")
            print()
            playquest3(numbersq3)

                           #PERGUNTA 03
def playquest3(numbersq3):
    qp1result3 = faturporce3()
    if qp1result3 != None:
        porce = numbersq3 / 100
        if porce < 0:
            p3 = porce * qp1result3
            resultp3 = qp1result3 - abs(int(p3)) + qp1resultf3
            conta.clear()
            conta.append(int(resultp3))
            print (f"Você perdeu {numbersq3}% das vendas de ações CALT SA.")
            print ()
            print (f"Conta: {int(resultp3)},00 R$")
            print()
            playquest4(numbersq4)

                           #PERGUNTA 04
def playquest4(numbersq4):
    qp1result4 = faturporce4()
    if qp1result4 != None:
        porce = numbersq4 / 100
        if porce > 0:
            p4 = porce * qp1result4
            resultp4 = p4 + qp1result4 + qp1resultf4
            conta.clear()
            conta.append(int(resultp4))
            print (f"Você lucrou {numbersq4}% das vendas.")
            print ()
            print (f"Conta: {int(resultp4)},00 R$")
            print()
            playquest5(numbersq5)

                           #PERGUNTA 05
def playquest5(numbersq5):
    qp1result5 = faturporce5()
    if qp1result5 != None:
        porce = numbersq5 / 100
        if porce > 0:
            p5 = porce * qp1result5
            resultp5 = p5 + qp1result5 + qp1resultf5
            conta.clear()
            conta.append(int(resultp5))
            print (f"Você recuperou {numbersq5}% das vendas de ações MTREPS.")
            print ()
            print (f"Conta: {int(resultp5)},00 R$")
            print()
            playquest6(numbersq6)

                           #PERGUNTA 06
def playquest6(numbersq6):
    qp1result6 = faturporce6()
    if qp1result6 != None:
        porce = numbersq6 / 100
        if porce > 0:
            p6 = porce * qp1result6
            resultp6 = p6 + qp1result6 + qp1resultf6
            conta.clear()
            conta.append(int(resultp6))
            print (f"Você lucrou {numbersq6}%.")
            print ()
            print (f"Conta: {int(resultp6)},00 R$")
            print()
            playquest7(numbersq7)

                           #PERGUNTA 07
def playquest7(numbersq7):
    qp1result7 = faturporce7()
    if qp1result7 != None:
        porce = numbersq7 / 100
        if porce < 0:
            p7 = porce * qp1result7
            resultp7 = qp1result7 - abs(int(p7)) + qp1resultf7
            conta.clear()
            conta.append(int(resultp7))
            print (f"Você perdeu {numbersq7}% das vendas de ações.")
            print ()
            print (f"Conta: {int(resultp7)},00 R$")
            print()
            playquest8(numbersq8)

                           #PERGUNTA 08
def playquest8(numbersq8):
    qp1result8 = faturporce8()
    if qp1result8 != None:
        porce = numbersq8 / 100
        if porce < 0:
            p8 = porce * qp1result8
            resultp8 = qp1result8 - abs(int(p8)) + qp1resultf8
            conta.clear()
            conta.append(int(resultp8))
            print (f"Você perdeu {numbersq8}% das vendas de ações da MTREPS.")
            print ()
            print (f"Conta: {int(resultp8)},00 R$")
            print()
            playquest9(numbersq9)


                           #PERGUNTA 09
def playquest9(numbersq9):
    qp1result9 = faturporce9()
    if qp1result9 != None:
        porce = numbersq9 / 100
        if porce > 0:
            p9 = porce * qp1result9
            resultp9 = p9 + qp1result9 + qp1resultf9
            conta.clear()
            conta.append(int(resultp9))
            print (f"Você recuperou {numbersq9}% das vendas de ações da SIDES-SHIRTS.")
            print ()
            print (f"Conta: {int(resultp9)},00 R$")
            print()
            playquest10(numbersq10)

                           #PERGUNTA 10
def playquest10(numbersq10):
    qp1result10 = faturporce10()
    if qp1result10 != None:
        porce = numbersq10 / 100
        if porce < 0:
            p10 = porce * qp1result10
            global resultp10
            resultp10 = qp1result10 - abs(int(p10)) + qp1resultf10
            conta.clear()
            conta.append(int(resultp10))
            print (f"Você perdeu {numbersq10}% das vendas de ações da SIDES-SHIRTS.")
            print ()
            print (f"Conta: {int(resultp10)},00 R$")
            print()
            writescore()

def writescore():
    questscore = input("Nome para Score: ")
    with open("Score.txt", "a") as f:
        score = questscore + " " + str(int(conta[0]))
        f.write(str(score) + "\n")

def readscores():
    with open("Score.txt", "r") as myscore:
        variav = myscore.read()
        variav = variav.split()
        res = map(int, (variav[1::2]))
        user = variav[::2]
        score = list(res)
        final = zip(user, score)
        scores_final = dict(final)
        names = sorted(scores_final, key=lambda valor: scores_final[valor], reverse=True)
        number = sorted(score, reverse=True)
        scores_sort = zip(names[:3], number[:3])
        final_sort = dict(scores_sort)
        for indice, users_scor in enumerate(final_sort.items(), start=1):
            print(f'{indice} Usuario: {users_scor[0].title()} R$ {users_scor[1]}')


#####################################################################################################
#################################  RECUPERAÇÃO OU PERDA E VALOR EM CONTA  ###########################
#####################################################################################################

def play():
    while True:
        play = input("Digite S, para iniciar o Jogo. Digite V, para Scores, Ou X para Sair: ")
        if play == "s":
            playquest1(numbersq1)
        elif play == 'v':
            readscores()
        elif play == "x":
            break
        else:
            print("Inválido!!")

play() 
print("Fim do Jogo")
