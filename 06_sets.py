


#Make Sets

a=set()
print(type(a))


a={2,3,3,8,34,53,65}
print(a)
# Output - {65, 2, 3, 34, 53, 8} its not showing value 3 again because set only get unique values

a.add(90) # single value add
print(a)
# Output - {65, 2, 3, 34, 53, 8, 90}

a.add((101,102,103))  # multiple values - nested set
print(a)
# Output - {65, 2, 3, 34, 53, 8, 90, (101, 102, 103)}

a.pop()
print(a)
# Output - {2, 3, 34, 53, 8, 90, (101, 102, 103)}

a.remove(2)
print(a)
# Output -  {3, 34, 53, 8, 90, (101, 102, 103)}



