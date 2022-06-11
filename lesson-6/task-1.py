# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
remote_addr_pos = 0
request_type_pos = 5
requested_resource_pos = 6
file_name = 'nginx_logs.txt'
parsed_file_name = 'parsed_nginx_logs.txt'


def parse_row(frow):
    tmp_list = frow.replace('"', '').split()
    return tmp_list[remote_addr_pos], tmp_list[request_type_pos], tmp_list[requested_resource_pos]


def parse_file(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        for line in f:
            yield parse_row(line)


# зачитали и сохранили файл
r = requests.get(url=url, timeout=5)
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(r.text)

log_list = []
log_rows = parse_file(file_name)
for row in log_rows:
    log_list.append(row)

print(log_list)
