import math

test = int(input())


def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


while test > 0:
    inp = input()
    count = 0

    for char in inp:
        if char == '2' or char == '3' or char == '5' or char == '7':
            count += 1

    # print(count)

    if (count > len(inp) - count) and isPrime(len(inp)):
        print("YES")
    else:
        print("NO")

    test -= 1
