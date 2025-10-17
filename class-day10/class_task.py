# Question 1
# Swapping values without extra variable
# swap a = 25, b = 27 using only arithmetic operators 

a = 25
b = 27

# Swapping 
a = a + b  
b = a - b  
a = a - b  

# Display the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)


# Question 2
# Discounted Price Calculation 
# Product price = 1200, discount = 15%  GST = 8% (on discounted price)


# Product price and discount/GST rates
product_price = 1200
discount_rate = 15  # in percentage
gst_rate = 8  # in percentage

discounted_price = product_price - (product_price * discount_rate / 100)

gst_amount = discounted_price * gst_rate / 100

#  Calculate the final price after adding GST
final_price = discounted_price + gst_amount

# Display the results
print("Original Price:", product_price)
print("Discounted Price:", discounted_price)
print("GST Amount:", gst_amount)
print("Final Price after GST:", final_price)


# Find the Middle Number among using arithmetic operators a =12, b=25, c=18

a = 12
b = 25
c = 18

max_ab = a * (a > b) + b * (b >= a)
max_abc = max_ab * (max_ab > c) + c * (c >= max_ab)

min_ab = a * (a < b) + b * (b <= a)
min_abc = min_ab * (min_ab < c) + c * (c <= min_ab)

middle = (a + b + c) - max_abc - min_abc

print("The middle number is:", middle)


# Digit  Extraction Game 
# if num = 4782(integer) extract digits 
#print(thousands,hundred,tens,ones) # 4782

# Number to extract digits from
num = 4782

thousands = num // 1000
hundarad = (num // 100) % 10
tens =(num//10) % 10
ones = num % 10

print("thousand", thousands)
print("hundards", hundarad)
print("tens", tens)
print("ones", ones)


# Question No. 5

# Truth Table Challenge 
# Check conditions using only operators
# Divisible by Both 2 and 5

n = 20  
result = (n % 2 == 0) and (n % 5 == 0)
print("20 is divisible by both 2 and 5", result)

# Question 6

# Both Variables Between 10 and 50
# check if x and y are both in the range 10-50(exclusive)

# Variables to check
x = 15
y = 45


# Check if both x and y are in the range 10-50 (exclusive)
in_range = (10 < x < 50) and (10 < y < 50)
print(f"Are both x({x}) and y({y}) between 10 and 50? {in_range}")


