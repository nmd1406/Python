test = int(input())

data = []
banGhi = {}

for i in range(test):
    string = input().split()
    data.append(string)
    if string[-1] not in banGhi.keys():
        banGhi[string[-1]] = 0

for i in data:
    if i[-2] == "IN":
        if i[1] == "Xe_con":
            if i[2] == "5":
                banGhi[i[-1]] += 10
            else:
                banGhi[i[-1]] += 15
        elif i[1] == "Xe_tai":
            banGhi[i[-1]] += 20
        else:
            if i[2] == "29":
                banGhi[i[-1]] += 50
            else:
                banGhi[i[-1]] += 70

for k, v in banGhi.items():
    print(f"{k}: {v * 1000}")