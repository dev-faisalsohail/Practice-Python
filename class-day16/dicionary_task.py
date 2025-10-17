import copy

students = [
  {"name":"Hashim","age":18,"grade":"B"},
  {"name":"Slman","age":11,"grade":"B"},
  {"name":"Mazhar","age":12,"grade":"B"},
  {"name":"Fahan","age":22,"grade":"B"},
  {"name":"Bilal","age":19,"grade":"B"},
  {"name":"Zalid","age":17,"grade":"B"},
]

print(students)


def func2(item):
  return item.get("age")

age_sorted = sorted(students, key = func2)


print(age_sorted)


dict1 = {
  'Faisal': 90,
  'Rizwan': 76,
  'Atif': 73,
  'Fasi': 93,
}

dict2 = dict1 

print('ID of dict1:', id(dict1))
print('ID of dict2:', id(dict2))


dict2["Sohail"] = 89

print('\ndict1', dict1)
print('dict2', dict2)

dict2 = dict1.copy()

print(dict2)

dict2 = copy.deepcopy(dict1)

print(dict2)


print('ID of dict2:', id(dict1))
print('ID of dict2:', id(dict1))

