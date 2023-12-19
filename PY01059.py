test = int(input())
for i in range(test):
    num = input()
    tong = 0
    tich = 1
    flag = False

    for i in range(len(num)):
        if i % 2 == 0:
            tong += int(num[i])
        else:
            if int(num[i]) != 0:
                tich *= int(num[i])
                flag = True

    if flag:
        print(tong, tich)
    else:
        print(tong, 0)