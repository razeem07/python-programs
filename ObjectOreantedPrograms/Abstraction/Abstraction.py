
from abc import ABC,abstractmethod

class Bike(ABC):
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def acceleration(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Hunter(Bike):

    def start(self):
        print("Hunter start method")

    def acceleration(self):
        print("Hunter acceleration method")

    def stop(self):
        print("Hunter stop ")


hunter_instance=Hunter()
hunter_instance.start()
hunter_instance.stop()
hunter_instance.acceleration()
