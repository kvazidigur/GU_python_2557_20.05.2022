from itertools import zip_longest


class Matrix:
    def __init__(self, llist: list):
        self.llist = llist

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.llist]))

    def __add__(self, other):
        for i in range(len(self.llist)):
            for j in range(len(other.llist[i])):
                self.llist[i][j] = self.llist[i][j] + other.llist[i][j]
        return self



l1 = [[31, 32], [33, 34], [8, 0]]
l2 = [[41, 42], [45, 46], [48, 49]]

m = Matrix(l1)
print(m)
print('######################')
m2 = Matrix(l2)
print(m + m2)
