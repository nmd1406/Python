import math

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

def check(num):
    length = len(num)
    if not isPrime(length):
        return "NO"
    
    count = 0
    for digit in num:
        if isPrime(int(digit)):
            count += 1

    if count > length - count:
        return "YES"
    
    return "NO"
    

test = int(input())
for i in range(test):
    num = input()
    print(check(num))