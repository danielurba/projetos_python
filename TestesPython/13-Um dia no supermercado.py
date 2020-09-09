#names = ["Adam","Alex","Mariah","Martine","Columbus"]

#for name in names:
#  print (name)

#webster = {
#  "Aardvark" : "A star of a popular children's cartoon show.",
#  "Baa" : "The sound a goat makes.",
#  "Carpet": "Goes on the floor.",
#  "Dab": "A small amount."
#}
#for item in webster:
#    print (webster[item])

#a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#for variav in a:
#    if variav %2 == 0:
#print ("vaca")

def fizzcount (x):
    count = 0
    for gueter in x:
        if gueter == "fizz":
            count = count + 1
    return count
result = fizzcount(["fizz", "fizz", "cat", "fizz"])
print(result)   

for letter in "Codecademy":
  print (letter)   
# Empty lines to make the output pretty
print
print
word = "Programming is fun!"
for letter in word:
  # Only print out the letter i
  if letter == "i":
    print (letter)

