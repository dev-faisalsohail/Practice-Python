s2 = {3.5,6.4,2.5,7.96}
print(s2,type(s2))

s2 = set([3.5,6.4,2.5,7.96])
print(s2)

s3 = set()
print(s3)
print(type(s3))

s4 = {}
print(s4)
print(type(s4))


mylist = [2,4,6,8,7,3,3,2]
print("\nList: ",mylist)
myset = set(mylist)
print("List converted to set:", myset)


mylist1 = ['faisal','atif','rizwan','rafi']
print("\nList: ",mylist1)
myset1 = set(mylist1)
print("List converted to set:", myset1)



s1 = {"Kiran", 30,5.5,True,(10,'hrm')}
print(s1)


s2 = (["Kiran", 30,5.5,True,(10,'hrm')])
print(s2)

# you can unpack set elements

myset = set(['learning','is','fun','with','Kiran'])
print(mylist)
a,b,c,d,e = myset # the number of variables on the left must match the 
print(a,b,c,d,e)

# you can pack individtual elemnt to a set

t1 = a,b,c,d,e
set2 = set(t1)
print(set2)
print(type(set2))

print(flush=True)

print(end='')

print(sep="")


# But you can loop through the set items using a for loop

myset = set (['learning','is','fun','with','Kiran'])

for i in myset:
  
  import time
  time.sleep(2)
  print(i, end=' ' )
  print("True####")
  for i in myset:
    import time
    time.sleep(2)
    print(i, end=' ', flush=False)