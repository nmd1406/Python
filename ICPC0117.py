n = int(input())

s = set()

while n > 0:
    string = input()
    s.add(string)
    n -= 1

print(len(s))
