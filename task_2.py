# составляем список, состоящий из кубов нечётных чисел от 1 до 1000
uneven_numbers_cube = [(num ** 3) for num in range(1, 1001, 2)]

# в первом проходе считаем для обычного случая
# во втором проходе считаем для случая +17 к каждому элементу списка
for i in [0, 17]:
    # считаем сумму чисел, для чисел, в которых сумма цифр делится нацело на 7
    numbers_sum = 0
    for num in uneven_numbers_cube:
        # вычисляем сумму чисел из которых состоит число
        text_number = str(num + i)
        part_num_sum = 0
        for part_num in text_number:
            part_num_sum += int(part_num)

        # если сумма цифр числа делится на 7 без остатка, то добавляем число к общей сумме
        if part_num_sum % 7 == 0:
            numbers_sum += num + i
    print(numbers_sum)
