test = int(input())

while test > 0:
    n, x, m = map(float, input().split())

    count = 0
    while n <= m:
        n += (n * x / 100)
        count += 1

    print(count)
    test -= 1
