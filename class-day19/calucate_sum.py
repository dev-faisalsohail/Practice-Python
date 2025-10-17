# # Example 3: Input number from user and compute the sum 1+2+3+4+....+n
# n = int(input("Enter number: "))
# sum = 0
# i = 1
# while (i <= n):
#     print("Sum: ",sum)
#     sum = sum + i
#     print("Updated sum",sum)
#     i = i+1   # update counter
#     print("Counter: ",i)
# print("The sum is", sum)


n1 = int(input("Enter number: "))
sum_of_even = 0
i = 1

while (i <= n1):
    if i % 2 == 0:        # check if number is even
        print("Even number:", i)
        sum_of_even = sum_of_even + i     # add only even numbers
        print("Updated sum:", sum_of_even)
    i = i + 1             # update counter
    print("Counter:", i)

print("The sum of even numbers is", sum_of_even)


# sum of foctorial 

n3 = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n3:
    fact = fact * i
    print("i =", i, " → factorial so far =", fact)
    i = i + 1

print("The factorial of", n3, "is", fact)
