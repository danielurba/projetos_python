"""
Jogo amigo secreto, roda nomes aleartorios que foram add pelo usuario
E retira o nome do jogo para proximo usuario rodar o jogo de novo, ate
tirar todos os nomes inseridos.
"""
from random import choice
from tkinter import *
from time import sleep

class Application:
    def __init__(self, master=None):
        self.img = PhotoImage(file = "amigosecretovirtual.png") 
        self.img1 = self.img.subsample(1, 1) 
        self.img12 = Label(root, image = self.img1)
        self.img12.grid(row = 0, column = 2,
                        columnspan = 2, rowspan = 2, padx = 5, pady = 5) 

        self.img2 = PhotoImage(file = "icon.png") 
        self.img22 = Label(root, image = self.img2)
        self.img22.grid(row = 0, column = 2, sticky = SE,
                                         padx = 20, pady = 20, rowspan = 20,
                                         columnspan = 20)

        self.login = Label(root, text = "Jogo Amigo Secreto",
                           font= ('Arial Black', '12'))
        self.login['bg'] = 'gray'
        self.login.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 40) 

        self.b1 = Button(root, text = "Iniciar") 
        self.b1.grid(row = 0, column = 2, sticky = W, padx = 20)
        self.b1["font"] = 'Arial Black', '12'
        self.b1["command"] = self.iniciar

        self.b2 = Button(root, text = "Sair") 
        self.b2.grid(row = 0, column = 2, sticky = W, padx = 100)
        self.b2["font"] = 'Arial Black', '12'
        self.b2["command"] = root.destroy

        self.dois = Label(root, text = "Jogo para tirar amigos aleatórios para amigo secreto",
                     font= ('Arial Black', '12'))
        self.dois['bg'] = 'gray'
        self.dois.grid(row = 0, column = 3, sticky = N, padx = 5, pady = 20,
                  rowspan = 20, columnspan = 20)


    def iniciar(self):
        self.nomes = []
        self.img = PhotoImage(file = "amigosecretovirtual.png") 
        self.img1 = self.img.subsample(1, 1) 
        self.img12 = Label(root, image = self.img1)
        self.img12.grid(row = 0, column = 2,
                        columnspan = 2, rowspan = 2, padx = 5, pady = 5)

        self.lista = Label(root, text = "", font= ('Arial Black', '12'))
        self.lista['bg'] = 'gray'
        self.lista.grid(row = 0, column = 3, sticky = E, padx = 20, pady = 40)

        self.entrada = Entry(root)
        self.entrada.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 100)
        self.entrada["font"] = 'Arial Black', '12'
        self.entrada.bind('<Return>', self.adiciona_lista)

        self.vizulis = Button(root, text= "Vizualizar Lista")
        self.vizulis.grid(row = 0, column = 2, sticky = SW, padx = 20)
        self.vizulis["font"] = 'Arial Black', '12'
        self.vizulis["command"] = self.vizualiza_lista

        self.removamig = Button(root, text= "Tirar um Amigo Secreto")
        self.removamig.grid(row = 0, column = 2, sticky = SW, padx = 20, pady = 50)
        self.removamig["font"] = 'Arial Black', '12'
        self.removamig["command"] = self.tira_amigo

        self.login = Label(root, text = "Jogo Amigo Secreto", font= ('Arial Black', '12'))
        self.login['bg'] = 'gray'
        self.login.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 40)
        
    def adiciona_lista(self, entrada):
        self.nomes.append(self.entrada.get().title())
        self.entrada.delete(0, END)

    def vizualiza_lista(self):
        self.listavazia2 = any(self.nomes)
        if self.listavazia2 == False:
            self.lista["text"] = 'Lista Vazia'
        else:
            self.lista["text"] = self.nomes
            
    def tira_amigo(self):
        self.listavazia = any(self.nomes)
        if self.listavazia == False:
            self.lista["text"] = "Lista Vazia"
        else:
            self.remov = choice(self.nomes)
            self.nomes.remove(self.remov)
            self.lista["text"] = f' Seu amigo Secreto é {self.remov}'
        

root = Tk()
root.title('Jogo Amigo Secreto')
root.configure(background='gray')
root.iconbitmap('favicon.ico')
Application(root)
root.mainloop()




