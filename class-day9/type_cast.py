# convert a string into list suing list()

str1 = 'Learning is fun'  # this is a string

print(type(str1))


# str.split() to split a List into strings

# used to tokenize a string based on some delimiter, which ca be stored in a list
# it returns a list having tokens of the string based on spaces if o arugments is passedd


list_num = [3,8,1,8,0,8,4]

print("length of list:",len(list_num))
print("max element in list:",max(list_num))
print("min element in list:",min(list_num))
print("sum of element list:",sum(list_num))


# aliasing python : nickname, new name  1 memory has more than one pointers 
# shallow copy create a new list it's a solution of aliasing

# aliasing : assignment operator = make new address same memory location
# Shallow copy: same memory location slicing 
# deep copy: create a new object and recursively creates indendpent copy of original object and all its neested objects 

s# sorting a list : it's return none