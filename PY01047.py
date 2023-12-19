import math

test = int(input())


def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True


while test > 0:
    string = input()
    num = int(string[-4::])

    if isPrime(num):
        print("YES")
    else:
        print("NO")

    test -= 1
