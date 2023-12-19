n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n - 1, i, -1):
        sum1 += arr[i][j]

for i in range(1, n):
    for j in range(i):
        sum2 += arr[i][j]

diff = abs(sum1 - sum2)
if diff <= k:
    print("YES")
else:
    print("NO")
print(diff)