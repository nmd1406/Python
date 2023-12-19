n = int(input())
arr = [int(num) for num in input().split()]
res = []

for num in arr:
    if len(res) == 0:
        res.append(num)
    else:
        if (res[-1] + num) % 2 == 0:
            res.pop()
        else:
            res.append(num)

print(len(res))
