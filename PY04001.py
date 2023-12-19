from decimal import Decimal, getcontext 
import math

# getcontext().prec = 45

class Point:
    def __init__(self, x, y):
        self.x = Decimal(x)
        self.y = Decimal(y)

    def distance(self, p):
        temp = (p.x - self.x) ** 2 + (p.y - self.y) ** 2
        res = temp.sqrt()
        return "{:.4f}".format(res)
        

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1