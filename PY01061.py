import math


def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

test = int(input())
for i in range(test):
    num = input()
    first = int(num[:3])
    last = int(num[-3:])
    if isPrime(first) and isPrime(last):
        print("YES")
    else:
        print("NO")