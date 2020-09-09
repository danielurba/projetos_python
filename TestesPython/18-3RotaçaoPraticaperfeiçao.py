#def iseven(x):
#    if x % 2 == 0:
#        return True
#    else:
#        return False
    
#def isint(x):
#    absolute = abs(x)
#    raounded = round(absolute)
#    return absolute - round == 0

#def digitsum(n):
#    total = 0
#    string = str(n)
#    for item in string:
#        total += int(item)
#    return total
#print(digitsum(1234))

#def factorial(x):
#    total = 1
#    while x > 0:
#        total *= x
#        x -= 1
#    return total
#print(factorial(6))

#def isprime(x):
#    if x < 2:
#        return False
#    else:
#        for n in range(2,x-1):
#            if x % n == 0:
#                return False
#            return True
#print(isprime(13))

#def reverse(text):
#    word = ""
#    l = len(text) - 1
#    while l >= 0:
#        word = word + text[l]
#        l -= 1
#    return word
#print(reverse("helloworld"))

#def antivogal(text):
#    result = ""
#    vogal = "aeiouAEIOU"
#    for char in text:
#        if char not in vogal:
#            result += char
#    return result
#print(antivogal("HEllo BoOk"))

#score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
#             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
#             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
#             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
#             "x": 8, "z": 10}

#def scrabblescore(word):
#    word = word.lower()
#    total = 0
#    for letters in word:
#        for letter in score:
#            if letters == letter:
#                total = total + score[letter]
#        return total

#print(scrabblescore("Pizza"))
        
def censor (text,word):
    words = text.split()
    result = ""
    stars = "*" * len(word)
    count = 0
    for i in words:
        if i == words:
            words[count] = stars
        count += 1
    result =" ".join(words)
    return result

print(censor("hack e wack hack", "hack"))

def count(sequence,item):
    count = 0
    for number in sequence:
        if number == item:
            count += 1
    return count
print(count([1,2,3,3,6,6,6,7],6))

def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res
print (purify([1,2,3,4]))

def product(x):
    total = 1
    for item in x:
        total = total * item
    return total
print(product([5,5,4]))

def removedupli(inputl):
    if inputl == []:
        return[]
    inputl = sorted(inputl)
    outputl = [inputl[0]]
    for i in inputl:
        if i > outputl[-1]:
            outputl.append(i)
    return outputl
print(removedupli([1,1,2,2]))
    
def median(lst):
    sortedlist = sorted(lst)
    if len(sortedlist) % 2 != 0:
        index = len(sortedlist)//2
        return sortedlist[index]
    elif len(sortedlist) % 2 == 0:
        index1= len(sortedlist)//2 - 1
        index2= len(sortedlist)//2
        mean = (sortedlist[index1] + sortedlist[index2])/2.0
        return mean
print(median([2,4,5,9]))
