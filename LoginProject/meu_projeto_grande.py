from tkinter import *

class Application:
    def __init__(self, master=None):
        self.img = PhotoImage(file = "dinheirodolares.png") 
        self.img1 = self.img.subsample(1, 1) 
        self.img12 = Label(master, image = self.img1)
        self.img12.grid(row = 0, column = 2,
                        columnspan = 2, rowspan = 2, padx = 5, pady = 5) 

        self.img2 = PhotoImage(file = "dinheirodolares2.png") 
        self.img22 = Label(master, image = self.img2)
        self.img22.grid(row = 0, column = 2, sticky = SE,
                                         padx = 20, pady = 20, rowspan = 20,
                                         columnspan = 20)

        self.login = Label(master, text = "Login", font= ('Calibri', '12'), bg = 'white') 
        self.senha = Label(master, text = "Senha", font= ('Calibri', '12'), bg = 'white')
        self.testo = Label(master, text = "", font= ('Calibri', '12'), bg = 'white')

        self.login.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 40)
        self.senha.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 100)
        self.testo.grid(row = 0, column = 2, sticky = SW, padx = 100, pady = 20)

        self.login_entry = Entry(master, font= ('Calibri', '12'), bg = 'white') 
        self.senha_entry = Entry(master, font= ('Calibri', '12'), bg = 'white')
        self.senha_entry['show'] = '*'

        self.login_entry.grid(row = 0, column = 2, sticky = NW, padx = 80, pady = 40) 
        self.senha_entry.grid(row = 0, column = 2, sticky = NW, padx = 80, pady = 100) 

        #self.b1 = Button(master, text = "Iniciar") 
        #self.b1.grid(row = 0, column = 2, sticky = W, padx = 130)
        #self.b1['command'] = self.verificasenha

        self.dois = Label(master, text = "Olá Bem Vindo ao Jogo O Grande Investidor - Project\n Feito Por DANIEL",
                     font= ('Calibri', '12'), bg = 'white')
        self.dois.grid(row = 0, column = 3, sticky = N, padx = 20, pady = 20,
                  rowspan = 20, columnspan = 20)
        
  
    #Método verificar senha
    def verificasenha(self):
        self.usuario = self.login_entry.get()
        self.senha = self.senha_entry.get()
        if self.usuario == 'daniel' and self.senha == '1234':
            self.testo['text'] = 'LOGADO'
        else:
            self.testo['text'] = 'NÂO LOGADO'
  

root = Tk()
root.title('O Grande Investidor')
root.configure(background='gray')
Application(root)
root.mainloop()
