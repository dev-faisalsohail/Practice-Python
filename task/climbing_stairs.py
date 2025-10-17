def climbStairs(n):
    if n <= 2:
        return n
    first, second = 1, 2
    for i in range(3, n + 1):
        total = first + second
        first = second
        second = total
    return second


  
print(climbStairs(2))  
print(climbStairs(3)) 
print(climbStairs(4))  
print(climbStairs(5))  
