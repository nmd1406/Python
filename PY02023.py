def digitSum(num):
    digitList = list(map(int, str(num)))
    return sum(digitList)

test = int(input())
for i in range(test):
    n = int(input())
    numList = list(map(int, input().split()))
    numList.sort(key=lambda x: (digitSum(x), x))
    for num in numList:
        print(num, end=" ")

    print()