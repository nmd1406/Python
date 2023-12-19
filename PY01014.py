a, k, n = map(int, input().split())

arr = []
b = k - (a % k)
n -= a

while b <= n:
    arr.append(b)
    b += k

if arr:
    for num in arr:
        print(num, end=" ")
else:
    print(-1)
