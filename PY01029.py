import math

test = int(input())
while test > 0:
    n = int(input())
    rev = int(str(n)[::-1])

    if math.gcd(n, rev) == 1:
        print("YES")
    else:
        print("NO")

    test -= 1
