import math  #gcd máximo común divisor, lcm mínimo común múltiplo

class Fraccion:
    __numerador: int
    __denominador: int

    def __init__(self, fraccion):
        variable = fraccion.split('/')
        self.__numerador = int(variable[0])
        self.__denominador = int(variable[1])
        print(self.__numerador)
        print(self.__denominador)

    def getNum (self):
        return self.__numerador

    def getDen (self):
        return self.__denominador
    
    def __add__ (self, otro):
        a = self.getNum()
        b = self.getDen()
        if isinstance(otro, Fraccion):
            c = otro.getNum()
            d = otro.getDen()
        else:
            c = otro
            d = 1
        x = math.lcm( b, d ) #minimo comun multiplo
        z = int((x/b)*a + (x/d)*c )#suma de fraciones
        return [z, x]

    def __radd__ (self, otro):
        return self.__add__(otro)

    def __sub__ (self, otro):
        a = self.getNum()
        b = self.getDen()
        if isinstance(otro, Fraccion):
            c = otro.getNum()
            d = otro.getDen()
        else:
            c = otro
            d = 1
        x = math.lcm( b, d ) #minimo comun multiplo
        z = int((x/b)*a - (x/d)*c) #resta de fraciones
        return [z, x]
    
    def __rsub__ (self, otro):
        return self.__rsub__(otro)

    def __mul__ (self, otro):
        a = self.getNum()
        b = self.getDen()
        if isinstance(otro, Fraccion):
            c = otro.getNum()
            d = otro.getDen()
        else:
            c = otro
            d = 1
        x = int(a * d)
        z = int(b * c)
        return [x, z]
    
    def __rmul__ (self, otro):
        return self.__mul__(otro)

    def __floordiv__ (self, otro):
        a = self.getNum()
        b = self.getDen()
        if isinstance(otro, Fraccion):
            c = otro.getNum()
            d = otro.getDen()
        else:
            c = otro
            d = 1
        x = int(a * c)
        z = int(b * d)
        return [x, z]

    def __truediv__ (self, otro):
        a = self.getNum()
        b = self.getDen()
        if isinstance(otro, Fraccion):
            c = otro.getNum()
            d = otro.getDen()
        else:
            c = otro
            d = 1
        x = int(a * c)
        z = int(b * d)
        return [x, z]

    def __rdiv__ (self, otro):
        return self.__div__(otro)

    def simplifica(self):
        mcd = math.gcd(self.__numerador, self.__denominador)
        num = int(self.__numerador / mcd)
        den = int(self.__denominador / mcd)
        return [num, den]
 
    def __repr__(self):
        if self.__numerador == self.__denominador:
            return('1')
        elif self.__denominador == 1:
            return('{}'.format(self.__numerador))
        elif self.__numerador > 0 and self.den < 0:
            return('{}/{}'.format(-self.__numerador, -self.__denominador))
        else:
            return('{}/{}'.format(self.__numerador, self.__denominador))
        
# if __name__ == '__main__':
#     f1 = Fraccion( "1/2" )
#     f2 = Fraccion( "1/2" )
#     #f3 = f1 + f2
#     f3 = f1 * f2
#     f3 = Fraccion( "{}/{}".format(f3[0], f3[1]) )
#     print(f3.simplifica())
#     print("representacion", f3)
#     #print("resta ",f3[0],"/",f3[1])