def last(s):
  return s[-1]


t1 = ('abcz','xyza','bas','kiran')
rv = sorted(t1, key=last)
print(rv)
print(t1)