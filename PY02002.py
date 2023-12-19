test = int(input())

fibo = [0] * 94
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1

for i in range(3, 94):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

while test > 0:
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(fibo[i], end=" ")
    print()

    test -= 1
