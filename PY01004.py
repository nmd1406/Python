import math


def isPrime(n):
    if n < 2:
        return False

    i = 2
    j = int(math.sqrt(n))

    while i <= j:
        if n % i == 0:
            return False

        i += 1

    return True


test = int(input())

while test > 0:
    num = int(input())

    count = 0
    for i in range(1, num):
        if math.gcd(i, num) == 1:
            count += 1

    if isPrime(count):
        print("YES")
    else:
        print("NO")

    test -= 1
