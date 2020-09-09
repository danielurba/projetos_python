#my_list = [1,9,3,8,5,7]

#for number in my_list:
#    print (2 * number)

#start_list = [5, 3, 1, 2, 4]
#square_list = []

#for number in start_list:
#    square_list.append(number ** 2)
#square_list.sort()

#print (square_list)

# Assigning a dictionary with three key-value pairs to residents:
#residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

#print (residents['Puffin'])
#print (residents["Sloth"])
#print (residents["Burmese Python"])


menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])
menu["frango"] = 12.50
menu["batata"] = 5.50
menu["arroz"] = 9.75
print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)


# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines
# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper"] = 12
zoo_animals["Artic Exhibit"] = 44

print (zoo_animals)

#backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
#backpack.remove("dagger")
#print (backpack)

inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()
inventory["pocket"] = ["seashell", "strang berry", "lint"]
inventory['backpack'].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] = inventory["gold"] + 50
print (inventory)
