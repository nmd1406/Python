import math


def check(num):
    length = len(num)
    flag = True
    for i in range(length):
        if i % 2 == 0:
            if int(num[i]) % 2 != 0:
                flag = False
                break
        else:
            if int(num[i]) % 2 == 0:
                flag = False
                break

    if flag:
        sum = 0
        for i in num:
            sum += int(i)
        if isPrime(sum):
            return "YES"
        else:
            return "NO"
    
    return "NO"
        
def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
        
    return True

test = int(input())
for i in range(test):
    num = input()
    print(check(num))