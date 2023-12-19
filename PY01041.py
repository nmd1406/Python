def check(num):
    length = len(num)
    if length < 3:
        return False
    
    idx = 0
    while idx < length - 1 and num[idx] < num[idx + 1]:
        idx += 1
    
    if idx + 1 == length:
        return False
    else:
        while idx < length - 1 and num[idx] > num[idx + 1]:
            idx += 1

        if idx + 1 == length:
            return True
        else:
            return False 
    

test = int(input())
for i in range(test):
    num = input()
    if check(num):
        print("YES")
    else:
        print("NO")