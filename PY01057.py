import math

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

def check(num):
    for i in range(len(num)):
        if isPrime(i) and num[i] not in prime:
            return "NO"
        if not isPrime(i) and num[i] in prime:
            return "NO"
            
    return "YES"

prime = ['2', '3', '5', '7']
test = int(input())
for i in range(test):
    num = input()
    print(check(num))
