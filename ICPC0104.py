test = int(input())

while test > 0:
    str = input()
    str += 'a'
    res = 10 ** 19
    num = 0

    for i in range(0, len(str) - 1):
        if str[i].isdigit():
            num = num * 10 + int(str[i])
            if str[i + 1].isalpha():
                res = min(num, res)
                num = 0

    print(res)
    test -= 1
