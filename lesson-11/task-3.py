class NotNumb(Exception):
    def __init__(self, txt):
        self.txt = txt


print('вам необходимо ввести числа, для прекращения вводе введите stop')
li = []
while True:
    el = input("Введите число: ")
    if el == 'stop':
        break

    try:
        if not el.isdigit():
            raise NotNumb(f'{el} не является числом.')
        li.append(int(el))

    except NotNumb as e:
        print(e)

print(li)
