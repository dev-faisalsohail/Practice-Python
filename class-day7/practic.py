str = 'Python Programming is fun'
print('original_string =', str)

#access first index
print('str[0] =', str[0])


#Negative index start from the opposite end of the string
print('First negative index =', str[-1]) 

#access second  last index
print('str[-2] =', str[-2])

print('str[-5] =', str[-5]) #access from index 0 to 5

# To find out the index of a specific character in a string
str1 = "Welcome to Python Programming"
str1.index('gram')
print('index of a specific character =', str1.index('gram'))

str2 = "Welcome to Python Programming"
str2.index('ing') # returns the index of first occurrence of 'ing
print("Index of 'ing' in str1 is:", str2.index('ing'))

print(id(str2)) # print the memory address of str2

# assigning a new value is valid

str2 = "Faisal Khan"

print(id(str2)) # print the memory address of str2

# Reverse a string  
str5 = "0123456789"
print(str5[len(str5):0:-1])# Reverse the string

print(str5[-5:1:-2]) # Reverse from index 5 to 1
print(str5[::-2])


str1 = ' Faisal'
str2 = ' Sohail'
str3 = str1 + str2
print(' str1 + str2 = ', str3)
print(str3[7:])
print("Y" + str3[:-7])

str6 = "Learning is fun with kiran"
print(str6[21:26:]) # Reverse the string
print(str6[21:26:2]) # Reverse the string

bufferr="              hello world, this is python programming     learning from mam kiran Khursheed          "
rn = bufferr.lstrip()
print(bufferr)
print(rn)

bufferr.rstrip()