test = int(input())

while test > 0:
    n = int(input())

    arr = [int(num) for num in input().split()]
    arr.sort()

    count = 0
    for i in range(0, n - 1):
        l = i + 1
        r = n - 1
        curr = arr[i]

        while l < r:
            if (curr + arr[l] + arr[r] == 0):
                count += 1
                l += 1
            elif (curr + arr[l] + arr[r] < 0):
                l += 1
            else:
                r -= 1

    print(count)
    test -= 1
