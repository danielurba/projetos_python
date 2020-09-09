

response = 'y'

answer = "Left"
if answer == "Left":
    print ("Esta é a sala de abuso verbal, seu monte de excrementos de papagaios!")
    
# A declaração de impressão acima será impressa no console?
# Defina a resposta como 'Y', se você acha, e 'N', se não.


def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print (using_control_once())
print (using_control_again())


answer = "É apenas um arranhão!"

def black_knight():
    if answer == "É apenas um arranhão!":
        return True
    else:             
        return False        # Make sure this returns False

def french_soldier():
    if answer == "Vá embora, ou eu vou provocá-lo uma segunda vez!":
        return True
    else:             
        return False        # Make sure this returns False


def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

# Complete as instruções if e elif!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 :
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
# Isso deve imprimir um "A"   
print (grade_converter(92))

# Isso deve imprimir um "C"
print (grade_converter(70))

# Isso deve imprimir um "F"
print (grade_converter(61))
