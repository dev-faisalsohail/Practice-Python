# Assignment Advanced Function Solved by Faisal Sohail

print("\n--------------------------------------\n")
print("***** Advanced Function *****")
print("\n--------------------------------------\n")

from functools import reduce

#  Q1: Sales Above Target (Filter)

print("Solution No.1: Sales Above Target (Filter)\n")

monthly_sales = [8500, 12300, 9800, 15700, 11200, 8900, 13450]
sales_target = list(filter(lambda sale: sale > 10000,monthly_sales))
print("sales above 10000:", sales_target)

print("\n--------------------------------------\n")

# Q2: Apply Discount to Prices (Map)

print("Solution No.2: Apply Discount to Prices (Map)\n")

product_prices = [1200, 800, 4000, 560, 1500]
discounted_prices = list(map(lambda price:price * 0.9, product_prices))
print("discounted price:", discounted_prices)

print("\n--------------------------------------\n")

# Q3: Find Total Sales (Reduce)
print("Solution No.3:  Find Total Sales (Reduce)\n")
daily_sales = [2500, 3200, 1800, 4000, 1500]
total_sales = reduce(lambda x,y: x + y,daily_sales)
print("Total Sales:", total_sales)

print("\n--------------------------------------\n")

# --- Q4: Square Even Numbers (Filter + Map)

print("Solution No.4: Square Even Numbers (Filter + Map)\n")

numbers = [3, 6, 9, 12, 15, 18, 21]
even_numbers = list(filter(lambda even: even % 2 == 0, numbers))
print("Even Numbers:",even_numbers)
square_even = list(map(lambda square: square ** 2,even_numbers))
print("Square of Even:",square_even)
print("\n--------------------------------------\n")

# Q5: Count Words in a Sentence (Reduce)

print("Solution No.5: Count Words in a Sentence (Reduce)\n")

sentence = "Python is a powerful and easy to learn programming language"
words = sentence.split()
print("Words:",words)
word_count = reduce(lambda count, word: count + 1, words,0)
print("Total Words:", word_count)
print("\n--------------------------------------\n")

# Q No. 6: Employee Performance (Filter + Map + Reduce)

print(" Solution No.6: Employee Performance (Filter + Map + Reduce)\n")

ratings = [5.8, 7.5, 8.2, 9.1, 6.7, 7.9]
above_7 = list(filter(lambda r: r > 7, ratings))
print("Above 7:",above_7)
percentages = list(map(lambda p: p * 10, above_7))
print("Precentages:",percentages)
average = reduce(lambda a,b: a + b, percentages)/len(percentages)
print("Average Performance:",average)
print("\n--------------------------------------\n")

# Q No. 7: City Temperature Analysis (Filter + Map)

print("Solution No.7: City Temperature Analysis (Filter + Map)\n")

temps = [
    {'city': 'Karachi', 'temp_c': 35},
    {'city': 'Lahore', 'temp_c': 31},
    {'city': 'Islamabad', 'temp_c': 28},
    {'city': 'Quetta', 'temp_c': 22}
]

fahrenheit = list(map(lambda x: {'city': x['city'], 'temp_f': (x['temp_c'] * 9/5) + 32}, temps))
print("Fahrenheit Data:",fahrenheit)
above_90 = list(filter(lambda x: x['temp_f'] > 90, fahrenheit))
print("Cities above 90 Fahrenheit:",above_90)

print("\n--------------------------------------\n")

# Q. No. 8 (Website Analytics – Total Views)

print("Solution No. 8 (Website Analytics – Total Views)\n")

views = [
    {'page': 'Home', 'views': 450},
    {'page': 'About', 'views': 120},
    {'page': 'Shop', 'views': 880},
    {'page': 'Blog', 'views': 530}
]

page_views = list(map(lambda v: v['views'], views))
print("Page Views:",page_views)
total_views = reduce(lambda a,b : a + b, page_views)
print("Total views:", total_views)

print("\n--------------------------------------\n")

# Q No. 9: Country GDP Growth (Filter + Map)

print(" Solution No. 9: Country GDP Growth (Filter + Map)\n")

gdp_growth = {'Pakistan': 2.8, 'India': 6.5, 'Bangladesh': 5.9, 'Nepal': 3.1, 'Sri Lanka': 1.5}
filtered = dict(filter(lambda item: item[1] > 3, gdp_growth.items()))
print("Filtered Countries:", filtered)
summary = list(map(lambda c: f"{c} has {filtered[c]}% GDP growth.", filtered))
print("Summary:", summary)

print("\n--------------------------------------\n")

# Q No. 10 — Average Sales After Discount (All Three)

print("Solution No. 10 — Average Sales After Discount (All Three)\n")

prices = [150, 90, 300, 120, 60]
discounted = list(map(lambda p: p * 0.8, prices))
print("Discounted Prices:", discounted)
filtered = list(filter(lambda p: p > 100, discounted))
print("Filtered Prices (above $100):", filtered)
total = reduce(lambda a, b: a + b, filtered)
average = total / len(filtered)
print("Average Price:", average)

