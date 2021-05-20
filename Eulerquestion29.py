__author__ = 'Jerry Li'
# since a set does not contain duplicate items,
# we can add the numbers to the set
temp = set()
for i in range (2, 101):
    for j in range (2, 101):
        temp.add(int(i ** j))
print(len(sorted(temp)))

# The answer is: 9183