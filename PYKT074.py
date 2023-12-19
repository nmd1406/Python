from operator import le
from token import tok_name


test = int(input())
for i in range(test):
    arr = list(map(str, input().split()))
    length = 0
    for token in arr:
        if len(token) + length <= 100:
            print(token, end=" ")
            length += len(token) + 1
        else:
            break
    print()