test = int(input())

while test > 0:
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(d, n):
        print(arr[i], end=" ")

    for i in range(d):
        print(arr[i], end=" ")

    print()
    test -= 1
