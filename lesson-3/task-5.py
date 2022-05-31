# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


def get_jokes(jokecnt, no_repeat=False):
    """
    Генерирует список шуток
    :param jokecnt: количество необходимых шуток
    :param no_repeat: флаг, запрещающий повторы слов в шутках, если доступные слова закончились,
    возвращает максимально возможный список шуток
    :return: Список шуток
    """
    from random import choice
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = []
    for i in range(0, jokecnt):
        if len(nouns) > 0 and len(adverbs) > 0 and len(adjectives) > 0:
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)

            jokes.append(f'{noun} {adverb} {adjective}')
            if no_repeat:
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)

    return jokes

print(get_jokes(50, True))

