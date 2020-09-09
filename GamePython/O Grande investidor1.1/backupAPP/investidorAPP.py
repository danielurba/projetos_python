from tkinter import *
from o_grande_investidorBETA import *

class Application:
    def __init__(self, master=None):
        user1, user2, user3 = scores()
        self.img = PhotoImage(file = "img/dinheirodolares.png") 
        self.img1 = self.img.subsample(1, 1) 
        self.img12 = Label(master, image = self.img1)
        self.img12.grid(row = 0, column = 2,
                        columnspan = 2, rowspan = 2, padx= 5, pady= 5)

        self.branco = PhotoImage(file = "img/branco.png") 
        self.branco1 = self.branco.subsample(1, 1) 
        self.branco2 = Label(master, image = self.branco1)
        self.branco2.grid(row = 0, column = 1,
                        columnspan = 2, rowspan = 2, padx = 25, pady = 25, sticky=NW)

        self.cinza = PhotoImage(file = "img/cinza.png") 
        self.cinza1 = self.cinza.subsample(1, 1) 
        self.cinza2 = Label(master, image = self.cinza1)
        self.cinza2.grid(row = 0, column = 3,
                        columnspan = 2, rowspan = 2, padx = 25, pady = 25, sticky=NE)

        self.login = Label(master, text = "Login", font= ('Arial', '12'), bg = '#f0f0f0') 
        self.senha = Label(master, text = "Senha", font= ('Arial', '12'), bg = '#f0f0f0')
        self.texto = Label(master, text = "", font= ('Helvetica Neue', '12'), bg = '#f0f0f0')
        self.ranking = Label(master, text = "Ranking", font= ('Arial Black', '12'), bg = '#959595')
        self.txt1 = Label(master, text = user1, font= ('Arial Black', '12'), bg = '#959595')
        self.txt2 = Label(master, text = user2, font= ('Arial Black', '12'), bg = '#959595')
        self.txt3 = Label(master, text = user3, font= ('Arial Black', '12'), bg = '#959595')

        self.login.grid(row = 0, column = 2, sticky = NW, padx = 37, pady = 40)
        self.senha.grid(row = 0, column = 2, sticky = NW, padx = 37, pady = 100)
        self.texto.grid(row = 0, column = 2, sticky = SW, padx = 80, pady = 160)
        self.ranking.grid(row = 0, column = 3, sticky = NE, padx = 125, pady = 30)
        self.txt1.grid(row = 0, column = 3, sticky = NE, padx = 60, pady = 80)
        self.txt2.grid(row = 0, column = 3, sticky = NE, padx = 60, pady = 130)
        self.txt3.grid(row = 0, column = 3, sticky = NE, padx = 60, pady = 180)

        self.login_entry = Entry(master, justify= CENTER, font= ('Arial', '12'),
                                 bg = '#e8f0fe') 
        self.senha_entry = Entry(master, justify= CENTER, font= ('Arial', '12'),
                                 bg = '#e8f0fe')
        self.senha_entry['show'] = '*'

        self.login_entry.grid(row = 0, column = 2, sticky = NW, padx = 90, pady = 40) 
        self.senha_entry.grid(row = 0, column = 2, sticky = NW, padx = 90, pady = 100) 

        self.b1 = Button(master, text = "Acessar", font=('Arial', '12'), bg='#3498db') 
        self.b1.grid(row = 0, column = 2, sticky = NW, padx = 145, pady= 140)
        self.b1['command'] = self.verificasenha

        self.b2 = Button(master, text = "Criar Conta", font=('Arial', '12'), bg='#00b33c') 
        self.b2.grid(row = 0, column = 2, sticky = NW, padx = 135, pady= 200)
        self.b2['command'] = self.criaconta1
        
        self.dois = Label(master, text = "O Grande Investidor Version 1.1 Feito Por DANIEL",
                     font= ('Arial Black', '12'), bg = '#f0f0f0')
        self.dois.grid(row = 0, column = 2, sticky = S, padx = 20, pady = 20,
                  rowspan = 20, columnspan = 20)
        
  
    def criaconta1(self):
        self.usuario = self.login_entry.get()
        self.senha = self.senha_entry.get()
        if self.usuario == '' or self.senha == '':
            self.texto['text'] = 'Digite Usuário e Senha'
        else:
             criaconta(self.usuario, self.senha)
             self.texto['text'] = 'Usuario Criado com Sucesso!'
    
    def verificasenha(self):
        self.usuariologin = self.login_entry.get()
        self.senhalogin = self.senha_entry.get()
        mostra, nome, number = login(self.usuariologin, self.senhalogin)
        if mostra:
            self.login.destroy()
            self.senha.destroy()
            self.b1.destroy()
            self.b2.destroy()
            self.dois.destroy()
            self.login_entry.destroy()
            self.senha_entry.destroy()
            self.ranking.destroy()
            self.txt1.destroy()
            self.txt2.destroy()
            self.txt3.destroy()
            self.texto.destroy()
            self.cinza2.destroy()
            self.branco2.destroy()
            Questoes(nome, number, root)
        else:
            self.texto['text'] = 'Usuário/Senha Inválidos'


