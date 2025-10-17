# how to access characters in a string using indexing
#Indexing starts from 0
'''
str = 'Python Programming is fun'
print('str =', str)
#access first index
print('str[0] =', str[0])

#Negative index start from the opposite end of the string
print('str[-1] =', str[-1]) 

#access second  last index
print('str[-2] =', str[-2])

print('str[-5] =', str[-5]) #access from index 0 to 5

# To find out the index of a specific character in a string
str1 = "Welcome to Python Programming"
str1.index('ing') # returns the index of first occurrence of 'ing
print("Index of 'ing' in str1 is:", str1.index('ing'))

# strings are immutable , means string object does not support imtem assigment

str2 = "Faisal Sohail"

print(id(str2)) # print the memory address of str2

# assigning a new value is valid

str2 = "Faisal Khan"

print(id(str2)) # print the memory address of str2


#The object Faisal Sohail is now orphan, since there is no variable referring to it now and will be destroyed by garbage collector in future



'''

str3 = "LearningAdvancedPythonProgramming"
str6 = "Learning is fun with kiran"

print (str3[0:4]) # From the start till before the 4th index

print(str3[:4])
print(str3[11:16])
print(str3[11:]) # From 11th index to the end
print(str3[19:len(str3)]) # From start to end with a step of 2
# if start is greater than end,it will return an empty string
print(str3[5:2])
print(str3[-5:-2])
print(str3[:]) # From start to end

# in python space ( ) is also a character
str4 = "Learning"
print(str4[::1]) # From start to end with a step of 1
print(str4[::2]) # From start to end with a step of 2
print(str4[::4]) # From start to end with a step of 4


# Reverse a string  
str5 = "0123456789"
print(str5[len(str5):0:-1])# Reverse the string

print(str5[5:1:-1]) # Reverse from index 5 to 1
print(str5[::-2])

