# Find method use for searching a substring in a string
# It returns the lowest index of the substring if it is found in given string. If it's not found then it returns -1

str1 = 'LearningAdvancedPythonProgrammingS'
print(str1.find('Learn'))
print(str1.find('Python'))

print(str1.find('s',2))  # start searching from index 2
print(str1.find('s',2))  # case senstive

print(str1.find('S',0,4))  # third arugment stops searching uptill that index
print(str1.find('S',0,5)) # third arugment stops searching uptill that index