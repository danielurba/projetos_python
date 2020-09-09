class bankaccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Conta: {self.name} = Saldo: {self.balance},00 R$"
    
    def showbalance(self):
        print("Saldo: %s" % (self.balance))

    def deposit(self, amount):
        if amount <= 0:
            print("Error")
            return
        else:
            print("Deposito: %s" % (amount))
            self.balance += amount
            myacount.showbalance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Dinheiro Indisponivel!")
            return
        else:
            print("Sacando: %s" % (amount))
            self.balance -= amount
            myacount.showbalance()

myacount = bankaccount(input("Nome para a conta: "))
print(myacount)
myacount.deposit(int(input("Depositar quanto?: ")))
myacount.withdraw(int(input("Sacar quanto?: ")))
print(myacount)
