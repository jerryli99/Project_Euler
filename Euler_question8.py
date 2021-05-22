#__author__ = 'Jerry Li'

file = open("Euler_question8_1000_digits.txt", "r")
number = file.read().replace("\n", "")
print(number)

max = 0
for i in range(len(number)):
    num = 1
    a_13_digit_string = number[i:i+13]
    for j in a_13_digit_string:
        num *= int(j)
    if num > max:
        max = num
print(max)

# The answer is: 23514624000
