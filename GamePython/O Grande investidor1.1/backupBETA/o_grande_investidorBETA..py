from random import randint
from time import sleep
from csv import writer, reader
from passlib.hash import pbkdf2_sha256 as cryp

class Perguntas:

    conta = []

    def __init__(self, quest, porcent):
        self.porcent = porcent
        self.quest = quest
        self.quests()
        
    def quests(self):
        if self.quest == 's':
            while True:
                try:
                    self.quest1 = int(input("Deseja Investir quantos por cento ?: "))
                    print()
                    if self.quest1 > 0 and self.quest1 <= 100:
                        self.faturporce()
                        break
                    else:
                        print('Somente Numeros de 1 até 100')
                        print()
                except ValueError:
                    print()
                    print('Somente Numeros de 1 até 100')
                    print()
        elif self.quest == "n":
            if self.porcent > 0:
                print (f"As ações subiram {self.porcent}% em poucos dias")
            else:
                print (f"As ações cairam  {self.porcent}% em poucos dias")
        else:
            print('Inválido')

    def faturporce(self):
        if self.quest1 != None:
            qp1 = float(self.quest1) / 100
            self.qp1result = qp1 * int(Perguntas.conta[0])
            self.qp1resultf = int(Perguntas.conta[0]) - int(self.qp1result)
            print ("Comprando ações...")
            sleep(2)
            print()
            print ("Dinheiro investido na CALT SA com sucesso!!")
            sleep(1)
            print()
            print (f"Conta: {self.qp1resultf},00 R$")
            sleep(1)
            print()
            self.playquest1()

    def playquest1(self):
        if self.qp1result != None:
            porce = self.porcent / 100
            if porce > 0:
                p1 = porce * self.qp1result
                resultp1 = p1 + int(Perguntas.conta[0])
                Perguntas.conta.clear()
                Perguntas.conta.append(int(resultp1))
                print (f"Você recuperou {self.porcent}% das vendas de ações CALT SA.")
                print ()
                print (f"Conta: {int(resultp1)},00 R$")
                print()
            else:
                p1 = porce * self.qp1result
                resultp = self.qp1result - abs(int(p1)) + self.qp1resultf
                Perguntas.conta.clear()
                Perguntas.conta.append(int(resultp))
                print (f"Você perdeu {self.porcent}% das vendas de ações CALT SA.")
                print ()
                print (f"Conta: {int(resultp)},00 R$")
                print()


numbersq1 = int(randint(10, 60))
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

