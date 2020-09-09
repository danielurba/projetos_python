#import math
#math.sqrt

#from math import sqrt

#from module import *

#import math
#todomundo = dir(math)
#print (todomundo)


def biggest_number(*args):
  print (max(args))
  return max(args)
    
def smallest_number(*args):
  print (min(args))
  return min(args)

def distance_from_zero(arg):
  print (abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

def numero(*n):
    print (max(n))

numero(24, 56, 75, 37, 67)

def tres(*z):
    print (min(z))

tres(8, 12, 44, 55)

def abesolute(b):
    print (abs(b))

abesolute(-43)

print (type(34))
print (type(12.5))
print (type("daniel"))

 
def shotdown(s):
    if s == "sim":
        return "nao esta acabado"
    elif s == "nao":
        return "esta acabado"
    else:
        return "sorry"
    shotdown(s)
 
s = "sim"
print (shotdown(s))

import math
result = math.sqrt(13689)
print (result)

def distanciadozero(d):
    if type(d) == int or type(d) == float:
        return abs(d)
    else:
        return "Nope"
distanciadozero("daniekl")
