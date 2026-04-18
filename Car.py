class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_car_detail(self):
        print(f'Car brand is {self.brand} and the model of the car is {self.model}')

    def start_engine(self):
        print(f"{self.brand}'s model {self.model} Car is starting")

toyota_car = car("Toyota", "Corolla")
honda_car = car("Honda", "Civic")

toyota_car.display_car_detail()
honda_car.display_car_detail()

toyota_car.start_engine()