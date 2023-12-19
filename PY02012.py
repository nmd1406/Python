n = int(input())
arr = []
while True:
    arr += list(map(int, input().split()))
    if len(arr) == n:
        break

odd = []
even = []
mark = [False] * n

for i in range(n):
    if arr[i] % 2 == 0:
        even.append(arr[i])
        mark[i] = True
    else:
        odd.append(arr[i])

even.sort()
odd.sort(reverse=True)
for i in range(n):
    if mark[i]:
        print(even.pop(0), end=" ")
    else:
        print(odd.pop(0), end=" ")