import cmath

class Complex:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"({self.real}{'+' if self.imag >= 0 else '-'}{abs(self.imag)}j)"

    def __add__(self, num):
        return Complex(self.real + num.real, self.imag + num.imag)

    def __radd__(self, num):
        num = Complex(num)
        return self.__add__(num)

    def __sub__(self, num):
        return Complex(self.real - num.real, self.imag - num.imag)

    def __rsub__(self, num):
        return self.__sub__(num)

    def __mul__(self, num):
        return Complex(self.real * num.real - self.imag * num.imag,
                             self.imag * num.real + self.real * num.real)

    def __truediv__(self, num):
        div = (num.real ** 2 + num.imag ** 2)
        return Complex((self.real * num.real) - (self.imag * num.imag) / div,
                             (self.imag * num.real) + (self.real * num.imag) / div)

    def __abs__(self):
        return cmath.sqrt(self.real ** 2 - (self.imag ** 2))

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    @classmethod
    def from_string(cls, string):
        new_str = None
        sign = None
        signs = ['+', '-']
        succeed = False
        all_good = False
        for idx, char in enumerate(string):
            if char in signs:
                if idx != 0:
                    sign = string[idx]
                    new_str = string.replace(sign, " ")
                    all_good = True
                    succeed = True
                    break
        if not succeed:
            for idx, char in enumerate(string):
                if char == 'j' or char == 'i':
                    real = 0
                    imag = float(string[:-1])
                    succeed = True

        if not succeed:
            real = float(string)
            imag = 0

        if all_good:
            real, imag = new_str.split()
            imag = imag[:-1]
            real, imag = float(real), float(imag)
            imag = imag if sign == '+' else -imag
        return cls(real, imag)


if __name__ == '__main__':
    print("Number 1:")
    number1 = Complex(2, 2)
    print(number1)
    print("Number 2:")
    number2 = Complex(4, 4)
    print(number2)
    print("Adding numbers: ")
    print(number1 + number2)
    print("Subtracting numbers: ")
    print(number1 - number2)
    print("Multiplying numbers: ")
    print(number1 * number2)
    print("Dividing numbers: ")
    print(number1 / number2)
    print("Absolute value of number 1: ")
    print(-number1)
    print("Negation of: ")
    print(-number1)
    number3 = 5
    print("Adding int to number1: ")
    print(number1 + number3)
