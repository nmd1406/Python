import math


def isPrime(num):
    if num < 2:
        return "NO"

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return "NO"

    return "YES"


test = int(input())

while test > 0:
    inp = input()
    sum = 0
    for ch in inp:
        sum += int(ch)

    print(isPrime(sum))

    test -= 1
