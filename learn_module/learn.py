import re

str1 = "Faisal,Sohail,Khan,Babur are good at playing acrobatic games . AAA is triple As. Faisal"

p = re.compile(r"[A]+[a-z]*", flags=re.M)

rv= p.match(str1)
print(rv)
print(type(rv))
