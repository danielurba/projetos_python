from random import randint
from csv import writer, reader
from passlib.hash import pbkdf2_sha256 as cryp

class Perguntas:

    conta = []

    def __init__(self, quest, porcent):
        self.porcent = porcent
        self.quest = quest
        

    def faturporce(self):
        if self.quest != None:
            qp1 = float(self.quest) / 100
            self.qp1result = qp1 * int(Perguntas.conta[0])
            self.qp1resultf = int(Perguntas.conta[0]) - int(self.qp1result)
            dinh = "Dinheiro investido\n com sucesso!!"
            cont = f"R$ {self.qp1resultf},00"
            return (dinh, cont)

    def playquest1(self):
        if self.qp1result != None:
            porce = self.porcent / 100
            if porce > 0:
                p1 = porce * self.qp1result
                resultp1 = p1 + int(Perguntas.conta[0])
                Perguntas.conta.clear()
                Perguntas.conta.append(int(resultp1))
                recup = f"Você recuperou {self.porcent}%\n das vendas de ações."
                cont2 = f"R$ {int(resultp1)},00"
                return (recup, cont2, int(resultp1))
            else:
                p1 = porce * self.qp1result
                resultp1 = self.qp1result - abs(int(p1)) + self.qp1resultf
                Perguntas.conta.clear()
                Perguntas.conta.append(int(resultp1))
                recup = f"Você perdeu {self.porcent}%\n das vendas de ações."
                cont2 = f"R$ {int(resultp1)},00"
                return (recup, cont2, int(resultp1))

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


def write_login(conta, user):
    listalinhas = []
    with open('data_users.csv') as score:
        write_score = reader(score)
        for linha in write_score:
            if linha[0] == user:
                linhauser = linha.copy()
            else:
                listalinhas.append(linha)
    linhauser.pop()
    linhauser.append(str(conta))
    listalinhas.append(linhauser)
    with open('data_users.csv', 'w', newline='') as writ:
        escreve = writer(writ)
        for linha in listalinhas:
            escreve.writerow(linha)

def criaconta(login, senha):
    score = '100000'
    senha = cryp.hash(senha, rounds=200000, salt_size=16)
    try:
        with open('data_users.csv') as verif:
            leia = reader(verif)
            for linha in leia:
                if linha[0] == login:
                    return 'Usuário Já Existe!!'
            else:
                with open('data_users.csv', 'a', newline='') as arquivo:
                    escritor = writer(arquivo)
                    escritor.writerow([login, senha, score])
    except FileNotFoundError:
        with open('data_users.csv', 'a', newline='') as arquivo:
                    escritor = writer(arquivo)
                    escritor.writerow([login, senha, score])

def login(login, senha):
    with open('data_users.csv') as arquivos:
        leitor = reader(arquivos)
        for linha in leitor:
            if linha[0] == login and cryp.verify(senha, linha[1]):
                Perguntas.conta.append(linha[2])
                nome = linha[0]
                number = linha[2]
                return (True, nome, number)
        else:
            return (False, None, None)

def scores():
    scores = []
    names = []
    try:
        with open('data_users.csv') as arquivo1:
            leitorscores = reader(arquivo1)
            for score in leitorscores:
                names.append(score[0])
                scores.append(int(score[2]))
        name_score = zip(names, scores)
        score_final = dict(name_score)
        user = sorted(score_final, key=lambda valor: score_final[valor], reverse=True)
        number = sorted(scores, reverse=True)
        scores_sort = zip(user[:3], number[:3])
        final_sort = dict(scores_sort)
        dicion = []
        for users_scor in final_sort.items():
            dicion.append(users_scor)
        user1 = f'1 - {dicion[0][0].title()} {dicion[0][1]},00 R$'
        try:
            user2 = f'2 - {dicion[1][0].title()} {dicion[1][1]},00 R$'
        except IndexError:
            user2 = '2 - Não a usuário            '
        try:
            user3 = f'3 - {dicion[2][0].title()} {dicion[2][1]},00 R$'
        except IndexError:
            user3 = '3 - Não a usuario            '
        return (user1, user2, user3)
    except FileNotFoundError:
        user1 = '1 - Não a usuário              '
        user2 = '2 - Não a usuário              '
        user3 = '3 - Não a usuário              ' 
        return (user1, user2, user3)

