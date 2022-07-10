from abc import ABC


class Warehouse:
    pass


class OfficeEquipment(ABC):
    def __init__(self, eq_type, name):
        self.eq_type = eq_type
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, model, print_speed):
        super().__init__('Printer', name)
        self.model = model
        self.print_speed = print_speed


class Xerox(OfficeEquipment):
    def __init__(self, name, model, copy_speed):
        super().__init__('Xerox', name)
        self.model = model
        self.copy_speed = copy_speed


class Scanner(OfficeEquipment):
    def __init__(self, name, model, scan_speed):
        super().__init__('Scanner', name)
        self.model = model
        self.scan_speed = scan_speed
