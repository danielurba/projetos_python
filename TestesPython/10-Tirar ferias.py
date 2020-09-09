def bigger (first, second):
    print (max (first, second))
    return True

def hotelcusto(noites):
    return 140 * noites

def planeridecost(city):
    if city == "charlotte":
        return 183
    elif city == "tampa":
        return 220
    elif city == "pittsburgh":
        return 222
    elif city == "los angeles":
        return 475
    
def rentalcarcust(days):
    custo = days * 40
    if days >= 7:
        return custo - 50
    elif days >= 3:
        return custo - 20
        
def tripcost(city, days, spendigmoney):
    return hotelcusto(days) + rentalcarcust(days) + planeridecost(city) + spendigmoney
    
print (tripcost("los angeles",5 , 600))
