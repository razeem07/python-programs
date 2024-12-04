from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod    
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass
   
    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class Vscode(Editor):

    def open(self):
        print("vscode open")

    def write(self):
        print("vscode write method")

    def debug(self):
        print("vscode debug")

    def execute(self):
        print("vscode execute")

vscode_instance=Vscode()
vscode_instance.open()
vscode_instance.write()
vscode_instance.debug()
vscode_instance.execute()