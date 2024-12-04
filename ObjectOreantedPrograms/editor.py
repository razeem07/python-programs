class Editor:

    def __init__(self,name,vendor):

        self.name=name
        self.vendor=vendor

    def display(self):

        print(self.name,self.vendor)

    def __str__(self):

        return self.name
    
editor_instance1=Editor("pycharm","jetbrains")
editor_instance2=Editor("intellij","jetbrains")
editor_instance3=Editor("vscode","micosft")

print(editor_instance1)

