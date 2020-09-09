class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()


#class Shape(object):
#    """Makes shapes!"""
#    def __init__(self, number_of_sides):
#        self.number_of_sides = number_of_sides

#class triangle(Shape):
#    def __init__(self, side1, side2, side3):
#        self.side1 = side1
#        self.side2 = side2
#        self.side3 = side3

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class parttime(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def fulltime(self, hours):
        return super(parttime,self).calculate_wage(hours)

milton = parttime("daniel")
print(milton.fulltime(10))
