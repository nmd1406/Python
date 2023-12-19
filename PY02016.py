test = int(input())
for i in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    Dict = {}
    for num in arr:
        if num not in Dict:
            Dict[num] = 1
        else:
            Dict[num] += 1

    maxVal = max(Dict.values())
    flag = False
    for itr in Dict:
        if Dict[itr] == maxVal and maxVal > n // 2:
            print(itr)
            flag = True

    if not flag:
        print("NO")