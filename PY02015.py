def check(arr):
    return arr.count(arr[0]) == len(arr)


while True:
    arr = list(map(int, input().split()))
    if check(arr) and arr[0] == 0:
        break

    count = 0
    while not check(arr):
        temp = arr[0]
        for i in range(3):
            arr[i] = abs(arr[i] - arr[i + 1])

        arr[3] = abs(arr[3] - temp)
        count += 1

    print(count)