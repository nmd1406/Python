test = int(input())
for i in range(test):
    n = int(input())
    arr = [0]
    arr += (list(map(int, input().split())))
    stack = [0]
    for i in range(1, n + 1):
        while len(stack) > 1 and arr[stack[-1]] <= arr[i]:
            stack.pop()

        print(i - stack[-1], end=" ")
        stack.append(i)

    print()