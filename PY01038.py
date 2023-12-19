test = int(input())
while test > 0:
    num = int(input())
    count = 0
    sum = num
    while count <= 1000 and sum % 7 != 0:
        revNum = int(str(num)[::-1])
        sum += revNum
        num = sum
        count += 1

    if sum % 7 != 0:
        print(-1)
    else:
        print(sum)

    test -= 1
