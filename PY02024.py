def digitProduct(num):
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10

    return product

test = int(input())
for i in range(test):
    n = int(input())
    numList = list(map(int, input().split()))
    numList.sort(key=lambda x: (digitProduct(x), x))
    for num in numList:
        print(num, end=" ")

    print()