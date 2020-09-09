from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer['bg'] = 'white'
        self.primeiroContainer.pack()
  

        self.img = PhotoImage(file='dinheirodolares.png')
        self.img.subsample(1, 1) 
        self.labelimg = Label(image=self.img)
        self.labelimg.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        self.titulo = Label(root, text='Olá Bem Vindo ao Jogo\n'
                            'O Grande Investidor - Project\n' 
                            'Feito Por DANIEL')
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.autenticar = Button(root)
        self.autenticar["text"] = "Iniciar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack(side=LEFT, anchor=SW, padx= 20, pady=20)

        self.autenticar = Button(root)
        self.autenticar["text"] = "Scores"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar.pack(side= RIGHT, anchor=SW, padx= 20, pady=20)
  
        self.mensagem = Label(root, text="", font=self.fontePadrao)
        self.mensagem.pack(side=BOTTOM, anchor=S, padx= 20, pady=20)
  
    #Método verificar senha
    def verificaSenha(self):
        if self.titulo['text'] == 'Bem-Vindo ao Jogo O grande investidor':
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"
  

root = Tk()
root.title('O Grande Investidor')
root.configure(background='gray')
root.geometry('739x415')
Application(root)
root.mainloop()
