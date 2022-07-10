from abc import ABC
import uuid


class Warehouse:
    def __init__(self, name):
        self.name = name
        self._dict = {}

    def add_equipment(self, equipment, inventory_number):
        equipment.inventory_number = inventory_number
        if not equipment.inventory_number:
            equipment.inventory_number = uuid.uuid1()

        li = self._dict.get(equipment.inventory_number, [])
        li.append(equipment)
        self._dict[equipment.inventory_number] = li

    def transfer(self, inventory_number, department):
        self._dict[inventory_number].department = department

    def __str__(self):
        return f'{self.name}: {len(self._dict)} equipment'


class OfficeEquipment(ABC):
    eq_type = ''

    def __init__(self, name):
        self.name = name
        self.department = None
        self.inventory_number = None


class Printer(OfficeEquipment):
    eq_type = 'Printer'

    def __init__(self, name, model, print_speed):
        super().__init__(name)
        self.model = model
        self.print_speed = print_speed


class Xerox(OfficeEquipment):
    eq_type = 'Xerox'

    def __init__(self, name, model, copy_speed):
        super().__init__(name)
        self.model = model
        self.copy_speed = copy_speed


class Scanner(OfficeEquipment):
    eq_type = 'Scanner'

    def __init__(self, name, model, scan_speed):
        super().__init__(name)
        self.model = model
        self.scan_speed = scan_speed


eq1 = Printer('hp', 'ew2101', 5)
eq2 = Scanner('Canon', 'rr5506', 1)
eq3 = Xerox('Xerox', 'hghg888', 2)
eq4 = Printer('azaza', 'hh22', 5)

wh = Warehouse('склад1')
wh.add_equipment(eq1, '123')
wh.add_equipment(eq2, '1234')
wh.add_equipment(eq3, '12345')
wh.add_equipment(eq4, '123456')

print(wh)
