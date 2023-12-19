class Rectangle:
    def __init__(self, a, b, color) -> None:
        self.a = a
        self.b = b
        self.mau = color

    def perimeter(self):
        return (self.a + self.b) * 2
    
    def area(self):
        return self.a * self.b
    
    def color(self):
        return self.mau.title()

    def __str__(self) -> str:
        if self.a <= 0 or self.b <= 0:
            return "INVALID"
        return "{} {} {}".format(self.perimeter(), self.area(), self.color())
    
arr = input().split() 
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
print(r)