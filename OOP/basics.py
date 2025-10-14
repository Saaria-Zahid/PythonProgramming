

class Student:
    
    def __init__(self, fullname, age, email):
        self.name = fullname
        self.age = age
        self.email = email
        print("Student Created Successfully")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}  ")
        print(f"Email = {self.email}")
        
    def greeting(self):
        print(f"Assalam u Alaikum {self.name}, How are you?")
    
    def goodbye(self):
        print(f"Goodbye {self.name}, See you later!")           
        
    def age_verification(self):
        if std.age >= 18:
            print("You are an adult, Eligilible for voting")
            std.greeting()
        else:
            print("You are not an adult, Not Eligilible for voting")
            self.goodbye()
            
            
    # Decorators        
    @staticmethod
    def hello():
        print("Hello World")           
    
              
    
    
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# email = input("Enter your email: ")


name = "Ali"
age = 20
email = "ali@gmail.com"
std = Student(name, age, email)
std.age_verification()
std.hello()












