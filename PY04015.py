class HoaDon:
    def __init__(self, id, ten, chiSoCu, chiSoMoi) -> None:
        self.id = "KH{:02d}".format(id)
        self.ten = ten
        self.chiSo = chiSoMoi - chiSoCu

    def tongTien(self):
        tien = 0
        phuPhi = 0
        if self.chiSo > 100:
            tien = 50 * 100 + 50 * 150 + (self.chiSo - 100) * 200
            phuPhi = tien * 5 / 100
        elif self.chiSo > 50:
            tien = 50 * 100 + (self.chiSo - 50) * 150
            phuPhi = tien * 3 / 100
        else:
            tien = self.chiSo * 100
            phuPhi = tien * 2 / 100

        return round(tien + phuPhi)

    def __str__(self) -> str:
        return f"{self.id} {self.ten} {self.tongTien()}"
    

test = int(input())
arr = []
for i in range(test):
    ten, chiSoCu, chiSoMoi = input(), int(input()), int(input())
    arr.append(HoaDon(i + 1, ten, chiSoCu, chiSoMoi))

arr = sorted(arr, key=lambda x: (-x.tongTien()))
for itr in arr:
    print(itr)


# 3 
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612