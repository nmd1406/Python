string = input()

countUpper = 0

for char in string:
    if char.isupper():
        countUpper += 1

countLower = len(string) - countUpper

if countUpper > countLower:
    print(string.upper())
else:
    print(string.lower())
