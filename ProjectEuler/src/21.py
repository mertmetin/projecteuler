def sum_divisors(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum+= i
    return sum 

sumOfAmicables = 0    
for i in range(0,10000):
    a = sum_divisors(i)
    b = sum_divisors(a)
    if i == b:
        if i != a:
            sumOfAmicables+= i
           
print sumOfAmicables
    
    