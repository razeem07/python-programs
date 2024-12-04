class GrandParent:

    def m(self):

        print("Grandparent class m1 method")

class Parent:

    def m(self):

        print("Parent class m2 method")

class Child(Parent,GrandParent):

    def m3(self):

        print("Child class m3 method ")


child_instance=Child()
child_instance.m3()
child_instance.m2()
child_instance.m1()