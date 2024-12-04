class GrandParent:

    def m(self):

        print("Grandparent class m  method")

class Parent:

    def m(self):

        print("Parent class m method")

class Child(Parent,GrandParent):

    def m3(self):

        print("Child class m3 method ")


child_instance=Child()
child_instance.m3()
child_instance.m()