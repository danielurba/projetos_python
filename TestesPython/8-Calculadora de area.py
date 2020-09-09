# Pragrama que calcula areas de circulos e triangulos !!!
print ("Calculadora de Área Iniciada !!")
option = input("Coloque C para calculo de Circulo e T para Triangulo:")
if option == "c":
    radius = float(input("Qual e o raio do circulo ? "))
    pi = 3.14159
    area = pi * radius **2
    print (area)
elif option == "t":
    base = float(input("Qual e a base do triangulo ? "))
    altura = float(input("Qual e a altura do triangulo ? "))
    area = (base * altura) / 2
    print (area)
else:
    print ("Comando Inválido !!! ")
print ("Seu calculo foi feito com Sucesso, Até Mais ! ")
