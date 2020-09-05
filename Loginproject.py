# -*- coding: utf-8 -*-
from tkinter import *

master = Tk()

img = PhotoImage(file = "dinheirodolares.png") 
img1 = img.subsample(1, 1) 
Label(master, image = img1).grid(row = 0, column = 2, 
       columnspan = 2, rowspan = 2, padx = 5, pady = 5) 

login = Label(master, text = "Login", font= ('Calibri', '12'), bg = 'white') 
senha = Label(master, text = "Senha") 


login.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 40) 
senha.grid(row = 0, column = 2, sticky = NW, padx = 20, pady = 100) 

e1 = Entry(master) 
e2 = Entry(master)

e1.grid(row = 0, column = 2, sticky = NW, padx = 80, pady = 40) 
e2.grid(row = 0, column = 2, sticky = NW, padx = 80, pady = 100) 

b1 = Button(master, text = "Iniciar") 
b1.grid(row = 0, column = 2, sticky = W, padx = 100) 

img2 = PhotoImage(file = "dinheirodolares2.png") 
Label(master, image = img2).grid(row = 0, column = 3, sticky = S,
                                 padx = 20, pady = 20, rowspan = 20,
                                 columnspan = 20)

dois = Label(master, text = "Olá Bem Vindo ao Jogo\n O Grande Investidor - Project\n Feito Por DANIEL")
dois.grid(row = 0, column = 3, sticky = NE, padx = 80, pady = 50)

mainloop() 
