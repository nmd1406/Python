test = int(input())
for i in range(test):
    n = int(input())
    arr = set(map(int, input().split()))
    maxNum = max(arr)
    minNum = min(arr)
    print(maxNum - minNum - len(arr) + 1)