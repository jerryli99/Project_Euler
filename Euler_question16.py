__author__ = 'Jerry Li'
num = 0

def two_to_the_nth_power(power):
    return str(2 ** power)

print(list(map(int, two_to_the_nth_power(1000))))
print(sum(map(int, two_to_the_nth_power(1000))))

# the answer is 1366