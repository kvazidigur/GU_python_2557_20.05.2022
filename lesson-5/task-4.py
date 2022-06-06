def get_next_less_than_prev(num_list):
    """Выводит элементы списка, значения которых больше предыдущего"""
    return [num_list[idx] for idx in range(0, len(num_list)) if 0 < idx and num_list[idx] > num_list[idx-1]]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(src)
print(get_next_less_than_prev(src))
