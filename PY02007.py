list = []
while len(list) != 10:
    list = list + [int(x) for x in input().split()]

set = set()
for num in list:
    set.add(num % 42)

print(len(set))