def backTrack(string, length, countA, countB, countC):
    if len(string) == length:
        if countA > 0 and countA <= countB and countB <= countC:
            print(string)
        return

    backTrack(string + "A", length, countA + 1, countB, countC)
    backTrack(string + "B", length, countA, countB + 1, countC)
    backTrack(string + "C", length, countA, countB, countC + 1)


n = int(input())
for i in range(3, n + 1):
    backTrack("", i, 0, 0, 0)
