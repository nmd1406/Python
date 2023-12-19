def check(string):
    revStr = string[::-1]
    for i in range(1, len(string)):
        if abs(ord(string[i]) - ord(string[i - 1])) != abs(ord(revStr[i]) - ord(revStr[i - 1])):
            return "NO"
        
    return "YES"

test = int(input())

for i in range(test):
    string = input()
    print(check(string))