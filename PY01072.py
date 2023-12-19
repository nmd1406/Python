from itertools import combinations


n, k = map(int, input().split())
arr = sorted(set(map(int, input().split())))

comp = combinations(arr, k)
print(type(comp))
for i in list(comp):
    print(''.join([str(x) + " " for x in i]))