from itertools import permutations


perm = permutations(input())

for i in list(perm):
    print(''.join(i))