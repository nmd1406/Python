fibo = [0] * 100

def solve(n, k):
    x = pow(2, n - 1)
    if k == x:
        return n
    
    if k < x:
        return solve(n - 1, k)
    
    return solve(n - 1, k - x)

test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, 94):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    print(chr(ord("A") + solve(n, k) - 1))
