n = int(input("Enter number: "))
sum = 0
i = 1
while (i <= n):
  #print("Sum: ",sum)
  sum = sum + i
  #print
  i = i + 1
  # print("Counter: ", i)
  print("The sum is", sum)
  
  

# make a table of 2
number = int(input("Enter number: "))
i = 1  

print(f"Multiplication table for {number}:")

while i <= 10:
    
    print(f"{number} x {i} = {number * i}")
    
    i = i + 1
  
  
  
list1 = ['learning','is','fun','with','python','&','R','programming','language','Data','Analysis']
str = 0
while(str < len(list1)):
  print(list1[str])
  str +=1
print(list1)

# use pop()

a = [1,2,3,4,5]

while (a):
  print("Outer:", a.pop())
  b = ['Kiran', 'Khursheed']
  while(b):
    print("\t Inner: ",b.pop())
    
print("After both the loops end")
print("a= ",a)
print("b ",b)

n = 10


# continue
while n > 0:
  n = n - 1
  if(n % 2 == 0):
    continue
  print(n)


# The while loop with else statement:

# Example: The 'else block will execute only when the loop 


n = 5 
while n > 0:
  n = n - 1
  print(n)
else:
  print("Loop is finished")
print("outside loop")


