       
       # Example 6: Print Fibonacci series
n = int(input("Enter count of fibonacci numbers you want to print: "))
i = 1
if n<1:
    fib = []       # In case user enter <0, the list is empty
elif n==1:
    fib = [0]      # If user enters 1, the list has the first fibonacci number
elif n==2:
    fib = [0, 1]   # If user enters 2, the list has the first two fibonacci numbers
elif n > 2:
    fib = [0, 1]   # if n>2, then we need to enter in while loop to compute the rest of the fibonacci numbers
    while (i < n-1):
        fib.append(fib[i] + fib[i-1])
        i += 1
print("Required Fibonacci series: ", fib)