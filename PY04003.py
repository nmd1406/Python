import math

class PhanSo:
    def __init__(self, tuSo, mauSo):
        self.tuSo = int(tuSo)
        self.mauSo = int(mauSo)

    def rutGon(self):
        ucln = math.gcd(self.tuSo, self.mauSo)
        self.tuSo //= ucln
        self.mauSo //= ucln

    def __str__(self) -> str:
        return f"{self.tuSo}/{self.mauSo}"
    
arr = input().split()
phanSo = PhanSo(arr[0], arr[1])
phanSo.rutGon()
print(phanSo)