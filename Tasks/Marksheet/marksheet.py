
# Total per subject is 100

eng=int(input("English Marks:"))
urd =int(input("Urdu Marks :"))
math =int(input("Maths Marks:"))
sci = int(input("Science Marks:"))

obt = eng+urd+math+sci
print(obt)
per= obt/400 *100
print(f"{per}%")