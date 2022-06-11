# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей
# и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа.
# Подумать, какие могут возникнуть проблемы при парсинге.
# В словаре должны храниться данные, полученные в результате парсинга.

def get_el(fname):
    """Возвращает строку из файла в виде кортежа"""
    with open(fname, 'r', encoding='utf-8') as f:
        for ln in f:
            yield tuple(ln.replace("\n", "").split(','))


user = get_el('users.csv')
hobby = get_el('hobby.csv')

with open('user_hobby.txt', 'w', encoding='utf-8') as f:
    f.writelines('{')
    for uh in user:
        hbb = next(hobby, None)
        f.writelines(f'{uh}:{hbb}')
        if hbb:
            f.writelines(',')
    f.writelines('}')
