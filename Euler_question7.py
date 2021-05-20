__author__ = 'Jerry Li'
count = 0
for num in range(1, 1000000):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           count  +=1
           if count == 10001:
               print(num)
               break;


#answer: 104743