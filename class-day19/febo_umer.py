x = int(input("Enter the number till while: "))

n = 0
n1 = 1

if x == n:
  print(n)
elif x ==n1:
  print(n,n1)
else:
  list1 = [n,n1]
  i = 2
  while(i<=x):
    n2 = n + n1 
    list1.append(n2)
    n=n1
    n1=n2
    i= i+1
    print(list1)