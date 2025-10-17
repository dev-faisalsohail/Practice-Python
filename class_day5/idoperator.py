# identity operator
a = 5
b = 5.0
print(a is b) # False, because 'is' checks for identity (same object in memory)
print(id(a))
print(id(b))



# membership operator
a = 10
b = 4
list = [1,2,3,4,5]

rv = a in list
print(rv) # False, because 10 is not in the list
rv = b in list
print(rv) # True, because 4 is in the list