def input_quests():
    print(f'CONTA: {Perguntas.conta[0]},00 R$')
    
    true1 = True
    while true1:
        quest1 = input("01 - A ações da empresa CALT SA estavam em 0,98 e foi para 1,45 em 10 dias e continua subindo. Deseja Investir ? S/N: ")
        if quest1 == 's' or quest1 == 'S':
            Perguntas(quest1 ,numbersq1)
            true1 = False
        elif quest1 == 'n' or quest1 == 'N':
            Perguntas(quest1, numbersq1)
            true1 = False
        else:
            print('Invalido')

    true2 = True
    while true2:
        quest2 = input("02 - A CALT SA subiu de 1,45 para 1,78. Deseja Investir ? S/N: ")
        if quest2 == 's' or quest2 == 'S':
            Perguntas(quest2 ,numbersq2)
            true2 = False
        elif quest2 == 'n' or quest2 == 'N':
            Perguntas(quest2, numbersq2)
            true2 = False
        else:
            print('Invalido')

    true3 = True
    while true3:
        quest3 = input("03 - Muito bem as ações da CALT SA subiram 300%, de 1,45 para 4,35. Porem estão com muitos dividendos!!. Deseja Investir ? S/N: ")
        if quest3 == 's' or quest3 == 'S':
            Perguntas(quest3 ,numbersq3)
            true3 = False
        elif quest3 == 'n' or quest3 == 'N':
            Perguntas(quest3, numbersq3)
            true3 = False
        else:
            print('Invalido')

    true4 = True
    while true4:
        quest4 = input("04 - A CALT SA teve uma queda incrivel em sua acões, muitos investidores perderam muito dinheiro!!. Deseja Investir agora que está barato ? S/N: ")
        if quest4 == 's' or quest4 == 'S':
            Perguntas(quest4 ,numbersq4)
            true4 = False
        elif quest4 == 'n' or quest4 == 'N':
            Perguntas(quest4, numbersq4)
            true4 = False
        else:
            print('Invalido')

    true5 = True
    while true5:
        quest5 = input("05 - Uma empresa grande está entrando no mercado financeiro, a MTREPS empresa alimenticía esta com valor de suas ações baixas !!. Deseja Investir ? S/N: ")
        if quest5 == 's' or quest5 == 'S':
            Perguntas(quest5 ,numbersq5)
            true5 = False
        elif quest5 == 'n' or quest5 == 'N':
            Perguntas(quest5, numbersq5)
            true5 = False
        else:
            print('Invalido')

    true6 = True
    while true6:
        quest6 = input("06 - A MTREPS teve ótimos resultados, e sua ações subiram um pouco !!. Deseja Investir novamente ? S/N: ")
        if quest6 == 's' or quest6 == 'S':
            Perguntas(quest6 ,numbersq6)
            true6 = False
        elif quest6 == 'n' or quest6 == 'N':
            Perguntas(quest6, numbersq6)
            true6 = False
        else:
            print('Invalido')

    true7 = True
    while true7:
        quest7 = input("07 - Explendido!! A empresa lucrou muito e sua ações subiram absurdamente, porém estão aflitos devido uma crise que se inicia no país. Deseja Investir ? S/N: ")
        if quest7 == 's' or quest7 == 'S':
            Perguntas(quest7 ,numbersq7)
            true7 = False
        elif quest7 == 'n' or quest7 == 'N':
            Perguntas(quest7, numbersq7)
            true7 = False
        else:
            print('Invalido')

    true8 = True
    while true8:
        quest8 = input("08 - A crise destruiu com as ações da empresa, porem continuam com suas ações no mercado!!. Deseja Investir ? S/N: ")
        if quest8 == 's' or quest8 == 'S':
            Perguntas(quest8 ,numbersq8)
            true8 = False
        elif quest8 == 'n' or quest8 == 'N':
            Perguntas(quest8, numbersq8)
            true8 = False
        else:
            print('Invalido')

    true9 = True
    while true9:
        quest9 = input("09 - A SIDES-SHIRTS empresa de produção de roupas de marcas caras, oscila suas ações no mercado!!. Deseja arriscar investir ? S/N: ")
        if quest9 == 's' or quest9 == 'S':
            Perguntas(quest9 ,numbersq9)
            true9 = False
        elif quest9 == 'n' or quest9 == 'N':
            Perguntas(quest9, numbersq9)
            true9 = False
        else:
            print('Invalido')

    true10 = True
    while true10:
        quest10 = input("10 - As SIDES-SHIRTS teve um bom desempenho porem, como dito suas ações oscilam de tempos em tempos!!. Deseja Investir ? S/N: ")
        if quest10 == 's' or quest10 == 'S':
            Perguntas(quest10 ,numbersq10)
            true10 = False
        elif quest10 == 'n' or quest10 == 'N':
            Perguntas(quest10, numbersq10)
            true10 = False
        else:
            print('Invalido')
    write_login()


def write_login():
    listalinhas = []
    with open('data_users.csv') as score:
        write_score = reader(score)
        for linha in write_score:
            if linha[0] == user:
                linhauser = linha.copy()
            else:
                listalinhas.append(linha)
    linhauser.pop()
    linhauser.append(str(Perguntas.conta[0]))
    listalinhas.append(linhauser)
    with open('data_users.csv', 'w', newline='') as writ:
        escreve = writer(writ)
        for linha in listalinhas:
            escreve.writerow(linha)
                

def users():
    while True:
        primary = input('Digite a para acessar conta, c para criar uma conta v para scores e x para sair: ')
        if primary == 'a' or primary == 'A':
            global user
            user = input('Usuário: ')
            password = input('Senha: ')
            with open('data_users.csv') as arquivos:
                leitor = reader(arquivos)
                for linha in leitor:
                    if linha[0] == user and cryp.verify(password, linha[1]):
                        Perguntas.conta.append(linha[2])
                        input_quests()
                        return False
                else:
                    print('Não Logado')

        elif primary == 'c' or primary == 'C':
            user = input('Usuário: ')
            password = input('Senha: ')
            score = '100000'
            password = cryp.hash(password, rounds=200000, salt_size=16)
            with open('data_users.csv', 'a', newline='') as arquivo:
                escritor = writer(arquivo)
                escritor.writerow([user, password, score])
                
                
        elif primary == 'v' or primary == 'V':
            with open('data_users.csv') as arquivo1:
                leitorscores = reader(arquivo1)
                scores = []
                names = []
                for score in leitorscores:
                    names.append(score[0])
                    scores.append(score[2])
                name_score = zip(names, scores)
                name_score = dict(name_score)
                user = sorted(name_score, key=lambda valor: name_score[valor], reverse=True)
                scores = sorted(scores, reverse=True)
                scores_sort = zip(user[:3], scores[:3])
                final_sort = dict(scores_sort)
                print('Ranking')
                for indice, users_scor in enumerate(final_sort.items(), start=1):
                    print(f'{indice} Usuario: {users_scor[0].title()} R$ {users_scor[1]}\n')
                
        elif primary == 'x' or primary == 'X':
            break

users()
