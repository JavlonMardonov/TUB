import math
print('Son kiriting: ')
a = int(input())
count = 0
n = 2
while n <= math.sqrt(a):
    if a % n == 0:
        count = count + 1
    n = n + 1
if count != 0:
    print("Tub emas")
else:
    print("Tub")
