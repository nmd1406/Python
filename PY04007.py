
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

test = int(input())
for idx in range(test):
    n, m = [int(x) for x in input().split()]
    mtx = [[0] * m] * n
    for i in range(n):
        mtx[i] = [int(x) for x in input().split()]
    matrix = Matrix(n, m, mtx)
    revMtx = [list(x) for x in zip(*mtx)]
    revMatrix = Matrix(m, n, revMtx)
    res = matrix.multiply(revMatrix)
    for i in res:
        for j in i:
            print(j, end=" ")
        print()

