import math

test = int(input())


def isPrime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n < 2:
        return False

    i = 2
    j = int(math.sqrt(n))

    while i <= j:
        if n % i == 0:
            return False

        i += 1

    return True


def check(string):
    num = int(string)
    sum = 0
    while num > 0:
        if not isPrime(int(num % 10)):
            return False
        sum += int(num % 10)
        num //= 10

    return isPrime(sum) and isPrime(int(string)) and isPrime(int(string[::-1]))


while test > 0:
    string = input()

    if check(string):
        print("Yes")
    else:
        print("No")
    test -= 1
