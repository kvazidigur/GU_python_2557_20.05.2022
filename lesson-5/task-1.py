def gen_number(last_num):
    """Генератор нечётных чисел от 1 до last_num (включительно)"""
    for num in range(1, last_num + 1, 2):
        yield num


nums = gen_number(15)
