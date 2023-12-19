factorial = [1] * 10

for i in range(1, 10):
    factorial[i] = i * factorial[i - 1]


def isKrish(n):
    num = n
    sum = 0
    while num != 0:
        sum += factorial[num % 10]
        num //= 10

    return sum == n


test = int(input())

while test > 0:
    n = int(input())

    if isKrish(n):
        print("Yes")
    else:
        print("No")

    test -= 1
