test = int(input())

even = ['0', '2', '4', '6', '8']

while test > 0:
    n = int(input())
    res = []
    queue = ['00', '22', '44', '66', '88']

    while len(queue) > 0:
        num = queue.pop(0)
        if len(num) < 6:
            for digit in even:
                queue.append(digit + num + digit)

        if not num.startswith('0'):
            res.append(int(num))

    res.sort()
    for num in res:
        if num < n:
            print(num, end=" ")
        else:
            break

    print()

    test -= 1

    