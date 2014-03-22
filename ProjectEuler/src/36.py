LIMIT = 1000000

def is_palindrome(num):
    return num == num[::-1]

sum = 0
for i in range(1, LIMIT, 2):
    if is_palindrome(str(i)) == True and is_palindrome(str(bin(i))[2:]):
        sum+= i
        
print sum
