#class Fruit(object):
#  """A class that makes various tasty fruits."""
#  def __init__(self, name, color, flavor, poisonous):
#    self.name = name
#    self.color = color
#    self.flavor = flavor
#    self.poisonous = poisonous

#  def description(self):
#    print (*"I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

#  def is_edible(self):
#    if not self.poisonous:
#      print ("Yep! I'm edible.")
#    else:
#      6print ("Don't eat me! I am super poisonous.")
#lemon = Fruit("lemon", "yellow", "sour", False)
#lemon.description()
#lemon.is_edible()

class Animal():
    vivo = True
    health = "Good"
    def __init__(self, name, age, ishungry):
        self.ishungry = ishungry
        self.name = name
        self.age = age
    def descrption(self):
        print(self.name)
        print(self.age)

sloth = Animal("Frederico", 15, True)
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
hippo = Animal("Daniel", 22, True)

print(hippo.health)
print(sloth.health)
print(hippo.descrption())
print (zebra.name, zebra.age, zebra.ishungry, giraffe.vivo)
print (giraffe.name, giraffe.age, giraffe.ishungry, giraffe.vivo)
print (panda.name, panda.age, panda.ishungry, panda.vivo)

