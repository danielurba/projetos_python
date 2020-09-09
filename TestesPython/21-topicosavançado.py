#mydict = {
#"idade" : 22,
#"dia" : 25,
#"mes" : "setembro"
#}
#for key in mydict:
#    print(key,mydict[key],)
#for letter in "setembro":
#    print(letter,)
    
#print(mydict.items())
#print(mydict.values())

#evens_to_50 = [i for i in range(51) if i % 2 == 0]
#print (evens_to_50)

#evensquares = [x ** 2 for x in range(1,11) if (x ** 2) % 2 == 0]
#print(evensquares)

#cubesbyfour = [x ** 3 for x in range(1,10) if ((x ** 3) % 4) == 0]
#print(cubesbyfour)

mylist = range(101)
lista = list(mylist[::-10])
print(lista)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (list(filter(lambda x: x == "Python", languages)))

squares = [x ** 2 for x in range(30,70)]
print(list(filter(lambda x: x % 2 == 0, squares)))

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = list(filter(lambda x: x != "X", garbled))
print(message)


