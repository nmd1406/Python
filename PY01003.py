test = int(input())

while test > 0:
    string = list(input())
    if string == "5":
        print("".join(string))
    elif string[-1] == "5":
        string[0] = str(int(string[0]) + 1)
        for i in range(1, len(string)):
            string[i] = "0"
    else:
        for i in range(1, len(string)):
            string[i] = "0"
    
    print("".join(string))
    test -= 1