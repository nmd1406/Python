set1 = set([x.lower() for x in input().split()])
set2 = set([x.lower() for x in input().split()])

set3 = sorted(set1.union(set2))
for i in set3:
    print(i, end=" ")

print()
set3 = sorted(set1.intersection(set2))
for i in set3:
    print(i, end=" ")