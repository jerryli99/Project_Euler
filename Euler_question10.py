__author__ = 'Jerry Li'
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        # number = num1 * num2; if number is prime,
        # num1 <= sqrt(number) and num2 >= sqrt(Number)
        #if number can be factorized, then it is not a prime number
        if n % i == 0:
            return False
    return True

def my_solution(sum):
    for i in range(2, 2000000):
        if isPrime(i):
            sum += i
    print(sum)

my_solution(0)

#answer is: 142913828922