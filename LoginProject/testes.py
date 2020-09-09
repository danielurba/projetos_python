from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.msg = Label(self.primeiroContainer, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()

        self.msg1 = Label(self.segundoContainer, text="segundo widget")
        self.msg1["font"] = ("Verdana", "10", "italic", "bold")
        self.msg1.pack()
        
        self.sair = Button(self.primeiroContainer)
        self.sair["text"] = "Criar Imagem"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.msg1.destroy
        self.sair.pack()

        self.sair = Button(self.primeiroContainer)
        self.sair["text"] = "Destuir Imagem"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.msg1.destroy
        self.sair.pack(side= RIGHT)

        

root = Tk()
Application(root)
root.mainloop()
