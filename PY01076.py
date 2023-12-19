import math

test = int(input())

while test > 0:
    a = int(input())
    b = int(input())

    print(math.gcd(a, b))

    test -= 1
