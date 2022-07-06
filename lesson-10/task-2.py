from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def fabric_consumption(self):
        """Расчет расхода ткани"""
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def fabric_consumption(self):
        """Расчет расхода ткани"""
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def fabric_consumption(self):
        """Расчет расхода ткани"""
        return 2 * self.h + 0.3


coat = Coat('Пальто #1', 5)
print(coat.fabric_consumption)
coat.v = 15
print(coat.fabric_consumption)

suit = Suit('Костюм #1', 200)
print(suit.fabric_consumption)
suit.h = 210
print(suit.fabric_consumption)
