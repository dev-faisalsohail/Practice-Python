# Python Input Guide for Beginners
# Learn how to get user input in Python with easy examples

# =============================================================================
# 1. BASIC INPUT - Getting text from user
# =============================================================================

print("=== Basic Input Examples ===")

# Simple input - always returns a string
name = input("What's your name? ")
print("Hello, " + name + "!")

# Input with no prompt message
user_input = input()
print("You entered:", user_input)

# =============================================================================
# 2. GETTING NUMBERS - Converting string input to numbers
# =============================================================================

print("\n=== Number Input Examples ===")

# Getting an integer (whole number)
age = int(input("How old are you? "))
print("Next year you'll be", age + 1)

# Getting a decimal number (float)
height = float(input("What's your height in meters? "))
print("Your height in centimeters is", height * 100)

# =============================================================================
# 3. MULTIPLE INPUTS - Getting several values
# =============================================================================

print("\n=== Multiple Input Examples ===")

# Getting multiple values on separate lines
print("Enter your favorite colors:")
color1 = input("First color: ")
color2 = input("Second color: ")
color3 = input("Third color: ")
print("Your colors are:", color1, color2, color3)

# Getting multiple values on one line (separated by spaces)
print("Enter three numbers separated by spaces:")
numbers = input().split()  # This creates a list of strings
print("Numbers as strings:", numbers)

# Converting the list of strings to integers
numbers = [int(x) for x in numbers]
print("Numbers as integers:", numbers)
print("Sum of numbers:", sum(numbers))

# =============================================================================
# 4. HANDLING INPUT ERRORS - Making your code safer
# =============================================================================

print("\n=== Safe Input Examples ===")

# Safe integer input with error handling
while True:
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
        break  # Exit the loop if input is valid
    except ValueError:
        print("That's not a valid number! Please try again.")

# Safe yes/no input
while True:
    answer = input("Do you like Python? (yes/no): ").lower()
    if answer in ['yes', 'y']:
        print("Great! Python is awesome!")
        break
    elif answer in ['no', 'n']:
        print("That's okay, maybe you'll like it later!")
        break
    else:
        print("Please answer 'yes' or 'no'")

# =============================================================================
# 5. PRACTICAL EXAMPLES - Real-world applications
# =============================================================================

print("\n=== Practical Examples ===")

# Example 1: Simple Calculator
print("Simple Calculator")
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Error: Invalid operation!"

print("Result:", result)

# Example 2: Personal Information Collector
print("\nPersonal Information")
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
city = input("City: ")

print(f"\nHello {first_name} {last_name}!")
print(f"You are {age} years old and live in {city}.")

# Example 3: Shopping List
print("\nShopping List Creator")
items = []
while True:
    item = input("Enter an item (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    items.append(item)

print("\nYour shopping list:")
for i, item in enumerate(items, 1):
    print(f"{i}. {item}")

# =============================================================================
# 6. USEFUL TIPS AND TRICKS
# =============================================================================

print("\n=== Tips and Tricks ===")

# Strip whitespace from input (removes extra spaces)
clean_input = input("Enter something with spaces: ").strip()
print("Clean input:", clean_input)

# Convert input to uppercase/lowercase
text = input("Enter some text: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Check if input is empty
user_text = input("Enter something (or press Enter for default): ")
if not user_text:  # Empty string is False in Python
    user_text = "Default value"
print("Final text:", user_text)

# Getting password input (note: this will still show the text in most environments)
import getpass
# Uncomment the next line if you want to hide password input
# password = getpass.getpass("Enter password: ")

# =============================================================================
# 7. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n=== Common Mistakes ===")

# MISTAKE 1: Forgetting to convert string to number
# Wrong way:
# age = input("Age: ")  # This is a string!
# next_year = age + 1   # This will cause an error!

# Right way:
age = int(input("Age: "))
next_year = age + 1
print("Next year:", next_year)

# MISTAKE 2: Not handling empty input
name = input("Name (optional): ")
if name:  # Check if name is not empty
    print("Hello,", name)
else:
    print("Hello, anonymous user!")

print("\n=== End of Examples ===")
print("Practice these examples and modify them to learn more!")