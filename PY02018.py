def solve(arr):
    res = arr[0]

    for num in arr:
        if res != num:
            return res
        res += 1
        
    return arr[-1] + 1

n = int(input())
arr = sorted(map(int, input().split()))
print(solve(arr))