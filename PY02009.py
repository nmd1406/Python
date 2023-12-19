from operator import itemgetter


test = int(input())
for i in range(test):
    n = int(input())
    dct = dict()
    for j in range(n):
        num = int(input())
        if num in dct:
            dct[num] += 1
        else:
            dct[num] = 1

    dct = dict(sorted(dct.items(), key=lambda x: (-x[1], x[0])))
    print(next(iter(dct)))
