class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a*other.b} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, 1)
z_2 = ComplexNumber(1, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
