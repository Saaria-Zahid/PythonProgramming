
class Order:
    def __init__(self, product, price):
        self.product = product
        self.price = price
        
    def __gt__(self, ord2):
        return self.price > ord2.price
    

ord1 = Order("Tea", 100)
ord2 = Order("Coffee", 200)
print(ord1 > ord2)  # False    