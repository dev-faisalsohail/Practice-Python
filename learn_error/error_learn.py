import sys
# exceptions : program is break (logical type error means syntax is okay but error is producing)

# how to handle exceptions

# try   (if condition is false than code run except.) (if condition is true than code don't run in except)
#   run this 
  
# except
#   execute this code when there is an Exception


# Ttype of Exceptions 

try: 
  # a = z
  # # z = 45/0
  # # print(z)
  
  a= "Faisal"
  print(a)

except Exception as e:
  print("Exception occured: ", e)
  

else:
  print("run this program know")
  

try: 
  z = 45/0
  print(z)
  a = 34 + 'hello'
  lsit1 = [1,5,9]
  pirnt(list[3])
  import kakamanna
  
except ZeroDivisionError:
  print("ZeroDivisonError accured and Handled")
  
except NameError:
  print("NameError Occured and Handled")
except TypeError:
  print("TypeError acccured and Handled")
except IndexError:
  print("IndexError occured and Handled")
except ModuleNotFoundError:
  print("ModuleNotFoundError accoured and handled")


else:
  print("This will execute if try clause doest not raise an exception")
finally:
  print("This will always be executed")
  
  
age = "hello"

# x = 10  # Define x with an integer value
# if not type(x) is int:
#   raise TypeError("Only intergers are allowed")
# print("Program continues as x is number")

# age = -1
# assert age > 0, 'age should be positive'
# print("program continues as age is positive")


assert ('win32' in sys.platform), "This code runs only on windows"
# assert ('darwin' in sys.platform), "This code runs only on Mac"
print("Program continues...")

