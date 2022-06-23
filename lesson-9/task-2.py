class Road:
    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def calc_weight(self, basis_weight, thickness):
        return self._length * self._width * basis_weight * thickness


a = Road(20, 5000)
print(a.calc_weight(25, 5))
