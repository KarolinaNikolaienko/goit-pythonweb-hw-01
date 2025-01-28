from abc import ABC, abstractmethod
import logging

logging.basicConfig(format='%(asctime)s %(message)s',
                    level=logging.INFO,
                    handlers=[logging.FileHandler("task_1.log"),
                              logging.StreamHandler()])

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> 'Car':
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> 'Motorcycle':
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> 'Car':
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> 'Motorcycle':
        return Motorcycle(make, model, "EU Spec")

class Car(Vehicle):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region}): Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region}): Мотор заведено")

# Використання
vehicle1 = USVehicleFactory().create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = EUVehicleFactory().create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
