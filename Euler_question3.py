__author__ = 'Jerry Li'
number = 600851475143
incrementNumber = 2
while number != 1:
    if not number % incrementNumber:
        number /= incrementNumber
    else:
        incrementNumber += 1
print(incrementNumber)


#The answer is: 6857
