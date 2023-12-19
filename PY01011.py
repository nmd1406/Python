test = int(input())


def check1(n):
    if len(n) % 2 == 1:
        return False
    for num in n:
        if int(num) % 2 == 1:
            return False
    return True


def check2(n):
    return (int(n) == int(n[::-1])) and int(n) > 10


while test > 0:
    n = int(input())
    for i in range(1, n):
        if check1(str(i)) and check2(str(i)):
            print(i, end=" ")
    print()
    test -= 1

# 22 44 66 88 1001 1221 2002 2222 2442
