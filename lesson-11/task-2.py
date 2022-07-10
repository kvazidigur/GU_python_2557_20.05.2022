class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))

    if b == 0:
        raise OwnError("Деление на ноль запрещено!!")
except OwnError as err:
    print(err)
except Exception:
    raise
else:
    print(a / b)
