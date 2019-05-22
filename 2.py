from random import random

n = 25
x = []
for i in range(n):
    x.append(int(random()*100))
x.sort()
print(x)

print('Enter number:')
number = int(input())

min = 0
max = n-1
while min <= max:
    mid = (min + max) // 2
    if number < x[mid]:
        max = mid - 1
    elif number > x[mid]:
        min = mid + 1
    else:
        print("Index:", mid)
        break
else:
    print("Doesn't exist.")