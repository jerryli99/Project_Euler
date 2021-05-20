__author__ = 'Jerry Li'

# In order to find the nth fibonacci number, we can use Binet's formula
goldenRatio = (1 + 5 ** 0.5) / 2


# print(goldenRatio)

def theNthFibonacciNumber(n):
    nth_fibonacciNumber = ((1 + 5 ** 0.5) ** n - (1 - 5 ** 0.5) ** n) / (2 ** n * 5 ** 0.5)
    return nth_fibonacciNumber


# print(int(theNthFibonacciNumber(100)))
# However, I don't know how to do it for now, so I use brute force


def numberOfDigits(numberOfDigits):
    a = 1
    b = 0
    n = 1
    while len(str(a)) != numberOfDigits:
        a, b = a+b, a
        n = n + 1
    print (n, "has 1000 digits")

numberOfDigits(1000)
# The answer is: 4782