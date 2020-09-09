# um calendário básico com o qual o usuário poderá interagir a partir da linha de comando. O usuário deve poder escolher:
#•	Ver o calendário
#•	Adicionar um evento ao calendário
#•	Atualizar um evento existente
#•	Excluir um evento existente
#O programa deve se comportar da seguinte maneira:
#1.	Imprimir uma mensagem de boas-vindas ao usuário
#2.	Solicitar que o usuário visualize, adicione, atualize ou exclua um evento no calendário
#3.	Dependendo da entrada do usuário: visualize, adicione, atualize ou exclua um evento no calendário
#4.	O programa nunca deve terminar, a menos que o usuário decida sair

from time import sleep,strftime

name = input("Qual seu nome ?: ")

calendar = {}

def welcome():
    print("Bem Vindo ao Calendario Agenda %s" % (name))
    print("Abrindo Calendario...")
    sleep(1)
    print("Hoje é " + strftime("%A %B Dia %d Ano 20%y"))
    print("Horário de agora é " + strftime("%H:%M:%S"))
    sleep(1)
    print("O que você gostaria de fazer?")

def startcalendar():
    welcome()
    start = True
    while start:
        userchoice = input("A para adicionar, U para atualizar, V para exibir, E para excluir e X para sair:")
        userchoice = userchoice.upper()
        if userchoice == "V":
            if len(calendar.keys()) < 1:
                print ("Calendario Vazio!")
            else:
                print(calendar)
        elif userchoice == "U":
            date = input("Qual Data?")
            update = input("Digite a Atualização:")
            calendar[date] = update
            print("Atualização Concluída!")
            print(calendar)
        elif userchoice == "A":
            event = input("Coloque o Evento:")
            date = input("Insira a data do evento (MM\DD\YYYY):")
            if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print("Uma data inválida foi inserida!!")
                tryagain = input("Tentar novamente? S/N:")
                tryagain = tryagain.upper()
                if tryagain == "S":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print("Evento add com Sucesso!")
                print(calendar)
        elif userchoice == "E":
            if len(calendar.keys()) < 1:
                print ("Calendario Vazio!")
            else:
                event = input("Qual evento?:")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print("Evento excluido com Sucesso!")
                        print(calendar)
                    else:
                        print("Evento não existe para ser excluido!")
        elif userchoice == "X":
            start = False
        else:
            print("Comando Inválido Inserido!!")
startcalendar()


