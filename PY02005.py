n = int(input())
list = list(map(int, input().split()))

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if list[i] > list[j]:
            count += 1
        

print(count)