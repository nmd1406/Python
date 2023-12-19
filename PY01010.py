test = int(input())

while test > 0:
    num = input()

    if num[:2] == num[-2:]:
        print("YES")
    else:
        print("NO")

    test -= 1
