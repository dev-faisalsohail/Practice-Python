str1 = ' Faisal'
str2 = ' Sohail'
str3 = str1 + str2
print(str3)
print(str3[7:])
print("Y" + str3[:-7])


# A string can be replicated/repeated using * operator
str4 = 'Hello '
print('str4 * 3 = ', str4 * 3)

buffer = 'F' * 40
print(buffer)  # prints 40 F's


"Faisal" * 50  # creates a string with 50 Faisal's
print("Faisal" * 50)

# learn lower and upper functions
str5 = "Learn Python Programming from Mam Kiran"

print('Original String =', str5)

rv = len(str5)
print('Length of str5 =', rv)

rv = str5.lower()
print('str5.lower() =', rv)

print('str5.upper() =', str5.upper())

rv = str5.capitalize()
print('str5.capitalize() =', rv)  
print('original string =', str5)     # original string is unchanged

str6 = "Learning is fun with kiran"
print(str6[21:26:2]) # Reverse the string


bufferr="              hello world, this is python programming     learning from mam kiran Khursheed          "
rn = bufferr.strip()
print(bufferr)
print(rn)

bufferr
bufferr.lstrip()


bufferr
bufferr.rstrip()


# start string indexing and slicing


str7 = "Learning is fun with Kiran Khursheed"

rz = str7.startswith('Learning')
print(rz)

rz = str7.startswith('Kiran')
print(rz)

rz = str7.startswith('kiran',21)
print(rz)

# case senstive

rz = str7.startswith('kiran',21)
print(rz)

rz = str7.startswith('arn',3)
print(rz)