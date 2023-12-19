class NhanVien:
    def __init__(self, id, ten, lyThuyet, thucHanh) -> None:
        self.id = "TS0" + str(id)
        self.ten = ten
        self.lyThuyet = lyThuyet
        while self.lyThuyet > 10:
            self.lyThuyet /= 10
        self.thucHanh = thucHanh
        while self.thucHanh > 10:
            self.thucHanh /= 10
        
        self.trungBinh = (self.lyThuyet + self.thucHanh) / 2

    def xepLoai(self):
        if self.trungBinh < 5:
            return "TRUOT"
        elif self.trungBinh < 8:
            return "CAN NHAC"
        elif self.trungBinh < 9.5:
            return "DAT"
        else:
            return "XUAT SAC"
        
    def __str__(self) -> str:
        return "{} {} {:.2f} {}".format(self.id, self.ten, self.trungBinh, self.xepLoai())
    
test = int(input())
arr = []
for i in range(test):
    arr.append(NhanVien(i + 1, input(), float(input()), float(input())))

arr.sort(key=lambda x: -x.trungBinh)
for ele in arr:
    print(ele)