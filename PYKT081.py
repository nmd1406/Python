def check(tokens):
    if len(tokens) != 4:
        return "NO"
    
    for token in tokens:
        try:
            if int(token) < 0 or int(token) > 255:
                return "NO"
        except:
            return "NO"
    return "YES"


test = int(input())
for i in range(test):
    tokens = [x for x in input().split(".")]
    print(check(tokens))