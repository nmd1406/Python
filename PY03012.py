

class SinhVien:
    def __init__(self, ten, ac, submit) -> None:
        self.ten = ten
        self.ac = ac
        self.submit = submit

    def __str__(self) -> str:
        return "{} {} {}".format(self.ten, self.ac, self.submit)

List = []
test = int(input())
for i in range(test):
    ten = input()
    ac, submit = map(int, input().split())
    List.append(SinhVien(ten, ac, submit))

List = sorted(List, key=lambda x: (-x.ac, x.submit, x.ten))
for sinhVien in List:
    print(sinhVien)