test = int(input())


while test > 0:
    inp = input()
    sum = 0
    for ch in inp:
        sum += int(ch)

    if sum == int(str(sum)[::-1]) and len(str(sum)) > 1:
        print("YES")
    else:
        print("NO")

    test -= 1
