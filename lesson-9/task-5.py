class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
