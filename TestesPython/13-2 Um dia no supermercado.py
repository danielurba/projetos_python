prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
    }
stock = {"banana" : 6,
         "apple" : 0,
         "orange" : 32,
         "pear" : 15
         }
#for key in prices:
#    print (key)
#    print (("Preço: %s") % prices[key])
#    print (("Estoque: %s") % stock[key])
    
totals = 0
for thy in prices:
    thy = prices[thy] * stock[thy]
    totals += thy
print (("Valor total dos produtos: %s") % totals)    

food = ["pear", "apple", "banana"]
def computebill(food):
    total = 0
    estoque = 0
    for nume in food:
        if stock[nume] > 0:
            total += prices[nume]
            stock[nume] -= 1
    return total
    print(total)
print (("Valor dos Produtos No Carrinho: %s Reais") % computebill(food))
