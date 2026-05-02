from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def move_forward(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class PetrolEngine(Engine):
    
    def move_forward(self):
        print("petrol Engine Car is moving forward")

    def stop(self):
        print("petrol Engine car stopped")


class DieselEngine(Engine):
    
    def move_forward(self):
        print("Diesel Engine Car is moving forward")

    def stop(self):
        print("Diesel Engine car stopped")

class ElectricEngine(Engine):
    
    def move_forward(self):
        print("Electric Engine Car is moving forward")

    def stop(self):
        print("Electric Engine car stopped")

class car:

    def move_forwared(self, Engine_Type: Engine):
        Engine_Type.move_forward()

    def stop(self, Engine_Type: Engine):
        Engine_Type.stop()


cheverlot = car()
cheverlot.move_forwared(PetrolEngine())

audi = car()
audi.move_forwared(ElectricEngine())

tata_punch = car()
tata_punch.move_forwared(DieselEngine())

cheverlot.stop(PetrolEngine())
audi.stop(ElectricEngine())
tata_punch.stop(DieselEngine())
