# PolyMorPhism = "many forms"
# Example With Operators Overloading

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def showNumber(self):
        print(f"{self.real}i + {self.imaginary}j")
        
        
        #Dunder Methods
        #Addition
    def __add__(self, num2):    
        self.real = self.real + num2.real
        self.imaginary = self.imaginary + num2.imaginary
        return Complex(self.real, self.imaginary)
    
    #Subtraction
    def __sub__(self, num2):    
        self.real = self.real - num2.real
        self.imaginary = self.imaginary - num2.imaginary
        return Complex(self.real, self.imaginary)
    
    #Multiplication
    def __mul__(self, num2):    
        self.real = self.real * num2.real
        self.imaginary = self.imaginary * num2.imaginary
        return Complex(self.real, self.imaginary)
    
    #Division
    def __truediv__(self, num2):    
      self.real = self.real / num2.real
      self.imaginary = self.imaginary / num2.imaginary
      return Complex(self.real, self.imaginary)
        
num1 = Complex(6, 8)
num2 = Complex(5, 6)

        
num1.showNumber()        
num2.showNumber()      

num3 = num1 + num2
print(f"Addition")
num3.showNumber()

num3 = num1 - num2
print(f"Subtraction")
num3.showNumber()


num3 = num1 * num2
print(f"Multiplication")
num3.showNumber()


num3 = num1 / num2
print(f"Division")
num3.showNumber()

# num3 = num1 * num2
# num3.showNumber()

