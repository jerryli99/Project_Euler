#__author__ = 'Jerry Li'


import math
#from 600851475143 to 1, decrement
for i in range(int(math.sqrt(600851475143)),1,-1):
    if 600851475143 % i == 0:
        flag = False
        for j in range(int(math.sqrt(i)),1,-1):
            if(i % j ==0):
               flag = True
        if(flag!=True):
            print(i)
            break

#result is 6857
