test = int(input())
for i in range(test):
    num = input()
    tong = 0
    tich = 1
    flag = False

    for i in range(len(num)):
        if i % 2 == 0:
            if int(num[i]) != 0:
                tich *= int(num[i])
                flag = True
        else:
            tong += int(num[i])

    if flag:
        print(tich, tong)
    else:
        print(0, tong)