test = int(input())


def solve(num):
    for char in num:
        if char != '4' and char != '7':
            return False

    return True


while test > 0:
    num = input()

    if solve(num):
        print("YES")
    else:
        print("NO")

    test -= 1
