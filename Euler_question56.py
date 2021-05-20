__author__ = 'Jerry Li'

result = max(sum(int(c) for c in str(a**b)) for a in range(100) for b in range(100))
print(result)

# The answer is: 972