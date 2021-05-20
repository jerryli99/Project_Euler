__author__ = 'Jerry Li'
import math

smallestCommonMultiple = 1
for i in range (1, 21):
    smallestCommonMultiple = int((smallestCommonMultiple * i) / math.gcd(smallestCommonMultiple, i))
print(smallestCommonMultiple)

# The answer is: 232792560