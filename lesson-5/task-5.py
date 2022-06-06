def non_repeating(num_list):
    """Возвращает не повторяющиеся элементы списка"""
    nr_list = [num for num in num_list if num_list.count(num) == 1]
    return nr_list


def non_repeating_opti(num_list):
    """Возвращает не повторяющиеся элементы списка"""
    tmp_set = set()
    uniq_num = set()
    for num in num_list:
        if num not in tmp_set:
            uniq_num.add(num)
        else:
            uniq_num.discard(num)
        tmp_set.add(num)

    nr_list = [num for num in num_list if num in uniq_num]
    return nr_list


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# решение в лоб
print(non_repeating(src))
# решение на хеш таблице
print(non_repeating_opti(src))
