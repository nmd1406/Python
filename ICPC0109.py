test = int(input())

while test > 0:
    n = int(input())

    arr = map(int, input().split())

    # fMin = 10**8
    # sMin = 10**8
    # tMin = 10**8

    # for num in arr:
    #     if num < fMin:
    #         tMin = sMin
    #         sMin = fMin
    #         fMin = num
    #     elif (num < sMin):
    #         tMin = sMin
    #         sMin = num
    #     elif (num < tMin):
    #         tMin = num

    arr.sort()

    print(arr[0] + arr[1] + arr[2])
    test -= 1
