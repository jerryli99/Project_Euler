#__author__ = 'Jerry Li'
'''
Since we can only move to the right and down starting from the top left corner, 
there will be 40 steps in a 20 * 20 grid to reach to the bottom right corner.
20 steps in the x direction and 20 steps in the y direction.
We can convert the problem into "In the set of 40 elements, how many ways are there to 
choose 20 elements?" 
Why this question? If we have two choices every time we move: right or down, the 
two choices result a total of 20 times of checking for each right and down moves. 
Therefore, it will be 40 choose 20. 
'''


def factorial(num):
    if num == 1:
        return num
    elif num < 1:
        return False
    else:
        return num * factorial(num - 1)


# Combinatorial
print(int(factorial(40) / (factorial(20) * factorial(20))))

# the answer is: 137846528820
