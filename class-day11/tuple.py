# tuple is immutable list can create in [], but tuple cerate by (), tuple are fast than list
# tuple are ordered , tuple are hetrogenious, it start from 0 in the ordered
''' 
Python introduced named tuples primarily to enhance code readability and maintainability by providing a more semantic way to access elements within a tuple-like data structure.
'''
# Learn Tuple 

# nested tuple a tuple an also have another tuple or list as an item

t1 = (1,"Hello",[8,'OK', 6],(1,2,'BYE'),5.5)
print("t1:",t1)
print("Type of t1 is:",type(t1))
print(t1[2][1])


# A list within a tuple is still mutable 

t2 = (1,"Hello",[8,'OK', 6],(1,2,'BYE'),5.5)
print("t2:",t2)
print("Type of t2 is:",type(t2))
t2[2][1] = 'Not OK'
# t2[1] = "Faisal"
print(t2)

# Packing and Un Packing 

# You can unpack tuple elements

t3 = ('learning', 'is', 'fun','with','kiran')
a,b,c,d,e = t3 # the number of variables on the left must match the length
print(a,c,e)
print(type(a))


# you can pack individual elements to a tuple
# Type casting in tuple
my_tuple = ('learning', 'is', 'fun','with','kiran')
my_list = list(my_tuple)
print(my_list)
print(type(my_list))


# You can access elements of tuple using indexing which starts from zero

t5 = ("kiran",20,5.5,(10,'Khursheed'))

print(t5[2])  # accessing element of tuple at index2
print(t5[3])  # accessing element of tuple at index3, which is again 


# accessing Nested tuple element
print(t5[0][2])
print(t5[3][1][7])
print(t5[2])


# index (value) method is used when you know the tuple element and wants to
# index (value) method is used when you know the tuple element and want to 
mytuple = (27,4.5,'kiran',64,"Khursheed",19,"aqsa","Kiran")
print('\mytuple:',mytuple)


# Slicing 

t1 = ('a','b','c','d','e','f','g','h','i')
print(t1)
print(t1[2:5])
print(t1[4:-1])
print(t1[::-1])
#print(t1[2,11:-1])


# You can't use slice slice operator on the left side of assignment as tupel si 

#t1 = (1,2,3,4,5,6,7)
#t1[2:4] = ['a','b','c']

# Concatenating Tuples 

# Add some elements to the end of an existing tuple using concatenation operator 

a = (1,2,3)
b = a + (4,5)

# Add some elements to the beginning of an existing tuple using concat
a = (1,2,3)
b = a + (4,5)

# Add some elemnts to the beginning 

c = (0,) + b
a,b,c
print (a,b,c)

# use + operator to concatenate two tupels 


food_item1 = ('fruits','bread','veggies')
food_item2 = ('meat','spices','burger')
food = food_item1 + food_item2
print(food)


n = ('khursheed',)

food_item3 = ('fruits','bread','veggies',('kiran',('khursheed', )))

print(food_item3[3][1][0].index('r'))


t1 = (3,8,1,6,0,8,4)

print("original tuple =", t1)

list1 = sorted(t1)

list2 = sorted(t1,reverse=True)

print("Ascending Sort: ", list1)
print("Descending Sort: ", list2)


t2 = ('ccc','aaaa','d','bb')

sorted(t2, key=len, reverse=True)

print(t2)


# suppose given a tuple with elements ('abcz','xyza','bas','kiran') and we want to sort it by last character of strings within the tuple so that the output is like : ('xyza','kiran','bas','abcz')

#t4 = ('abcz','xyza','bas','kiran')

#sorted(iterable, key=)