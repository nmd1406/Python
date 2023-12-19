from itertools import combinations


n, k = map(int, input().split())
wordSet = {x for x in input().split()}
wordList = sorted(list(wordSet))

res = combinations(wordList, k)
for itr in res:
    for j in itr:
        print(j, end=" ")
    print()