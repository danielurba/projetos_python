# import tkinter module 
from tkinter import *
  
# criando a janela principal do tkinter / nível superior
master = Tk() 
  
# isso criará um widget de etiqueta
l1 = Label(master, text = "Login") 
l2 = Label(master, text = "Senha") 
dois = Label(master, text = f'{11}')

# método de grade para organizar as etiquetas nos respectivos
# linhas e colunas conforme especificado
l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
l2.grid(row = 1, column = 0, sticky = W, pady = 2) 
dois.grid(row = 2, column = 0, sticky = W, pady = 2)

# widgets de entrada, usados para receber entradas do usuário
e1 = Entry(master) 
e2 = Entry(master)

# adicionando imagem (lembre-se de que a imagem deve ser PNG e não JPG)
img = PhotoImage(file = "dinheirodolares.png") 
img1 = img.subsample(1, 1) 
  
# definindo a imagem com a ajuda da etiqueta 
Label(master, image = img1).grid(row = 0, column = 2, 
       columnspan = 2, rowspan = 2, padx = 5, pady = 5) 
  
# isso organizará widgets de entrada
e1.grid(row = 0, column = 1, pady = 2) 
e2.grid(row = 1, column = 1, pady = 2) 
  
# widget de botão de verificação 
c1 = Checkbutton(master, text = "Preserve") 
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2) 
  
  
# widget de botão 
b1 = Button(master, text = "Iniciar") 
  
# organizando widgets de botão
b1.grid(row = 2, column = 2, sticky = E) 
  
# loop infinito que pode ser finalizado
# por interrupção do teclado ou mouse

mainloop() 
