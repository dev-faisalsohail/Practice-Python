def mysub(a,b):
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


# function calling with keyword argument
display(age = 35, name = "Sara")
display(name = "Omar")
display()
display(age = 40)
# function calling with positional argument
display("Lina")
display(28, "Yousef") 


# passing variable number of arguments to a function
def my_function(*args):
  for i in args:
    print(i, end=" ")

my_function()
my_function("Faisal","Khursheed")
print("\n")

my_function(1,2,3,4,5)

print("\n")

my_function("Hello", 1, 2.5, True)



def make_pizza(size, *toppings):
    print("\nMaking a", size, "inch pizza with the following toppings:")
    for topping in toppings:
        print("Topping:", topping)
    return
make_pizza(12, "pepperoni","extra cheese","mushrooms")
make_pizza(16, "mushrooms", "green peppers", "extra cheese")


# Arbitray Keyword Arguments

def myfunction1(**kwargs):
    for arg in kwargs.items():
        print(arg)  
    return
  
myfunction1(name="Faisal", age=20, city="Karachi")
print("\n") 


def myfunc(**kwargs):
    for key, value in kwargs.items():
        print(key + " : " + str(value))
    return
myfunc(name="Ali", age=25, city="Lahore")
print("\n")

# def greet(**kwargs):
#     if 'name' in kwargs:
#         print("Hello " + kwargs['name'])
#     else:
#         print(input("Enter your name: "))
#     return
# greet(input("Enter your name: "))
# greet()

# make a function for grocery items , item first name should be captial letter and price should be float value 2 decimal points at the end in the total bill 
def grocery_item(item, **kwargs):
    item = item.capitalize()
    print("Grocery Item:", item)
    total = 0
    for key, value in kwargs.items():
        print(key + " : " + str(value))
        total += float(value)
    print("Total Bill: Rs.", format(total, '.2f'))
    return