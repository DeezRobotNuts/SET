import math
class Fraction:
    def __init__(self, teller=0, noemer=1):
        self.a = teller
        self.b = noemer

    def __str__(self):
        return f'{str(self.a)}/{str(self.b)}'
    
    def __add__(self,other):
        asom = self.a * other.b + self.b * other.a
        bsom= self.b * other.b
        return Fraction(asom,bsom)
    def __radd__(self,other):
        asom = self.a * other.b + self.b * other.a
        bsom= self.b * other.b
        return Fraction(asom,bsom)
    def __sub__(self,other):
        asub = self.a * other.b - self.b * other.a
        bsub = self.b * other.b
        return Fraction(asub,bsub)
    def __rsub__(self,other):
        return -self + other
    def __mul__(self, other):
        amul = self.a * other.a
        bmul = self.b * other.b
        return Fraction(amul,bmul)
    def __rmul__(self,other):
        return self * other
    def __truediv__(self, other):
        adiv = self.a * other.b
        bdiv = self.b * other.a
        return Fraction(adiv,bdiv)
    def __rtruediv__(self, other):
        return other / self
    def __gt__(self, other):
        float(self) > float(other)
    def __ge__(self, other):
        float(self) >= float(other)
    def __lt__(self, other):
        float(self) < float(other)

    def __le__(self, other):
        float(self) <= float(other)

    def __eq__(self, other):
        float(self) == float(other)
    
    def __ne__(self, other):
        float(self) != float(other)

    def __neg__(self):
        aneg = -self.a
        b = self.b
        return Fraction(aneg,b)

    def __pos__(self):
        a = self.a
        b = self.b
        return Fraction(a,b)

    def __abs__(self):
        aabs = abs(self.a)
        babs = abs(self.b)
        return Fraction(aabs,babs)

    def __float__(self):
        numerator = self.a
        denomiantor = self.b
        return Fraction(numerator,denomiantor)

    def __int__(self):
        aint = int(self.a)
        bint = int(self.b)
        return  int(aint / bint)
