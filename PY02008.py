prime = [True] * (10 ** 6 + 1)

prime[0] = False
prime[1] = False
for i in range(2, 1001):
    if prime[i]:
        for j in range(i * i, 10 ** 6 + 1, i):
            prime[j] = False


n, x = map(int, input().split())

arr = []
itr = 0
while len(arr) < n:
    if prime[itr]:
        arr.append(itr)
    itr += 1

print(x, end=" ")
for i in range(n):
    x += arr[i]
    print(x, end=" ")