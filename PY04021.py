class User:
    def __init__(self, id, ten, gioVao, gioRa) -> None:
        self.id = id
        self.ten = ten
        self.thoiGian = self.calcThoiGian(gioVao, gioRa)

    def calcThoiGian(self, gioVao, gioRa):
        a = list(map(int, gioVao.split(":")))
        b = list(map(int, gioRa.split(":")))
        return (b[0] - a[0]) * 60 + (b[1] - a[1])
    
    def __str__(self) -> str:
        return "{} {} {} gio {} phut".format(self.id, self.ten, self.thoiGian // 60, self.thoiGian % 60)
    

test = int(input())
arr = []
for i in range(test):
    arr.append(User(input(), input(), input(), input()))

arr.sort(key=lambda x: -x.thoiGian)
for user in arr:
    print(user)