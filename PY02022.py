import math


def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

n = int(input())
numList = list(map(int, input().split()))
numDict = {}

for num in numList:
    if isPrime(num):
        if num not in numDict:
            numDict[num] = 1
        else:
            numDict[num] += 1

for i in numDict:
    print(i, numDict[i])