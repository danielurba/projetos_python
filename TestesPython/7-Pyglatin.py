pyg = "ay"
original = input("Qual seu nome ? ")
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    newword = (word + first + pyg)
    newword = newword[1:len(newword)]
    print (original)
    print (newword)
else:
    print ("Vazio!")
