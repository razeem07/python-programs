class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

# ExpressShipping ==> weight*20

# StandardShipping ==> weight*10

class ExpressShipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*20)


class StandardShipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*10)

Express_instance=ExpressShipping()
Express_instance.calculate_shipping_cost(20)
Standard_instance=StandardShipping()
Standard_instance.calculate_shipping_cost(10)




# class 
# object
# __init__
# __str__
# super()
# self
# inheritance
    #  single
    # multilevel
    # multiple
# polimoraphism
    # method_overloading
    # method_overriding

# Abstraction
    # hiding implimentation details