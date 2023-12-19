import math


def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

test = int(input())
for itr in range(test):
    num = input()
    newNum = num[-4:]
    if isPrime(int(newNum)):
        print("YES")
    else:
        print("NO")