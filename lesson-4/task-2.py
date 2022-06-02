import requests
import decimal

def currency_rates(fund, url="http://www.cbr.ru/scripts/XML_daily.asp"):
    """
    Возвращает курс валюты по ее коды.
    Реализовано только методами класса str,
    :param fund: код валюты
    :param url: api url, указан по умолчанию
    :return: курс в типе данных decimal. None, в случае некорректных параметров/отсутствия курса/неудачного запроса
    """
    val_tag_start = "<Value>"
    val_tag_end = "</Valute>"

    # Не передан хоть один из параметров - выходим
    if not (fund and url):
        return None

    # Запрашиваем курсы
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if not response.ok:
        return None

    # Находим первое вхождение интересующей нас валюты
    fund_idx = response.text.find(fund.upper())
    if fund_idx == -1:
        return None

    # Отрезаем все лишее с начала строки
    fund_str = response.text[fund_idx:]

    # находим начало и окончание тега со значением валюту
    val_tag_start_idx = fund_str.find(val_tag_start)
    val_tag_end_idx = fund_str.find(val_tag_end)

    # вырезаем значение внутри тега
    val = fund_str[val_tag_start_idx+len(val_tag_start):val_tag_end_idx-len(val_tag_end)]
    val = decimal.Decimal(val.replace(",", "."))

    return val


print(currency_rates(fund="usd"))
print(currency_rates(fund="eur"))
print(currency_rates(fund="eur222"))
