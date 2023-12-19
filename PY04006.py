from decimal import Decimal
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        res = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return res
    
class Triangle:
    def __init__(self, p1, p2, p3) -> None:
        self.ab = p1.distance(p2)
        self.bc = p2.distance(p3)
        self.ac = p3.distance(p1)

    def dienTich(self):
        if (self.ab + self.bc <= self.ac) or (self.ab + self.ac <= self.bc) or (self.bc + self.ac <= self.ab):
            print("INVALID")
        else:
            a = self.ab
            b = self.bc
            c = self.ac
            s = math.sqrt((self.ab + self.bc + self.ac) * (self.ab + self.bc - self.ac) * (self.ab - self.bc + self.ac) * (-self.ab + self.bc + self.ac)) / 4
            print("{:.2f}".format(s))
    

test = int(input())
arr = []    
for i in range(test):
    arr += [float(x) for x in input().split()]
idx = 0
while test > 0:
    triangle = Triangle(Point(arr[idx], arr[idx + 1]), Point(arr[idx + 2], arr[idx + 3]), Point(arr[idx + 4], arr[idx + 5]))
    triangle.dienTich()
    idx += 6
    test -= 1