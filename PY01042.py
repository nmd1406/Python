test = int(input())


def solve(inp):
    for ch in inp:
        if ch.isalpha():
            return "NO"
        if ch != '0' and ch != '1' and ch != '2':
            return "NO"

    return "YES"


while test > 0:
    inp = input()
    print(solve(inp))

    test -= 1
