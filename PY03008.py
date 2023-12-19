Dict = {}
def add(num):
    if num in Dict:
        Dict[num] += 1
    else:
        Dict[num] = 1


test = int(input())
for i in range(test - 1):
    u, v = map(int, input().split())
    add(u)
    add(v)

flag = False
for item in Dict:
    if Dict[item] == test - 1:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")