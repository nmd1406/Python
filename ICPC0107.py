test = int(input())


def convert(p, q, text1, text2):
    num1 = text1.replace(p, q)
    num2 = text2.replace(p, q)

    return int(num1) + int(num2)


while test > 0:
    p, q = input().split()
    s = input().split()

    if len(s) > 1:           # input tren 1 dong
        x1 = s[0]
        x2 = s[1]
    else:                   # input tren 2 dong
        x1 = s[0]
        x2 = input()

    sum1 = convert(p, q, x1, x2)
    sum2 = convert(q, p, x1, x2)

    print(f"{min(sum1, sum2)} {max(sum1, sum2)}")

    test -= 1
