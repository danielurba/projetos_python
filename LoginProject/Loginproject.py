from tkinter import *

master = Tk()

img = PhotoImage(file = "dinheirodolares.png") 
img1 = img.subsample(1, 1) 
Label(master, image = img1).grid(row = 0, column = 2, 
        columnspan = 2, rowspan = 2, padx = 5, pady = 5) 

img2 = PhotoImage(file = "dinheirodolares2.png") 
Label(master, image = img2).grid(row = 0, column = 2, sticky = SE,
                                 padx = 20, pady = 20, rowspan = 20,
                                 columnspan = 20)

def painel():
    login = Label(master, text = "Login", font= ('Calibri', '12'), bg = 'white') 
    senha = Label(master, text = "Senha", font= ('Calibri', '12'), bg = 'white') 


    login.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 40) 
    senha.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 100) 

    e1 = Entry(master, font= ('Calibri', '12'), bg = 'white') 
    e2 = Entry(master, font= ('Calibri', '12'), bg = 'white')

    e1.grid(row = 0, column = 2, sticky = NW, padx = 80, pady = 40) 
    e2.grid(row = 0, column = 2, sticky = NW, padx = 80, pady = 100) 

    b1 = Button(master, text = "Iniciar") 
    b1.grid(row = 0, column = 2, sticky = W, padx = 130)
    b1['command'] = verificasenha

    dois = Label(master, text = "Olá Bem Vindo ao Jogo O Grande Investidor - Project\n Feito Por DANIEL",
                  font= ('Calibri', '12'), bg = 'white')
    dois.grid(row = 0, column = 3, sticky = N, padx = 20, pady = 20,
              rowspan = 20, columnspan = 20)

def verificasenha():
    usuario = e1.get()
    senha = e2.get()
    if usuario == 'daniel' and senha == '1234':
        print('Conseguiu')

painel()
mainloop() 
