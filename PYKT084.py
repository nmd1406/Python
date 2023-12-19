arr = []
n = int(input())
for i in range(n):
    string = input()

    if string == "":
        print(f"{arr[0]}: {len(arr) - 1}")
        arr.clear()
    else:
        arr.append(string)

print(f"{arr[0]}: {len(arr) - 1}")