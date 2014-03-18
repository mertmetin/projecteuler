num = 600851475143
list = []

i = 2
while i*i <= num:
    while (num % i) == 0:
        list.append(i)
        num /= i
    i+= 1
    
if num > 1:
    list.append(num)    

print list[-1]
