#phrase = "A bird in the hand..."
#for char in phrase:
#    if char == "A" or char == "a":
#        print("X",)
#    else:
#        print(char,)
        
#numbers  = [7, 9, 12, 54, 99]
#for num in numbers:
#  print (num)
#for quad in numbers:
#    print(quad**2)

#d = {'x' : 9, 'y' : 10, 'z' : 20}
#for key in d:
#    if d[key] == 20:
#        print("Isso e 20")

choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
  print (index + 1, item)


list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print(max(a,b))


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') # (It actually is.)
    print ('A', f)
else:
    print ('A fine selection of fruits!')

