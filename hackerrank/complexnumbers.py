from math import *
class Complex(object):
    def __init__(self, real, img):
        self.real=real
        self.img=img
    def __add__(self, other):
        return Complex(self.real+other.real,self.img+other.img)
    def __sub__(self, other):
        return Complex(self.real-other.real, self.img-other.img)
    def __mul__(self, other):
        return Complex(self.real*other.real-self.img*other.img,self.img*other.real+self.real*other.img)
    def mod(self):
        m=(self.real**2+self.img**2)**0.5
        return Complex(m,0)
    def __truediv__(self, other):
        cdiv=float(other.real*other.real+other.img*other.img)
        return Complex((self.real*other.real+self.img*other.img)/cdiv,(self.img*other.real-self.real*other.img)/cdiv)

    def __str__(self):
        if self.img == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.img >= 0:
                result = "0.00+%.2fi" % (self.img)
            else:
                result = "0.00-%.2fi" % (abs(self.img))
        elif self.img> 0:
            result = "%.2f+%.2fi" % (self.real, self.img)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.img))
        return result

c = map(float, input().strip().split())
d = map(float, input().strip().split())
x = Complex(*c)
y = Complex(*d)
#print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
print(x + y)
print(x-y)
print(x*y)
print(x/y)
print(x.mod())
print(y.mod())