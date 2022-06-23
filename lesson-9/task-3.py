class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict = {'wage': 0, 'bonus': 1}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] * self._income['bonus']


a = Position('Паша', 'Иванов', 'Developer', {'wage': 1000, 'bonus': 1.2})
print(a.get_full_name())
print(a.get_total_income())
