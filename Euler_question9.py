__author__ = 'Jerry Li'
sum = 1000
for a in range(1, 1001):
    for b in range(1, 1001):
        c = sum - a - b
        if a < b < c:
            if a * a + b * b == c * c:
                print(a, b, c)
                print("Answer: " + str(a * b * c))
                
# answer is: 31875000