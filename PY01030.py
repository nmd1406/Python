import math

n, k = map(int, input().split())
start = 10 ** (k - 1)
end = 10 ** k

count = 0
for i in range(start, end):
    if math.gcd(i, n) == 1:
        print(i, end=" ")
        count += 1
    if count == 10:
        count = 0
        print()
