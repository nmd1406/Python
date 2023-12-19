test = int(input())

while test > 0:
    num = input()
    res = 1
    for digit in num:
        if digit != '0':
            res *= int(digit)

    print(res)
    test -= 1
