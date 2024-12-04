# polymorphism   (more than one form)
# method_overloading
# method_overriding



# method_overloading ==>  same method name and different numbers of parameters

class Operations :

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

obj=Operations()

obj.add(10,20,30)


# obj.add(10,20) #error



# method_overriding ==> different class and should inherite from object class and signature name should be same 

class Parent:
    def mobile(self):
        print("samsung")
    
class Child(Parent):
    def mobile(self):
        print("iphone")

child_instance=Child()
child_instance.mobile()