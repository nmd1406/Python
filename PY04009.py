class SoPhuc:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def add(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return SoPhuc(a, b)
    
    def multiply(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a 
        return SoPhuc(a, b)
    
    def __str__(self) -> str:
        if self.b > 0:
            return f"{self.a} + {self.b}i"
        return f"{self.a} - {self.b}i"
    
test = int(input())
for i in range(test):
    inp = list(map(int, input().split()))
    idx = 0
    imgNum1 = SoPhuc(inp[idx], inp[idx + 1])
    imgNum2 = SoPhuc(inp[idx + 2], inp[idx + 3])
    imgNum3 = imgNum1.add(imgNum2)

    print(f"{imgNum3.multiply(imgNum1)}, {imgNum3.multiply(imgNum3)}")