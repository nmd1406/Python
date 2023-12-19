class LuongMua:
    def __init__(self, id, ten) -> None:
        self.id = "T{:02d}".format(id)
        self.ten = ten
        self.thoiGian = 0
        self.luongMua = 0

    def add(self, batDau, ketThuc, luongMua):
        a = list(map(int, batDau.split(":")))
        b = list(map(int, ketThuc.split(":")))
        self.thoiGian += (b[0] - a[0]) * 60 + (b[1] - a[1])
        self.luongMua += luongMua

    def luongMuaTrungBinh(self):
        return self.luongMua / (self.thoiGian / 60)

    def __str__(self) -> str:
        return "{} {} {:.2f}".format(self.id, self.ten, self.luongMuaTrungBinh())

test = int(input())
Dict = {}
for i in range(test):
    ten = input()
    batDau = input()
    ketThuc = input()
    luongMua = int(input())

    if ten not in Dict:
        Dict[ten] = LuongMua(i + 1, ten)
        Dict[ten].add(batDau, ketThuc, luongMua)
    else:
        Dict[ten].add(batDau, ketThuc, luongMua)

for ele in Dict:
    print(Dict[ele])