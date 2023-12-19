import math


n = int(input())
row = [0] * n
col = [0] * n
arr = []
for i in range(n):
    arr.append(input())

for i in range(n):
    for j in range(n):
        if arr[i][j] == "C":
            row[i] += 1
            col[j] += 1

res = 0
for i in range(n):
    res += math.comb(row[i], 2) + math.comb(col[i], 2)

print(res)