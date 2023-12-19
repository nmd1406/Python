test = int(input())

def maHoa(inp):
    arr = [inp[i:i + 2] for i in range(0, len(inp), 2)]

    res = ""
    for j in range(len(arr)):
        count = int(arr[j][1])
        while count > 0:
            res += arr[j][0]
            count -= 1

    return res            

while test > 0:
    inp = input()
    print(maHoa(inp))
    test -= 1
    