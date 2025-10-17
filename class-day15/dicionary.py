# motivation to use dictionary 
# in old version it's un ordered but after(python 3.7 version) in dictionary it's orders
students = ['Rizwan','Rafi','Atif']

marks = [54,66,45]

i = students.index('Rafi')
print(marks[i])


def get_marks(name):
  i = students.index(name)
  return marks[1]


# A dictionary with strings keys, and integer values, showing 
dict1 = {
  'Faisal' : 23,
  'Rafi' : 54,
  'Rizwan' : 55,
}

print(dict1)
print(type(dict1))
print(id(dict1))


# Proof of concept
# keys inside dictionaries must be of imuteable 
# Dictoionary 

# Creating a nested dictionary

dict7 = {
  'name':'Faisal',
         'occupation':'Consultant',
         'address' :
           {
             'house#' : 3, 'area' : 'xyz', 'city': 'lahore' , 'phone' : '0300-00000'},
}

print(dict7)

d1 = {
  'name': 'Sohail',
  'age':  '30',
  'marks': '554',
  'address': 'Multan,pakistan',
}


print(d1['address'])

print(d1.get('marks'))

print(d1.items())
print(d1.keys())
print(d1.values())


d1['address'] = 'Lahore'

print(d1)


d1['status'] = 'single'

print(d1)


d1.update({'name':'Faisal_Khan'})

print(d1)

d1.update({'Father_Name':'Sohail_Khan'})

print(d1)


d2 = {
  'name': 'Maaz',
  'age':  '27',
  'marks': '3432',
  'address': 'Multan(Mutazabad),pakistan',
}


d1.update(d2)

print(d1)

del d1['address']

print (d1)


d1.popitem()

print(d1)

d1.popitem()

print(d1)

d1.pop('name')

print(d1)

rn = d1.items()
print(rn)

rv = d1.items()
print(rv)
print("\n",type(rv))


mylist = list(d1.values())
print("\n", mylist)


print(sorted(dict1, reverse=True))


print(sorted(dict1))


d2 = sorted(dict1)

print(d2)


d2 = sorted(dict1.keys())

print(d2)

d2 = sorted(dict1.values())

print(d2)

dict1.items()

print(dict1)


def func1(item):
  return item[1]

mylist = sorted(dict1.items(), key=func1)

print(mylist)

mylist = sorted(dict1.items(), key=func1, reverse=True)

print(mylist)





dict2 = {
    "apple": 5,
    "banana": 2,
    "mango": 7,
    "orange": 3
}

tu1 = tuple(dict2.items())
print(tu1)

def func2(item):
  return item[1]


mylist1 = sorted(dict2.items(), key=func2)

print(mylist1)

mylist1 = sorted(dict2.items(), key=func2, reverse=True)

print(mylist1)


print("Orignal Dict2 :",mylist1)

print("Tuple: ", tu1)



