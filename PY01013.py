import math

test = int(input())


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


def solve(n):
    sum = 0
    while n > 0:
        sum += (n % 10)
        n //= 10

    return isPrime(sum)


while test > 0:
    a, b = map(int, input().split())
    if solve(math.gcd(a, b)):
        print("YES")
    else:
        print("NO")

    test -= 1
