# Encapsulation = Wrapping data and methods into a single unit
# In Python, we denote private attributes and methods with a leading underscore (_)


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
