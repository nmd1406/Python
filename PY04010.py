class ThiSinh:
    def __init__(self, ten, dob, diem1, diem2, diem3) -> None:
        self.ten = ten
        self.dob = dob
        self.diem1 = diem1
        self.diem3 = diem3
        self.diem2 = diem2

    def __str__(self) -> str:
        return "{} {} {:.1f}".format(self.ten, self.dob, self.diem1 + self.diem2 + self.diem3)
    
thiSinh = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
print(thiSinh)