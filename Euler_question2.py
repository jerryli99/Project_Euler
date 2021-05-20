__author__ = 'Jerry Li'
a, b = 1, 1
sum = 0
while a <= 4000000:
    if a % 2 == 0:
        sum += a
    a, b = b, a+b
print (sum)

#result is: 4613732