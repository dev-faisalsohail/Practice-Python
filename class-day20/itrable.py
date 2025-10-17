mylist = [1, 2, 3, 4, 5]
myit = iter(mylist)
print(next(myit))  # Output: 1
print(next(myit))  # Output: 2 
print(next(myit))  # Output: 3
print(next(myit))  # Output: 4
print(next(myit))  # Output: 5
# print(next(myit))  # This would raise StopIteration error


# For Loops
mylist = [1, 2, 3, 4, 5]
for i in mylist:
    print(i)
    
    
    
# loop though a string
mystr = "Hello"
for i in mystr:
    print(i)
    
    
# Iterate a string suing for loop and count the count of specific character
mystr = "Hello, welcome to my world."
count = 0
for character in mystr:
    if character == "e":
        count += 1
print("Count of 'e':", count)


# Iterating through a dictionary keys and values
mydict = {"name": "John", "age": 30, "city": "New York", "height": "180cm","Occupation": "Engineer"}
for key in mydict:
    print(key, ":", mydict[key])
for key, value in mydict.items():
    print(key, ":", value)
    
    
# print all elements of list ignoring string string "Faisal"
list1 = ["Faisal", 1, 2, 3, 4, 5, "Hello", "World"]
for item in list1:
    if item == "Faisal":
         pass  # do nothing
    else: 
      print(item)
      
# range function
for i in range(5):  # 0 to 4
    print(i)
for i in range(1, 6):  # 1 to 5
    print(i)
for i in range(1, 10, 2):  # 1 to 9 with step of 2
    print(i)
for i in range(10, 0, -1):  # 10 to 1
    print(i)  
for i in range(5, 0, -1):  # 5 to 1
    print(i)
for i in range(0, -5, -1):  # 0 to -4
    print(i)
for i in range(-5, 0):  # -5 to -1
    print(i)  
for i in range(-1, -6, -1):  # -1 to -5
    print(i)
for i in range(-10, -1, 2):  # -10 to -2 with step of 2
    print(i)  
for i in range(-10, -1, 3):  # -10 to -2 with step of 3
    print(i)  
for i in range(-10, -1, 4):  # -10 to -2 with step of 4
    print(i)
for i in range(-10, -1, 5):  # -10 to -2 with step of 5
    print(i)  
for i in range(-10, -1, 6):  # -10 to -2 with step of 6
    print(i)
    
    
# Used to iterate over lists, when you need to track the index of the current item in range
mylist = ['apple', 'banana', 'cherry']
for index in range(len(mylist)):
    print('The value at position {} is {}'.format(index, mylist[index]))   
# Output:
# 0 apple 

# enumerate function
mylist = ['apple', 'banana', 'cherry']
for index, value in enumerate(mylist):
    print('The value at position {} is {}'.format(index, value))
    
    
# Break the loop when it reaches the element "cherry"
mylist = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for fruit in mylist:
    if fruit == 'cherry':
        break
    print(fruit)
    
    
# range is 12 not print even just print odd numbers
for i in range(12): 
    if i % 2 == 0: # Check if the number is even
        continue # Skip the rest of the loop for even numbers
    print(i)  
    
    
# A for loop with else and break statement if name is found in the dictionary else print not found
names = {
  'Faisal': 27,
  'Atif': 22,
  'Rizwan': 22,
  'Fasi': 28,
  'Auun': 20
}
name_find = input("Enter name to find: ")
for myName in names:
    if myName == name_find:
        print(f"{name_find} name found with age {names[myName]}.")
        break
else:
    print(f"{name_find} name not found.")
    
    
# Nested for loop to print a pattern

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['Apple', 'Banana', 'guava']
for day in days:
    for fruit in fruits:
        print(f"{day}: {fruit}")  


# suppose we have an oldish list of names and we want to create a new list with the names in uppercase
old_names = ['alice', 'bob', 'charlie']
new_names = []
for name in old_names:
    new_names.append(name.upper())   
print(new_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']


oldlist = ['alice', 'bob', 'charlie']
newlist = [i*i for i in oldlist]
print(newlist)  # Output: ['alicealice', 'bobbob', 'charliecharlie']

# Given a list, create a new list that should contain the even numbers in the given list using list comprehension
# new list = [expression for item in iterable if condition == True]
oldlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = [i for i in oldlist if i % 2 == 0]
print(newlist)


oldlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlist = []

for i in oldlist:
    newlist.append(i)
print(newlist)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for fruit in fruits:
    if 'a' in fruit:
        newlist.append(fruit)
print(newlist)  # Output: ['apple', 'banana', 'mango']



fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [fruit for fruit in fruits if(fruit != 'kiwi')]

print(newlist)  # Output: ['apple', 'banana', 'cherry', 'mango']
print(type(newlist))  # Output: <class 'list'>