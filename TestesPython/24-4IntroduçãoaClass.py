class triangle(object):
    numberofsides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def checkangle(self):
        if (self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False

class equilateral(triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.anlge2 = self.angle
        self.angle3 = self.angle

mytriangle = triangle(90, 30, 60)
print(mytriangle.numberofsides)
print(mytriangle.checkangle())
