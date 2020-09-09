grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print ("Grades:", grades)

def printgrades(gradesinput):
    for grade in grades:
        print(grade)

def gradessum(scores):
    total = 0
    for score in scores:
        total += score
        return total

def gradesaverage(gradesinput):
    sumofgrade = gradessum(gradesinput)
    averagem = sumofgrade / float(len(gradesinput))
    return averagem

def gradesvariance(scores):
    average = gradesaverage(scores)
    variance = 0
    for score in scores:
        variance += (average - score)**2
        return variance / len(scores)

def gradesstd(variance):
    return variance ** 0.5
variance = gradesvariance(grades)

for grade in grades:
    print(grade)
    
print(gradessum(grades))
print(gradesaverage(grades))
print(gradesvariance(grades))
print(gradesstd(variance))

        
