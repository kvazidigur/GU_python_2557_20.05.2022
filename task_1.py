# забиваем константы
SECOND_PER_DAY = 86400
SECOND_PER_HOUR = 3600
SECOND_PER_MINUTE = 60

# Запрашиваем продолжительность в секундах
duration = input('Введите продолжительность в секундах: ')
while not duration.isdigit():
    duration = input('Введено некорректное значение. Необходимо ввести целое, положительное число: ')
else:
    duration = int(duration)

# вычисляем количество дней
days_qty = duration // SECOND_PER_DAY
# вычитаем дни из общего оъема
duration -= days_qty * SECOND_PER_DAY

# вычисляем количество часов за вычетом дней
hours_qty = duration // SECOND_PER_HOUR
# вычитаем часы из общего оъема
duration -= hours_qty * SECOND_PER_HOUR

# вычисляем количество минут
minute_qty = duration // SECOND_PER_MINUTE
# вычитаем минуты  из общего оъема, оставшееся и есть секунды
duration -= minute_qty * SECOND_PER_MINUTE

time_str = '{} сек'.format(duration)
if minute_qty or hours_qty or days_qty > 0:
    time_str = '{} мин '.format(minute_qty) + time_str
if hours_qty or days_qty > 0:
    time_str = '{} час '.format(hours_qty) + time_str
if days_qty > 0:
    time_str = '{} дн '.format(days_qty) + time_str

print(time_str)
