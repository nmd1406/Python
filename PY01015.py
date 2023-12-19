test = int(input())

def solve(num):
    for i in range(0, len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            return "NO"
        
    return "YES"


while test > 0:
    num = input()
    print(solve(num))

    test -= 1
