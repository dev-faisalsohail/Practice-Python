
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

# Initialize the first two numbers of the series
n1, n2 = 0, 1
count = 0

# Check if the input is valid
if num_terms <= 0:
   print("Please enter a positive integer.")
# If there is only one term, return n1
elif num_terms == 1:
   print("Fibonacci sequence up to", num_terms, "term:")
   print(n1)
# Generate the Fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < num_terms:
       print(n1, end='  ')
       # Calculate the next term in the sequence
       nth = n1 + n2
       # Update values for the next iteration
       n1 = n2
       n2 = nth
       count += 1
       
       
