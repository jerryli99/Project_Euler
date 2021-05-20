__author__ = 'Jerry Li'
sum1 = 0
sum2 = 0
for i in range (1, 101):
    sum1 += i**2
print(sum1)

for j in range (1,101):
    sum2 += j
print(sum2**2 - sum1)

#answer is : 25164150