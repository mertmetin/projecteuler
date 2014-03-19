def numof_collatz(num):
    q = 1
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        q = q + 1
    
    return q

numOfSeq = 0
number = 0
for i in range(13, 1000000):
    temp = numof_collatz(i)
    if temp > numOfSeq:
        numOfSeq = temp
        number = i
        
print number
        
