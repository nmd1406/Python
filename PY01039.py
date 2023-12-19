test = int(input())


def soDep(num):
    for i in range(len(num) - 2):
        if num[i] != num[i + 2]:
            return False

    return True


while test > 0:
    num = input()
    if soDep(num):
        print("YES")
    else:
        print("NO")

    test -= 1
