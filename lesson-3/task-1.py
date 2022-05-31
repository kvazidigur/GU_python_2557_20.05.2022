# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
# русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
# информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
# снаружи.


def num_translate(num_en):
    """Переводит числительные от 0 до 10 c английского на русский язык."""
    en_to_ru = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }

    num_ru = None
    if num_en.lower() in en_to_ru:
        num_ru = en_to_ru[num_en.lower()]
    return num_ru


print(num_translate("one"))
print(num_translate("blabla"))
