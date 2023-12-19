test = int(input())

def maHoa(inp):
    count = 1
    for i in range(1, len(inp)):
        if inp[i] != inp[i - 1]:
            print(count, end="")
            print(inp[i - 1], end="")
            count = 1
        else:
            count += 1

    print(count, end="")
    print(inp[-1])


while test > 0:
    inp = input()

    maHoa(inp)
    test -= 1