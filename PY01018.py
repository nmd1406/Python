k = 0

p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    inp = input()
    if inp[0] == "0":
        break
    k, s = inp.split()
    k = int(k)

    res = ""
    for i in range(len(s)):
        res += p[(p.find(s[i]) + k) % 28]

    print(res[::-1])
