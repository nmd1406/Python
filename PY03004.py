import re

Dict = {}
test = int(input())
for i in range(test):
    tokens = re.findall("[a-zA-Z0-9]+", input())
    for token in tokens:
        temp = token.lower()
        if temp in Dict:
            Dict[temp] += 1
        else:
            Dict[temp] = 1

res = sorted(Dict.items(), key=lambda x: (-x[-1], x[0]))
for item in res:
    print(item[0], item[1])