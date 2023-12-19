import math

test = int(input())


def solve(n):
    res = "1 * "

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count = 0
            while n % i == 0:
                count += 1
                n /= i

            res += (str(i) + "^" + str(count) + " * ")

    if n > 1:
        res += (str(int(n)) + "^1")
    else:
        res = res[:-3:]

    return res


while test > 0:
    n = int(input())
    print(solve(n))
    test -= 1
