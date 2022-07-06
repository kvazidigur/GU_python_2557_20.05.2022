class OrganicCell:
    def __init__(self, cell_qty):
        self.cell_qty = cell_qty

    def __str__(self):
        return str(self.cell_qty)

    def __add__(self, other):
        return OrganicCell(self.cell_qty + other.cell_qty)

    def __sub__(self, other):
        if self.cell_qty > other.cell_qty:
            return OrganicCell(self.cell_qty - other.cell_qty)

        print('Операция вычиания невозможна')

    def __mul__(self, other):
        return OrganicCell(self.cell_qty * other.cell_qty)

    def __truediv__(self, other):
        return OrganicCell(self.cell_qty // other.cell_qty)

    def __floordiv__(self, other):
        return OrganicCell(self.cell_qty // other.cell_qty)

    def make_order(self, cell_per_line):
        row_qty, remains = self.cell_qty // cell_per_line, self.cell_qty % cell_per_line
        return '\n'.join(['*' * cell_per_line] * row_qty + (['*' * remains] if remains else []))


c1 = OrganicCell(15)
c2 = OrganicCell(30)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1 // c2)

print(c1.make_order(2))
