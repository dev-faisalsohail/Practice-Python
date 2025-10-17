# List Comprehension 

# 1. Squares from 1 to 10
squares = [i**2 for i in range(1, 11)]
print("Squares",squares)

# 2. Even numbers from list
even_numbers = [x for x in [10, 21, 32, 43, 54, 65] if x % 2 == 0]
print("Even Number",even_numbers)

# 3. Convert to uppercase
fruits_upper = [fruit.upper() for fruit in ["apple", "banana", "cherry"]]
print("Upper Case",fruits_upper)

# 4. First letter of each word
first_letters = [word[0] for word in ["sun", "moon", "stars"]]
print("First Letter",first_letters)

# 5. Multiples of 5 between 1 and 50
multiples_of_5 = [x for x in range(1, 51) if x % 5 == 0]
print("Multiple of 5",multiples_of_5)

# 6. Flat 2D list
flat_list = [item for sublist in [[1, 2, 3], [4, 5], [6, 7, 8]] for item in sublist]
print("Flat List",flat_list)

# 7. Replace vowels with *
text = "programming is fun"
vowels = "aeiouAEIOU"
replaced_text = ''.join(['*' if char in vowels else char for char in text])
print("Replaced Text",replaced_text)

# 8. Tuples (number, square) from 1 to 8
number_squares = [(i, i**2) for i in range(1, 9)]
print("Number Squares: ",number_squares)

# 9. All pairs from two lists
pairs = [(x, y) for x in ["red", "blue"] for y in ["pen", "book", "bag"]]
print("Pairs",pairs)

# 10. Numbers from 1 to 10
numbers_1_to_10 = [i for i in range(1, 11)]
print("Number 1 to 10 are: ",numbers_1_to_10)

# 11. Squares of numbers from 2 to 6
squares_2_to_6 = [i**2 for i in range(2, 7)]
print("Square 2 to 6 are:",squares_2_to_6)

# 12. Double each number
doubled = [x*2 for x in [2, 4, 6, 8, 10]]
print("Doubled are:",doubled)

# 13. Convert to uppercase
words_upper = [word.upper() for word in ["cat", "dog", "cow"]]
print("Words Upper are:",words_upper)

# 14. First letter of each word
first_letters_names = [word[0] for word in ["Ali", "Sara", "Usman", "Hamza"]]
print("First Letters are:",first_letters_names)

# 15. Even numbers 1 to 20
even_numbers_1_20 = [x for x in range(1, 21) if x % 2 == 0]
print("Even Numbers 1 to 20 are:",even_numbers_1_20)

# 16. Characters of 'python'
chars_python = [char for char in "python"]
print("Characters of python are:",chars_python)

# 17. Numbers 1 to 20 divisible by 3
div_by_3 = [x for x in range(1, 21) if x % 3 == 0]
print("Numbers 1 to 20 divisible by 3 are:",div_by_3)

# 18. Cubes of [1,2,3,4,5]
cubes = [x**3 for x in [1, 2, 3, 4, 5]]
print("Cubes are:",cubes)

# 19. Lengths of words
lengths_words = [len(word) for word in ["hi", "hello", "morning"]]
print("Lengths of words are:",lengths_words)

# 20. Odd numbers from 1 to 9
odd_numbers_1_9 = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 2 != 0]
print("Odd Numbers from 1 to 9 are:",odd_numbers_1_9)

# 21. Numbers 1 to 50 divisible by 2 and 5
div_2_5 = [x for x in range(1, 51) if x % 2 == 0 and x % 5 == 0]
print("Numbers 1 to 50 divisible by 2 and 5 are:",div_2_5)

# 22. Names starting with 'A'
names = ["Usama", "Ayesha", "Sidra", "Mughees", "Talha", "Aun"]
names_start_A = [name for name in names if name.startswith('A')]
print("Names starting with A are:",names_start_A)

# 23. (number, cube) pairs 1 to 5
number_cube_pairs = [(x, x**3) for x in range(1, 6)]
print("Number and Cube pairs are:",number_cube_pairs)

# 24. Flatten list
nested_list = [[10, 20], [30, 40], [50, 60]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened List is:",flattened_list)

# 25. Lengths of each word in sentence
sentence = "Python makes coding easy"
lengths_sentence = [len(word) for word in sentence.split()]
print("Lengths of each word in sentence are:",lengths_sentence)


# 26. Replace vowels with *
text2 = "beautiful day"
replaced_text2 = ''.join(['*' if char in vowels else char for char in text2])
print("Replaced Text 2 is:",replaced_text2)

# 27. Cubes of even numbers 2 to 16
even_cubes = [x**3 for x in range(2, 17) if x % 2 == 0]
print("Cubes of even numbers 2 to 16 are:",even_cubes)

# 28. Positive numbers only
numbers_list = [5, -3, 8, -1, 0, -7, 2]
positive_numbers = [x for x in numbers_list if x > 0]
print("Positive Numbers are:",positive_numbers)

# 29. All pairs (x, y)
x_list = [1, 2, 3]
y_list = ["a", "b", "c"]
all_pairs = [(x, y) for x in x_list for y in y_list]
print("All Pairs are:",all_pairs)