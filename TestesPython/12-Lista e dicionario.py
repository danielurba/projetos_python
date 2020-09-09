
zoo_animals = ["pangolin", "cassowary", "sloth", "Macaco"]
zoo_animals[3] = "Vaca"

if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])

numbers = [5, 6, 7, 8]

print ("Adding the numbers at indices 0 and 2...")
print (numbers[0] + numbers[2])
print ("Adding the numbers at indices 1 and 3...")
print (numbers[1] + numbers[3])


#suitcase = [] 
#suitcase.append("sunglasses")
#suitcase.append("Sunga")
#suitcase.append("calça")
#suitcase.append("camisa")
#list_length = len(suitcase)

#print ("Existem %d na Mala" % (list_length))
#print (suitcase)


suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
# The first and second items (index zero and one)
first = suitcase[0:2]
# Third and fourth items (index two and three)
middle = suitcase[2:4]
# The last two items (index four and five)
last = suitcase[4:6]
print(first)
print(middle)
print(last)

animals = "catdogfrog"
# The first three characters of animals
cat = animals[:3]
# The fourth through sixth characters
dog = animals[3:6]
# From the seventh character to the end
frog = animals[6:]
print(cat)
print(dog)
print(frog)


animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")
print (animals)


