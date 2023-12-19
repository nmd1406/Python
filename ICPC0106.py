import math

test = int(input())

char = ['A', 'B', 'C', 'D', 'E', 'F']

while test > 0:
    base = int(input())
    str = input()

    if base == 2:
        print(str)
        test -= 1
        continue

    base = int(math.log(base, 2))

    while (len(str) % base) != 0:
        str = "0" + str

    i = 0
    while i < len(str):
        num = 0
        for j in range(i, i + base):
            num += int(str[j]) * (2 ** (base - j + i - 1))

        if num >= 10:
            print(char[num - 10], end='')
        else:
            print(num, end='')

        i += base

    print()
    test -= 1
