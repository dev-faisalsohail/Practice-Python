# in set we access an element by for loop
# but you can loop through the set items using a far loop
# by default for loop running the whole sequence 

# create an empty set

# add method on add one element

set1 = set()
set1.add(25)
set1.add(73)
print (set1)

# if we want to add multiple adds than we use update method 

set2 = set([5,3,23])
set2.update('kiran')
print(set2)

set3 = set([3,6,22])
set3.update({'kiran','khursheed','53'})
print(set3)

expl = set3.pop()

print("element pop", expl)
print("set now is:", set3)
print("element pop", expl)
print("set now is:", set3)
print("element pop", expl)
print("set now is:", set3)
print("element pop", expl)
print("set now is:", set3)

# pop() method return an element 


# remove method

s4 = set(['Welcome','to','course','of ','Advanced','Python'])
print("\nOriginal set: ", s4)
x = s4.remove('course')
print("after remove work", s4)
print("are urn value o remove () is :", x)

# discard () method


s5 = set()
help(s5.discard)

hlp = set()
help(hlp.discard)

s7 = set(['Welcome','to','advanced','course','of','advanced','python','with'])

y = s7.discard('kiran')
print (y)

print(s7.clear())


str1 = 'Learning is fun' # this is a string 

# by default split data type is list
set1 = set(str1.split(' '))
print(set1)
print(type(set1))



set3 = {'This','is','getting','more','and','more','interesting'}
print('/' .join(set3))
print(type(set3))


set_no=set([3,4,6,8,1,0,8,2])

print("length of set: ", len(set_no))
print("max element of set: ", max(set_no))
print("min element of set: ", min(set_no))
print("sum of set: ", sum(set_no))


# union of set

set1 = {'kiran', 'khursheed'}

set2 = {'aaraizz','shifa','abdul ahad'}


set3 = set1 | set2
set4 = set1.union(set2)

set5 = set1 - set2
set6 = set.difference(set2) 

print("set1:", set1)
print("set2:", set2)
print("set3:", set3)
print("set1 | set2:", set3)
print("set1-set2", set4)
print("set1 - set2:", set5)
print("set1-set2", set6)



