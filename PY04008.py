
import sys


class Matrix:
    def __init__(self, n, m, mtx) -> None:
        self.n = n
        self.m = m
        self.mtx = mtx

    def multiply(self, other):
        ans = [[0] * n for _ in range(n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    ans[i][j] += self.mtx[i][k] * other.mtx[k][j]

        return ans

arr = []
for line in sys.stdin: arr += map(int, line.split())
idx = 1
for i in range(arr[0]):
    n, m = arr[idx], arr[idx + 1]
    idx += 2
    mtx = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            mtx[i][j] = arr[idx]
            idx += 1
    matrix = Matrix(n, m, mtx)
    revMtx = [list(x) for x in zip(*mtx)]
    revMatrix = Matrix(m, n, revMtx)
    res = matrix.multiply(revMatrix)
    for i in res:
        for j in i:
            print(j, end=" ")
        print()

