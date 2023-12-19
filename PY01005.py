num = input()

countFour = 0
countSeven = 0

for char in num:
    if char == "4":
        countFour += 1
    elif char == "7":
        countSeven += 1

if (countFour + countSeven) == 4 or (countSeven + countFour) == 7:
    print("YES")
else:
    print("NO")