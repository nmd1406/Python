test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(arr.index(max(arr)), k)
    for num in arr:
        if num < 0:
            print(num, end=" ")
    
    for num in arr:
        if num >= 0:
            print(num, end=" ")
    print()