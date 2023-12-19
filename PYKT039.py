test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    flag = False
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            flag = True
            break

    if not flag:
        print("YES")