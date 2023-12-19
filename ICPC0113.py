import math

prime = [True] * 1000005
prime[0] = prime[1] = False

for i in range(2, 1000):
    if prime[i]:
        j = i * i
        while j <= 1000000:
            prime[j] = False
            j += i


test = int(input())

while test > 0:
    n = int(input())

    mark = {}
    for i in range(13, n):
        revNum = int(str(i)[::-1])
        if prime[revNum] and prime[i] and revNum != i and revNum < n and revNum not in mark:
            print(i, revNum, end=" ")
            mark[i] = mark[revNum] = 1

    print()
    test -= 1
