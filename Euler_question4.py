__author__ = 'Jerry Li'
max = 0
for i in range(100,1000):
    for j in range(100,1000):
      mult = i * j
      # Check if the number is palindrome
      if str(mult) == str(mult)[::-1]:
          if mult > max:
              max = mult
              print(i, "*" ,j, "=", max)

print (max)

#The result is 906609