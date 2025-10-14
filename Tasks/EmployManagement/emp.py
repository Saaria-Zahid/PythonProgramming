# Question : Define an employ class with attributes role, department, and salary. this class also method ShowDetails()
# - Create a subclass Engineer that inherits from Employ and adds attributes name and age.
#   Implement a method engineerInfo() in the Engineer class that displays all the details of the engineer, including their role, department, salary, name, and age.


class Employ:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.__salary = salary  # Private attribute
        
    def show_details(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: Rs.{self.__salary}")
        
        
# emp1 = Employ("Sale Manager", "Sales", 60000)
# emp1.show_details()        



class Engineer(Employ):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "80,000")
    
    def engineer_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        self.show_details()        
    
eng1 = Engineer("Ahmed", 30,)
eng1.engineer_info() 