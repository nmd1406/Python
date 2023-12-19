test = int(input())


def solve(num):
    sum = int(num[0])
    for i in range(1, len(num)):
        if abs(int(num[i]) - int(num[i - 1])) != 2:
            return "NO"
        sum += int(num[i])

    if sum % 10 == 0:
        return "YES"
    else:
        return "NO"


while test > 0:
    num = input()
    print(solve(num))
    test -= 1
