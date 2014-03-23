FILE = 'nums.txt'
sum = 0
with open(FILE) as f:
    for line in f:
        sum+= int(line)

result = str(sum)
print result[:10]
