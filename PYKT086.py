temp = "0123456789ABCDEF"

def convert(num, b):
    res = ""
    while num > 0:
        digit = num % b
        res += temp[digit]
        num //= b

    return res[::-1]

file = open("DATA.in", "r")
test = int(file.readline())
for i in range(test):
    b = int(file.readline())
    num = int(file.readline(), 2)
    print(convert(num, b))
    