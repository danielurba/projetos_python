class car (object):
    condition = "Novo"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    def displaycar(self):
        print("O carro é %s a cor e %s e o ano e %s" % (self.model,self.color,str(self.mpg)))
    def drivecar(self):
        self.condition = "Usado"

class eletriccar(car):
    def __init__(self, model, color, mpg, baterrytipe):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.baterrytipe = baterrytipe
    def drivecar(self):
        self.condition = "Carro Novo"
    
mycar = eletriccar("Palio", "Branca", 2000, "Vpower")
print(mycar.condition)
mycar.drivecar()
print(mycar.condition)

class point3d(object):
    def __init__(self, x , y ,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d,%d,%d)" % (self.x, self.y, self.z)

mypoint = point3d(1, 2, 3)
print(mypoint)
