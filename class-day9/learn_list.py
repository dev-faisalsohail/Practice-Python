# learn list

list1 = ["Faisal", 90, 5.5,5 < 3, [10, 'Sohail']]
print(list1)
print(type(list1))

# Proof of concepts

numbers = [10,20,30,40,50]
print(id(numbers))
numbers[2] = 555
print("number: ", numbers)
print(id(numbers))


# lists can have duplicate emements

names = ['Kiran','Khursheed']

# lists can be nested to arbitary depth

# Packing and unpacking lists

# Unpacking list

mylist = ['learning','is','fun','with','Kiran']
a,b,c,d,e = mylist # the number of variables on the left must match
print(a,d,e)
print(type(a))


# you can pack individual elements to a list

tuple1 = a,b,c,d,e

mylist2 = list(tuple1)
print(mylist2)
print(type(mylist2))

# 

list3 = ["Kiran",90,5.5,[10,'khursheed']]
print(list3[3])

#accessing nested list element

print(list3[0][2])

print(list3[3][1])

print(list3[3][1][5])


print(list3[3][1][6:].capitalize())

print(list3[1]+list3[2]+list3[3][0])


# index()
#print(list3.idex("Kiran"))

#Reverse slicing

list5 = ['a','b','c','d','e','f','g','h','i']
print(list5[::-1]) # take 1 step back each time
print(list5[5:1:-1]) # take 1 step back each time of start os ;ess tjam eemd om case pf a negative step it will return empty string
print(list5[2:10:-1]) # 
print(list5[::-2]) # take 2 step back


# Eid Sweets List

# Create a list of eid sweets - 5
# print threee deserts from the list

feast = ["Swaiyan","Dhai-Bhally","Cake","Sweets","Bottle"]

print(feast[1:4])
print(feast[1:3:-1])


# Eid Preparation
'''# list of 100 Faisal's

buf = ['Faisal']
newbuf = buf * 100
print(newbuf)
len(newbuf)'''



mylist = ['advance python','machine learning',2,5,7]
mylist1= ['Faisal','data analytical','Exd Education']
mylist[0:1] = ['math','stat']
mylist.append('hello')
mylist.extend(mylist1)

# note we using a slice instead of single index, although it means just zero

print(mylist)

print(mylist[0:1] == mylist[0])


# Aliasing 

list1 = [1,2,3,4]
list2 = list1
list2 [2] = 9

# shaloolow 
list1 = [1,2,3,4]
list2 = list1
list2 [2] = 9


list1 = [1,2,3,4]
list2 = list1
list2 [2] = 9










