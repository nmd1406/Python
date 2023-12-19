n = int(input())
arr = list(map(float, input().split()))

minNum = min(arr)
maxNum = max(arr)
while minNum in arr:
    arr.remove(minNum)
while maxNum in arr:
    arr.remove(maxNum)

print(round(sum(arr) / len(arr), 2))