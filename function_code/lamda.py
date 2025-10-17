from functools import reduce


def mysyn2(a, b):
    return a + b
  
rv = mysyn2(5, 7)
print(rv)


mysum3 = lambda a, b: a + b
rv2 = mysum3(5, 7)
print(rv2)

mysum3 = lambda a, b, c: a + b + c

rv3 = mysum3(5, 7, 9)
print(rv3)


even = lambda x: x % 2 == 0
print(even(4))
print(even(5))
odd = lambda x: x % 2 != 0
print(odd(4))

func = lambda s:s[0]
rv = func("hello")
print(rv)

func2 = lambda s:s[-1]
rv2 = func2("hello")
print(rv2)


def mymul(a, b):
    return a * b
def mysub(a, b):
    return a - b
def myadd(a, b):
    return a + b

rv1 = myadd(5, 7)
print(rv1)
rv3 = mysub(5, 7)
print(rv3)
rv3 = mymul(5, 7)
print(rv3)


myddd = lambda a, b: a + b
rv4 = myddd(5, 7)
print(rv4)
mysub = lambda a, b: a - b
rv5 = mysub(5, 7)
print(rv5)
mymul = lambda a, b: a * b
rv6 = mymul(5, 7)
print(rv6)  



def mycalc(op, a, b):
    return op(a, b)

myadd = lambda a, b: a + b
mysub = lambda a, b: a - b
mymul = lambda a, b: a * b

rv1 = mycalc(myadd, 5, 7)
rv2 = mycalc(mysub, 5, 7)
rv3 = mycalc(mymul, 5, 7)
print(rv1)
print(rv2)
print(rv3)


# make a lamda function in greeting 
greet = lambda name: f"Hello, {name}!"
print(greet("Faisal"))   
greet = lambda name: f"Goodbye, {name}!"
print(greet("Sohail"))


# lamda function for pass and fail if marks is greater than 50
result = lambda marks: "Pass" if marks >= 50 else "Fail"
print(result(60))
print(result(40))   

# lamda function to find leap year
leap_year = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(leap_year(2020))


mylist = [5,7,2,6,9]


map_object = map(lambda x: x ** 2, mylist)

mylist_squared = list(map_object)

print("Original list: ",mylist)
print("list with items squared:",mylist_squared)

# suppose we want to add two lists in lamda

mylist1 = [4,8,3,2]
mylist2 = [3,1,2,6]

result = map(lambda a,b: a + b,mylist1,mylist2)
result = list(result)

print("Sum of the two list: ", result)

# make a list of happy sad and angry in map function and apply emoji of each list entity

# A list of emotions
emotions = ['happy', 'sad', 'angry', 'surprised']

# A dictionary that maps emotion strings to emoji characters
emoji_map = {
    'happy': '😊',
    'sad': '😢',
    'angry': '😠',
    'surprised': '😮'
}

# Use the map() function with a lambda to transform the list.
# The lambda function looks up each emotion in the emoji_map dictionary.
# .get() is used to safely retrieve the value, providing a default '😐' if the key is not found.
emoji_list = list(map(lambda emotion: emoji_map.get(emotion, '😐'), emotions))

# Print the resulting list of emojis
print("Original list:", emotions)
print("List with emojis:", emoji_list)


# reverse each word in a list

# ...existing code...
# The list of emojis from the previous example
emoji_list = ['😊', '😢', '😠', '😮']

# Use map() with a lambda to reverse each emoji string in the list
reversed_emojis = list(map(lambda emoji: emoji[::-1], emoji_list))

# Print the original and reversed emoji lists
print("Original emoji list:", emoji_list)
print("List with reversed emojis:", reversed_emojis)
# length of each element of list



new_list = [1,5,4,6,8,11,3,12]

result = map(lambda x: x % 2 == 0, new_list)

result = (list(result))

print("Even numbers in the list are: ",result)


result1 = filter(lambda x: x % 2 == 0, new_list)

result1 = (list(result))

print("Even numbers in the list are: ",result1)

characters = ['i', 'z', 'b', 'a', 'd', 'f', 't', 'e','w', 'x']

vowels = ['a', 'e', 'i', 'o', 'u']
    
result = filter(lambda x: x in vowels, characters)

result = list(result)    
print("Vowels in the list are: ", result)


def myadd(a,b):
    return a+b

numbers = [47, 11, 42, 13]

rv = reduce(myadd, numbers)
print(rv)


mylist = [0,0,1,0,0]

rv1 = reduce(lambda a,b: bool(a and b),mylist)

print(rv1)


# map apply on list and than covert this list into uppercase


