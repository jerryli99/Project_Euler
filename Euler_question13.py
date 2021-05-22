#__author__ = 'Jerry Li'
filePath = '100numbers_50digit.txt'
line = open(filePath, 'r')
nums = [sum(int(i) for i in line)]
print(nums)

#result: [5537376230390876637302048746832985971773659831892672]
#the answer is: 5537376230
