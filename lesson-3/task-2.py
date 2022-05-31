# 2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate_adv(num_en):
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
        if num_en == num_en.capitalize():
            num_ru = en_to_ru[num_en.lower()].capitalize()
        else:
            num_ru = en_to_ru[num_en.lower()]
    return num_ru


print(num_translate_adv("One"))
print(num_translate_adv("one"))
print(num_translate_adv("blabla"))

