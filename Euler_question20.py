__author__ = 'Jerry Li'
def factorial(num):
    if num == 1:
        return num
    elif num < 1:
        return False
    else:
        return num * factorial(num - 1)

def addNumbers(n):
    factorialNumber = factorial(n)
    sumOfNumbers = 0
    for i in str(factorialNumber):
        sumOfNumbers += int(i)
    return sumOfNumbers

print(addNumbers(100))

# The answer is: 648