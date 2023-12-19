def check(num):
    length = len(num)
    if length % 2 == 0:
        return "NO"
    
    if num[0] == num[1]:
        return "NO"
    
    for i in range(0, length - 2, 2):
        if num[i] != num[i + 2]:
            return "NO"
        
    return "YES"

test = int(input())
for i in range(test):
    num = input()
    print(check(num))