list1 = ["Faisal", 90, 5.5, 5 < 3, [10, 'Sohail']]
print(list1)
print(type(list1))

numbers = [10,20,30,40,50]
print(id(numbers))  # memory id دکھاتا ہے
numbers[2] = 555    # value بدل دی
print("number: ", numbers)
print(id(numbers))  # id وہی رہی


num = [20,44,65,42,11]
print(id(num))
num [4] = "Faisal"
print("Name:", num )
print(id(num))


mylist = ['learning','is','fun','with','Kiran']
a,b,c,d,e = mylist # the number of variables on the left must match
print(a,d,e)
print(type(a))


new_list = ['faisal', 'khan','babar']

print(new_list)
f,g,h = new_list
print(f,g,h)


tuple1 = a,b,c,d,e  
print(mylist)

list5 = ['a','b','c','d','e','f','g','h','i']
print(list5[::-1])   # ['i','h','g','f','e','d','c','b','a']
print(list5[5:1:-1]) # ['f','e','d','c']
print(list5[::-2])   # ['i','g','e','c','a']
print(list5[:4:])
print(list5[1:-4:])
print(list5[::])
print(list5[-9:3:])
print(list5[-9:3:-1])
print(list5[:3:-1])
print(list5[-8:3:])
print(list5[-9:3:])
print(list5[-9:3:])
print(list5[-9:3:])
