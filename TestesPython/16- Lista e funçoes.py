#n = [1,5,4,6]
#n[1] = n[1]*4
#n.append(3)
#n.pop(1)
#n.remove(1)
#print (n)
#number = 5

#def my_function(x):
#    return x * 3

#print (my_function(number))

#m = 5
#n3 = 13
#def add_function(x,y):
#    return x+y
#print (add_function(m, n3))

#n2 = "Hello"
#def string_function(s):
#    return"world"
#print (string_function(n2))

#def list_function(x):
#    x[1]=x[1]+3
#    return x

#n = [3, 5, 7]
#print (list_function(n))

#n3 = [1,5,6,7]
#def listextender(lst):
#    n3.append(9)
#    return n3
#print(listextender(n3))

n4 = [3,5,7]
#def printlist(x):
#    for ide in range(0, len(x)):
#        print(x[ide])
#print (printlist(n4))

#def doublelist(x):
#    for ida in range(0,len(x)):
#        x[ida] = x[ida] * 2
#        print(x[ida])
#print(doublelist(n4))

#def my_function(x):
#  for i in range(0, len(x)):
#    x[i] = x[i]
#  return x
#print (my_function(range(3)))

def total(h):
    result = 0
    for ity in range(0,len(n4)):
        result += h[ity]
        return result
print(total(n4))

n = ["Michael", "Lieberman"]
def join_strings(words):
    result = ""
    for item in range(len(words)):
        result += words[item]
    return result
print (join_strings(n))

m = [1, 2, 3]
n = [4, 5, 6]
def joinlist(x,y):
    return x + y
print (joinlist(m,n))

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
    results = []
    for numbers in lists:
        for item in numbers:
            results.append(item)
    return results
print (flatten(n))

