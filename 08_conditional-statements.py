
age = int(input("Enter your age: "))
day = input("Enter the day: ").strip().lower()

if age < 5:
    price = 0
elif 5 <= age <= 17:
    price = 8
elif 18 <= age <= 59:
    price = 12
else:
    price = 6

if day == "wednesday":
    discount = 0.2  # 20%
    final_price = price - (price * discount)
else:
    final_price = price

print(f"\nBase price: ${price}")
if day == "wednesday" and price != 0:
    print("Discount applied: 20%")
print(f"Final ticket price: ${final_price}")
