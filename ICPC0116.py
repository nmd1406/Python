test = int(input())

while test > 0:
    num = input()
    if num[0] == num[-1]:
        print("YES")
    else:
        print("NO")
    
    test -= 1