class Questoes:
    def __init__(self, nome, number, master=None):
        self.nome = nome
        self.number = number
        self.imge = PhotoImage(file = "img/fundoinvestimento.png") 
        self.imge1 = self.imge.subsample(1, 1) 
        self.imge12 = Label(master, image = self.imge1)
        self.imge12.grid(row = 0, column = 2,
                        columnspan = 2, rowspan = 2, padx = 5, pady = 5)

        self.target = PhotoImage(file = "img/target.png") 
        self.target1 = self.target.subsample(1, 1) 
        self.target2 = Label(master, image = self.target1)
        self.target2.grid(row = 0, column = 2, sticky= NW,
                        columnspan = 2, rowspan = 2, padx = 25, pady = 50)

        self.target2 = PhotoImage(file = "img/target.png") 
        self.target21 = self.target2.subsample(1, 1) 
        self.target22 = Label(master, image = self.target21)
        self.target22.grid(row = 0, column = 2, sticky= NW,
                        columnspan = 2, rowspan = 2, padx = 25, pady = 100)

        self.fundoquest = PhotoImage(file = "img/fundoquest.png") 
        self.fundoquest1 = self.fundoquest.subsample(1, 1) 
        self.fundoquest2 = Label(master, image = self.fundoquest1)
        self.fundoquest2.grid(row = 0, column = 2, sticky= NE,
                        columnspan = 2, rowspan = 2, padx = 25, pady = 50)

        self.usuario = Label(master, text= f'Conta: {nome}',
                             font=('Arial Black', '12'), bg= '#555', fg='white')
        self.usuario.grid(row= 0, column= 2, sticky = NW, padx = 50, pady= 55)

        self.conta = Label(master, text= f'R$ {number},00',
                             font=('Arial Black', '12'), bg= '#555', fg='white')
        self.conta.grid(row= 0, column= 2, sticky = NW, padx = 50, pady= 105)

        self.pergunt = Label(master, text= "",
                             font=('Arial Black', '10'), bg= '#555', fg='white')
        self.pergunt.grid(row= 0, column= 3, sticky = NE, padx = 40, pady= 70)
        
        self.b1 = Button(master, text = "Comprar", font= ('Arial Black', '12')) 
        self.b1.grid(row = 1, column = 3, sticky = SW, padx = 120, pady= 20)
        self.b1['command'] = self.input_quests

        self.b2 = Button(master, text = "Recusar", font= ('Arial Black', '12')) 
        self.b2.grid(row = 1, column = 3, sticky = SE, padx = 100, pady= 20)
        self.b2['command'] = self.recusou

        self.scal = Scale(master, from_=0, to=100, orient=HORIZONTAL, length=380,
                         tickinterval=10)
        self.scal.grid(row = 0, column = 3, sticky = SE, padx = 35, pady= 10)

        self.input_quests()

    def input_quests(self):
        self.quest1 = "01 - A ações da empresa CALT SA estavam em 0,98\n e foi para 1,45 em 10 dias e\n continua subindo. Deseja Investir ?"
        self.quest2 = "02 - A CALT SA subiu de 1,45 para 1,78. Investir ?"
        self.quest3 = "03 - Muito bem as ações da CALT SA subiram 300%, de 1,45 para 4,35. Porem estão com muitos dividendos!!. Deseja Investir ?"
        self.quest4 = "04 - A CALT SA teve uma queda incrivel em sua acões, muitos investidores perderam muito dinheiro!!. Deseja Investir agora que está barato ?"
        self.quest5 = "05 - Uma empresa grande está entrando no mercado financeiro, a MTREPS empresa alimenticía esta com valor de suas ações baixas !!. Deseja Investir ?"
        self.quest6 = "06 - A MTREPS teve ótimos resultados, e sua ações subiram um pouco !!. Deseja Investir novamente ?"
        self.quest7 = "07 - Explendido!! A empresa lucrou muito e sua ações subiram absurdamente, porém estão aflitos devido uma crise que se inicia no país. Deseja Investir ?"
        self.quest8 = "08 - A crise destruiu com as ações da empresa, porem continuam com suas ações no mercado!!. Deseja Investir ?"
        self.quest9 = "09 - A SIDES-SHIRTS empresa de produção de roupas de marcas caras, oscila suas ações no mercado!!. Deseja arriscar investir ?"
        self.quest10 = "10 - As SIDES-SHIRTS teve um bom desempenho porem, como dito suas ações oscilam de tempos em tempos!!. Deseja Investir ?"
        if self.pergunt['text'] == "":
            self.pergunt['text'] = self.quest1
        elif self.pergunt['text'] == self.quest1:
            self.pergunt['text'] = self.quest2
        elif self.pergunt['text'] == self.quest2:
            self.pergunt['text'] = self.quest3
        elif self.pergunt['text'] == self.quest3:
            self.pergunt['text'] = self.quest4
        elif self.pergunt['text'] == self.quest4:
            self.pergunt['text'] = self.quest5
        elif self.pergunt['text'] == self.quest5:
            self.pergunt['text'] = self.quest6
        elif self.pergunt['text'] == self.quest6:
            self.pergunt['text'] = self.quest7
        elif self.pergunt['text'] == self.quest7:
            self.pergunt['text'] = self.quest8
        elif self.pergunt['text'] == self.quest8:
            self.pergunt['text'] = self.quest9
        else:
            self.pergunt['text'] = self.quest10

    def comprou(self):
        print(self.scal.get())

    def recusou(self):
        if numbersq1 > 0:
            self.pergunt['text'] = f"As ações subiram {numbersq1}% em poucos dias"
        else:
            self.pegunt['text'] = f"As ações cairam  {numbersq1}% em poucos dias"


root = Tk()
root.title('O Grande Investidor')
root.configure(background='gray')
Questoes('daniel', '30000', root)
root.mainloop()
