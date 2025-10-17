if (2 != 2):
  print('True statement')
else:
  print('False')
  
  
  x = 2 
  
  if (x ==1):
    print('This will execute, only if the condtion is true')
  print('Tis will always execute')


x = input("enter a number:")
# by defualt the type returned by input( ) is string, so don't forget to type cast it
x = int(x)
if(x%2 == 0):
  print("Even")
else:
  print("Odd")
print("Bye")


y = input("enter a number: ")
y = int(y)

age = 18
if age >=18:
  print("you're eligible")
else:
  print("you're not eligible")
  
  '''
  a = 5
  b = 10
  
  if(a>b):
    print('a is greater than b.')
    print("i'm in if block'")
    
  else:
    print('a is smaller than b.')
  print("i'm neitherin the if-block nor in the else block")
  
  
  '''
  
  # python ternary operator
  
  age = 14
  
  rv = 'adult' if age>= 18 else 'child'
  print (rv)
  
  
number = 31

rn = 'even' if number%2==0 else 'odd'

print(rn)
'''
if len(password) => 8:
  print('password length is valid')
else:
  print('password is not strong')
'''

age = float(input("Please enter your age:"))
if(age >= 18):
    rv = input("Do you have National ID card? Y/N:")
    if((rv == 'Y') or (rv == 'y')):
     print("WElcome,you can vote")
    else:
     print("Since you donot have CNIC, so you cannot vote")  
else:
  print("You are too young to vote")
  
  
  cnic = input("Enter CNIC: ")


cnic = cnic.replace("#", "")
cnic = cnic.replace("@", "")
cnic = cnic.replace("&", "")


if cnic.isdigit() and len(cnic) == 13:
    clean_cnic = cnic[:5] + "-" + cnic[5:12] + "-" + cnic[12:]
    print("Valid CNIC:", clean_cnic)
else:
    print("Invalid CNIC")



# Example 1:
y = input("Enter your subject marks: ")
# by default the type is string, so we need to convert the type first
y = int(y)
if  (y >= 85):
    print("Letter Grade A")
elif((y >= 80) and (y<85)):
    print("Letter Grade A-")
elif((y >= 77) and (y<80)):
    print("Letter Grade B+")
elif((y >= 73) and (y<77)):
    print("Letter Grade B")
else:
    print("Bad Grade")
    


# Example 3

x = 6
if x < 0:
    pass
  print("I will place ocde when the condtion is true, later :")