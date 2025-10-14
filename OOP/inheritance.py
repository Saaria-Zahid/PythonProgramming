class Car:
    def __init__(self, color, model, year, horsepower ):
        self.color = color
        self.model = model
        self.year = year
        self.horsepower = horsepower
        

    @staticmethod
    def start():
        print("Car Started..")
    
    @staticmethod
    def stop():
        print("Car Stopped..")
        
    def info(self):
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Horsepower: {self.horsepower} HP")
        
class Toyota(Car):
    brand = "Toyota"
    
    def __init__(self, name, vehivle_type, color, model, year, horsepower):
        super().__init__(color, model, year, horsepower)
        self.name = name
        self.vehicle_type = vehivle_type
        
    def car_info(self):
        self.info()
        print(f"Brand: {self.brand}")
        print(f"Name: {self.name}")
        print(f"Vehicle Type: {self.vehicle_type}")    


car1 = Toyota("Corolla", "Sedan", color="White", model="X", year=2025, horsepower=200)            
car1.car_info()
car1.start()
car1.stop()
car1.info()