test = int(input())

while test > 0:
    s = input()
    num = int(s[-2::])
    if num == 86:
        print("YES")
    else:
        print("NO")

    test -= 1