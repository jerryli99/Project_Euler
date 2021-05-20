__author__= 'Jerry Li'
count = 0
sum = 0
for i in range (1, 1000):
    if(i % 5 == 0 or i % 3 == 0):
        sum = sum + i
print(sum)

#final answer: 233168