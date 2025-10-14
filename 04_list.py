

# Make a list,
a=["Saaria", "Arsalan","Amir", "Zahid", "Babar"]

print(a)
# Output - ['Saaria', 'Arsalan', 'Amir', 'Zahid', 'Babar']

a.sort()
print(a)
# Output - ['Amir', 'Arsalan', 'Babar', 'Saaria', 'Zahid']

a.reverse()
print(a)
# Output - ['Zahid', 'Saaria', 'Babar', 'Arsalan', 'Amir']

a.append("Sudaes")
print(a)
# Output - ['Zahid', 'Saaria', 'Babar', 'Arsalan', 'Amir', 'Sudaes']

a.insert(2, "Huzaif")
print(a)
# Output - ['Zahid', 'Saaria', 'Huzaif', 'Babar', 'Arsalan', 'Amir', 'Sudaes']

a.pop(3)
print(a)
# Output - ['Zahid', 'Saaria', 'Huzaif', 'Arsalan', 'Amir', 'Sudaes'] removed value on index 3


a.remove("Amir")
print(a)
# Output - ['Zahid', 'Saaria', 'Huzaif', 'Arsalan', 'Sudaes']


print(a.count("Zahid"))
# Output - 1

a.clear()
print(a)
# Output - []




