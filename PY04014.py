import functools


class HocSinh:
    def __init__(self, id, ten, diem) -> None:
        self.id = "HS{:02d}".format(id)
        self.ten = ten
        self.diem = diem

    def diemTrungBinh(self):
        tong = 0
        for i in range(10):
            if i < 2:
                tong += self.diem[i] * 2
            else:
                tong += self.diem[i]

        tong /= 12
        return round((tong * 100 + 1) / 100, 1)
    
    def xepLoai(self):
        avg = self.diemTrungBinh()
        if avg < 5:
            return "YEU"
        elif avg < 7:
            return "TB"
        elif avg < 8:
            return "KHA"
        elif avg < 9:
            return "GIOI"
        else:
            return "XUAT SAC"
        
    def __str__(self) -> str:
        return "{} {} {:.1f} {}".format(self.id, self.ten, self.diemTrungBinh(), self.xepLoai())
    
def cmp(a, b):
    if a.diemTrungBinh() == b.diemTrungBinh():
        return 1 if a.id > b.id else -1
    
    return 1 if a.diemTrungBinh() < b.diemTrungBinh() else -1


test = int(input())
arr = []
for i in range(test):
    ten = input()
    diem = list(map(float, input().split()))
    arr.append(HocSinh(i + 1, ten, diem))

arr.sort(key=functools.cmp_to_key(cmp))
for hocSinh in arr:
    print(hocSinh)