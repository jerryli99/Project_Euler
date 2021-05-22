#__author__ = 'Jerry Li'
count = 0
for i in range(1, 10):
    nth_power = 1
    while True:
        if nth_power == len(str(i**nth_power)):
            count = count + 1
        else:
            # Since 1^1, 1^2, 1^3, ..., and 2^1, 2^2, and 2^3, ... have single digit numbers,
            # we need to break the while loop to continue the next term i
            break
        nth_power = nth_power + 1
print(count)

# The answer is: 49
