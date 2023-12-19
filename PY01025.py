s = input()

s = s[::-1]
res = ""
count = 0
for ch in s:
    if count == 3:
        res += ","
        count = 0
    res += ch
    count += 1

print(res[::-1])
