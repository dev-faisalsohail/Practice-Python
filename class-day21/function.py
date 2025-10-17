# # How to create user Defined Functions in Python
# def greet(name):
#     """This function greets to the person passed in as a parameter"""
#     print("Hello, " + name + ". Good morning!")
    




# def myLength(s):
#     count = 0
#     for i in s:
#         count += 1
#     return count
  
# print(myLength("Faisal"))


# # get input from user and add 2 numbers
# def add_two_numbers():  
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     sum = num1 + num2
#     return sum  
  
#   # greeting function make a docstring
# def func1():
#     """This function does nothing"""
#     print("Hello World")
# func1()
# greet("Faisal") 
# print(greet.__doc__)  # prints the docstring of greet function
# print(greet("Faisal"))  # prints None because there is no return statement in

# # make a docstring of sum function
# def sum(a, b):
#     """This function returns the sum of two numbers"""
#     return a + b
# print(sum(10, 20))  # prints the sum of 10 and 20
# print(sum.__doc__)  # prints the docstring of sum function


# # defining a function
# def mysum2():
#     total = 5 + 7
#     return total
  
  
# rv = mysum2()  # function call
# print("5 + 7 =",rv) # prints the return value of mysum2 function


# # Returning multiple values from a function
# def func():
#     str1 = "Hello"
#     str2 = "bye"
#     return str1, str2  # returning multiple values as a tuple
  
# rv1, rv2 = func()  # unpacking the returned tuple
# print(rv1)  # prints "Hello"
# print(rv2)  # prints "bye"


# # A function that receives a list and returns a list data type counting the number of even
# def count_even_numbers(lst):
#     count = 0
#     for num in lst:
#         if num % 2 == 0:
#             count += 1
#     return count
  
# even_count = count_even_numbers([1, 2, 3, 4, 5, 6])
# print("Number of even numbers:", even_count)  # prints the count of even numbers in the list greet



# def sort(mylist2):
#    for c in range(len(mylist2)):
#        for d in range(c + 1, len(mylist2)):
#                if mylist2[c] > mylist2[d]:
#                    mylist2[c], mylist2[d] = mylist2[d], mylist2[c]
#        return mylist2
# numbers = [-5, 4, 3, 76, 34, 23, 12]
# sorted_numbers = sort(numbers)
# print("Original list is:", numbers) 
# print("Sorted list is:", sorted_numbers)  


def my_sort(mylist2):
    # simple in-place selection-style sort
    for c in range(len(mylist2)):
        for d in range(c + 1, len(mylist2)):
            if mylist2[c] > mylist2[d]:
                mylist2[c], mylist2[d] = mylist2[d], mylist2[c]
    return mylist2




numbers = [-5, 4, 3, 76, 34, 23, 12]
sorted_numbers = my_sort(numbers.copy())  # use .copy() to keep original unchanged
print("Original list is:", numbers)
print("Sorted list is:", sorted_numbers)


def sel_sort2(mylist):
    newlist = mylist[:]
    for i in range(len(newlist)):
            min_index = i
            for j in range(i + 1, len(newlist)):
                if newlist[j] < newlist[min_index]:
                    min_index = j
            newlist[i], newlist[min_index] = newlist[min_index], newlist[i]
        return newlist


numbers = [-5, 4, 3, 76, 34, 23, 12]
sorted_numbers = my_sort(numbers.copy())  # use .copy() to keep original unchanged
print("Original list is:", numbers)
print("Sorted list is:", sorted_numbers)


# make a function that takes a message as user input and than give response a message
def respond_to_message():
    message = input("You: ")
    print("Nadia: G")
    respond_to_message()
# respond_to_message() greet function



def mysub(a,b)
    return a - b
print(mysub(10,5))

def mydiv(a,b):
    return a / b    
print(mydiv(10,2))

def display(name = "Faisal", age = 20):
    print("Hello", name, "Your age is", age)
    return

display("Ali", 25)
display("Ahmed", 30)