# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
# Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
import os
import sys


def get_el(fname):
    """Возвращает строку из файла в виде кортежа"""
    with open(fname, 'r', encoding='utf-8') as f:
        for ln in f:
            yield tuple(ln.replace("\n", "").split(','))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit("Некорректное количество агрументов")

    user = get_el(sys.argv[1])
    hobby = get_el(sys.argv[2])

    with open(sys.argv[3], 'w', encoding='utf-8') as f:
        f.writelines('{')
        for uh in user:
            hbb = next(hobby, None)
            f.writelines(f'{uh}:{hbb}')
            if hbb:
                f.writelines(',')
        f.writelines('}')
    exit
