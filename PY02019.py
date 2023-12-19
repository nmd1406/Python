import math


n = int(input())
numList = sorted(map(int, input().split()))

for i in range(n - 1):
    for j in range(i + 1, n):
        if math.gcd(numList[i], numList[j]) == 1:
            print(numList[i], numList[j])